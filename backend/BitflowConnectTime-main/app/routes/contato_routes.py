import csv
import io
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.usuario_model import UsuarioModel
from app.schemas.contato_schema import ContatoCreate, ContatoResponse, ContatoUpdate
from app.repositories.contato_repository import ContatoRepository
from app.depedencies import obter_usuario_atual

# Criamos o roteador (semelhante ao 'Route::' do Laravel)
router = APIRouter()

@router.post("/", response_model=ContatoResponse)
def criar_contato(
    contato: ContatoCreate, 
    db: Session = Depends(get_db),
    usuario_atual: UsuarioModel = Depends(obter_usuario_atual)
):
    return ContatoRepository(db).criar(contato)

@router.get("/", response_model=List[ContatoResponse])
def listar_contatos(
    search: str = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, le=100),
    db: Session = Depends(get_db),
    usuario_atual: UsuarioModel = Depends(obter_usuario_atual)
):
    return ContatoRepository(db).listar(search, skip, limit)

@router.get("/{contato_id}", response_model=ContatoResponse)
def obter_contato(
    contato_id: int,
    db: Session = Depends(get_db),
    usuario_atual: UsuarioModel = Depends(obter_usuario_atual)
):
    contato = ContatoRepository(db).obter_por_id(contato_id)
    if not contato:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return contato

@router.put("/{contato_id}", response_model=ContatoResponse)
def atualizar_contato(
    contato_id: int,
    contato_atualizado: ContatoUpdate,
    db: Session = Depends(get_db),
    usuario_atual: UsuarioModel = Depends(obter_usuario_atual)
):
    contato = ContatoRepository(db).atualizar(contato_id, contato_atualizado)
    if not contato:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return contato

@router.delete("/{contato_id}")
def deletar_contato(
    contato_id: int,
    db: Session = Depends(get_db),
    usuario_atual: UsuarioModel = Depends(obter_usuario_atual)
):
    if not ContatoRepository(db).deletar(contato_id):
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return {"detail": "Deletado com sucesso"}

@router.get("/exportar/csv")
def exportar_contatos(
    db: Session = Depends(get_db),
    usuario_atual: UsuarioModel = Depends(obter_usuario_atual)
):
    repo = ContatoRepository(db)
    contatos = repo.listar()
    
    stream = io.StringIO()
    csv_writer = csv.writer(stream)
    csv_writer.writerow(["ID", "Nome", "Telefone", "Email", "Grupo", "Favorito"])
    
    for c in contatos:
        csv_writer.writerow([c.id, c.nome, c.telefone, c.email, c.grupo, c.is_favorito])
    
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=contatos.csv"
    return response
