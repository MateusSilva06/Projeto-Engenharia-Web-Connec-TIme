import Image from "next/image";

export default function LoginPage() {
  return (
    <section className="section-login">
      <div className="container hero-forms" style={{ marginTop: "5rem" }}>
        <div className="form-card">
          <h3>Crie sua conta</h3>

          <p className="form-subtitle">Conecte com uma das plataformas:</p>
                <div className="social-row">
                  <button className="social-btn">
                    <Image src="/logo-Google.png" alt="Google" width={70} height={50} />
                  </button>
                  <button className="social-btn">
                    <Image src="/logo-facebook.png" alt="Logo Facebook" width={50} height={45} />
                  </button>
                  <button className="social-btn">
                    <Image src="/logo-intagram.png" alt="Logo Instagram" width={50} height={45} />
                  </button>
                </div>

          <input className="input" placeholder="Nome completo" />
          <input className="input" placeholder="E-mail" type="email" />
          <input className="input" placeholder="Senha" type="password" />

          <button className="secondary-btn" style={{ width: "100%" }}>
            Cadastrar-se
          </button>
        </div>

        <div className="form-card">
          <h3>Já tem uma conta?</h3>

        <p className="form-subtitle">Conecte com uma das plataformas:</p>
           <div className="social-row">
                  <button className="social-btn">
                    <Image src="/logo-Google.png" alt="Google" width={70} height={50} />
                  </button>
                  <button className="social-btn">
                    <Image src="/logo-facebook.png" alt="Logo Facebook" width={50} height={45} />
                  </button>
                  <button className="social-btn">
                    <Image src="/logo-intagram.png" alt="Logo Instagram" width={50} height={45} />
                  </button>
                </div>
        

          <p className="form-subtitle">Entre com seu e-mail e senha.</p>

          <input className="input" placeholder="E-mail" type="email" />
          <input className="input" placeholder="Senha" type="password" />

          <button className="primary-btn" style={{ width: "100%" }}>
            Entrar
          </button>
        </div>
      </div>
    </section>
  );
}
