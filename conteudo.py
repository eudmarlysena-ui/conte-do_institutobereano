import streamlit as st

st.set_page_config(
    page_title="Instituto Bereano | Curso de Interpretação e Pregação Expositiva",
    page_icon="📖",
    layout="wide",
)

INTERESSE_URL = "https://institutobereano.streamlit.app/"
WHATSAPP_GROUP_URL = "https://chat.whatsapp.com/F4OsPElqXI2FAvGdj5xpyg"

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #07182f 0%, #0d274a 55%, #050d1a 100%);
    color: white;
}
.block-container {
    padding-top: 2rem;
    max-width: 1150px;
}
.hero {
    text-align: center;
    padding: 3rem 2rem;
    border-radius: 28px;
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(227,199,111,.35);
}
.kicker {
    color: #e3c76f;
    letter-spacing: .18em;
    text-transform: uppercase;
    font-weight: 800;
}
.title {
    font-family: Georgia, serif;
    font-size: 4rem;
    line-height: 1.05;
    font-weight: 700;
}
.subtitle {
    color: #e3c76f;
    font-family: Georgia, serif;
    font-size: 1.5rem;
    font-style: italic;
}
.text {
    color: #d6dde8;
    font-size: 1.08rem;
    line-height: 1.8;
}
.card {
    padding: 1.4rem;
    border-radius: 20px;
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,255,255,.12);
    height: 100%;
}
.card h3 {
    color: #e3c76f;
    font-family: Georgia, serif;
}
.notice {
    padding: 1rem;
    border-radius: 16px;
    background: rgba(227,199,111,.12);
    border: 1px solid rgba(227,199,111,.35);
    color: #f6e7ae;
}
a.button {
    display: inline-block;
    padding: 14px 26px;
    border-radius: 999px;
    background: linear-gradient(90deg, #b8892e, #e3c76f);
    color: #07182f !important;
    font-weight: 800;
    text-decoration: none;
    margin-top: 20px;
}
.footer {
    text-align: center;
    color: #aebbd0;
    padding: 2rem 0;
}
.whatsapp-float {
    position: fixed;
    bottom: 28px;
    right: 28px;
    width: 78px;
    height: 78px;
    border-radius: 50%;
    background: linear-gradient(135deg, #25D366, #128C7E);
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 12px 35px rgba(0,0,0,.45);
    z-index: 99999;
    text-decoration: none;
    transition: all .25s ease;
    border: 3px solid rgba(255,255,255,.25);
}

.whatsapp-float:hover {
    transform: scale(1.08);
    box-shadow: 0 18px 45px rgba(0,0,0,.55);
}

.whatsapp-tooltip {
    position: fixed;
    bottom: 116px;
    right: 24px;
    background: rgba(7, 24, 47, .96);
    color: white;
    padding: 12px 16px;
    border-radius: 14px;
    font-size: 14px;
    font-weight: 700;
    border: 1px solid rgba(227,199,111,.35);
    z-index: 99999;
    box-shadow: 0 10px 25px rgba(0,0,0,.35);
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="hero">
    <div class="kicker">Em breve</div>
    <div class="title">Instituto Bereano</div>
    <div class="subtitle">Da correta interpretação à fiel proclamação.</div>
    <p class="text">
        Curso de <b>Interpretação Bíblica e Pregação Expositiva</b>, pensado para capacitar alunos
        a interpretar corretamente as Escrituras e transformar o texto bíblico em sermões expositivos,
        fiéis ao texto e aplicáveis à igreja contemporânea.
    </p>
    <a class="button" href="{INTERESSE_URL}" target="_blank">Manifestar interesse</a>
</div>
""", unsafe_allow_html=True)

st.markdown("## Visão geral do curso")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card"><h3>Duração</h3><p class="text">6 meses de formação.</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><h3>Total</h3><p class="text">24 aulas semanais.</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="card"><h3>Carga</h3><p class="text">1 aula por semana, de 14h a 17h.</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="card"><h3>Formato</h3><p class="text">Teórico-prático, com produção de sermões.</p></div>', unsafe_allow_html=True)

st.markdown("## Estrutura curricular")

modulos = [
    {
        "titulo": "Módulo 1 — Fundamentos da Interpretação Bíblica",
        "periodo": "Semanas 1–4",
        "conteudo": [
            "Introdução à hermenêutica bíblica",
            "Natureza da revelação e inspiração",
            "Autoridade das Escrituras",
            "Contexto histórico, cultural e literário",
        ],
    },
    {
        "titulo": "Módulo 2 — Hermenêutica Aplicada",
        "periodo": "Semanas 5–8",
        "conteudo": [
            "Gêneros literários bíblicos",
            "Narrativa, poesia, profecia, epístolas e evangelhos",
            "Tipologia e figuras de linguagem",
            "Erros comuns de interpretação",
        ],
    },
    {
        "titulo": "Módulo 3 — Exegese Bíblica",
        "periodo": "Semanas 9–12",
        "conteudo": [
            "Observação do texto",
            "Interpretação correta",
            "Estudo de palavras",
            "Contexto cultural e histórico",
        ],
    },
    {
        "titulo": "Módulo 4 — Teologia Bíblica e Organização do Texto",
        "periodo": "Semanas 13–16",
        "conteudo": [
            "Ideia central do texto",
            "Estrutura do texto bíblico",
            "Teologia do texto",
            "Aplicação bíblica",
        ],
    },
    {
        "titulo": "Módulo 5 — Pregação Expositiva",
        "periodo": "Semanas 17–20",
        "conteudo": [
            "O que é sermão expositivo",
            "Tipos de sermão",
            "Estrutura do sermão",
            "Construção dos pontos",
        ],
    },
    {
        "titulo": "Módulo 6 — Elaboração e Comunicação do Sermão",
        "periodo": "Semanas 21–24",
        "conteudo": [
            "Introdução e conclusão",
            "Ilustrações e aplicação",
            "Comunicação e oratória",
            "Apresentação dos sermões",
        ],
    },
]

for modulo in modulos:
    with st.expander(f"{modulo['titulo']} | {modulo['periodo']}"):
        for item in modulo["conteudo"]:
            st.markdown(f"- {item}")

            st.markdown("## Plano completo de formação — 24 semanas")

plano = {
    "MÊS 1 — Fundamentos": [
        "Aula 1: Introdução ao curso + o que é pregação expositiva",
        "Aula 2: O que é hermenêutica",
        "Aula 3: Inspiração e autoridade bíblica",
        "Aula 4: Contexto histórico e literário",
    ],

    "MÊS 2 — Hermenêutica aplicada": [
        "Aula 5: Gêneros bíblicos (narrativa)",
        "Aula 6: Poesia e sabedoria",
        "Aula 7: Profecia e apocalíptico",
        "Aula 8: Epístolas e evangelhos",
    ],

    "MÊS 3 — Exegese": [
        "Aula 9: Observação do texto",
        "Aula 10: Interpretação correta",
        "Aula 11: Estudo de palavras",
        "Aula 12: Contexto cultural e histórico",
    ],

    "MÊS 4 — Organização do texto": [
        "Aula 13: Ideia central do texto",
        "Aula 14: Estrutura do texto bíblico",
        "Aula 15: Teologia do texto",
        "Aula 16: Aplicação bíblica",
    ],

    "MÊS 5 — Pregação expositiva": [
        "Aula 17: O que é sermão expositivo",
        "Aula 18: Tipos de sermão",
        "Aula 19: Estrutura do sermão",
        "Aula 20: Construção dos pontos",
    ],

    "MÊS 6 — Prática ministerial": [
        "Aula 21: Introdução e conclusão",
        "Aula 22: Ilustrações e aplicação",
        "Aula 23: Comunicação e oratória",
        "Aula 24: Apresentação dos sermões",
    ],
}

col1, col2 = st.columns(2)

items = list(plano.items())

for i, (titulo, aulas) in enumerate(items):
    destino = col1 if i % 2 == 0 else col2

    with destino:
        with st.container():
            st.markdown(f"""
            <div class="card">
                <h3>{titulo}</h3>
            """, unsafe_allow_html=True)

            for aula in aulas:
                st.markdown(f"- {aula}")

            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("## O que o aluno desenvolverá")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <h3>Interpretar</h3>
        <p class="text">Com excelência e responsabilidade bíblica.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>Pregar</h3>
        <p class="text">Com fidelidade ao texto e relevância pastoral.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>Exaltar Cristo</h3>
        <p class="text">Com leitura cristocêntrica equilibrada.</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <h3>Edificar a Igreja</h3>
        <p class="text">Com ensino sólido, bíblico e aplicável.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## Metodologia")

st.markdown("""
<div class="card">
<p class="text">
O curso combinará aulas expositivas, oficinas práticas, leituras orientadas,
produção de esboços, exercícios exegéticos e apresentações orais.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## Sistema de avaliação")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Exercícios interpretativos", "20%")
with col2:
    st.metric("Trabalhos exegéticos", "30%")
with col3:
    st.metric("Produção de sermões", "20%")
with col4:
    st.metric("Sermão final", "30%")

st.markdown("## Bibliografia base")

bibliografia = [
    "Gordon Fee & Douglas Stuart — Entendes o que Lês?",
    "Henry Virkler — Hermenêutica Bíblica",
    "Grant Osborne — A Espiral Hermenêutica",
    "Haddon Robinson — Pregação Bíblica",
    "John Stott — Entre Dois Mundos",
    "David Helm — Pregação Expositiva",
    "Hernandes Dias Lopes — Pregação Expositiva",
]

for livro in bibliografia:
    st.markdown(f"- {livro}")

st.markdown("## Diferenciais do curso")

st.markdown("""
<div class="notice">
Integração total entre interpretação e pregação; foco prático desde o início;
produção real de sermões; formação de pregadores expositivos bíblicos e compromisso
com a fiel exposição das Escrituras.
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align:center; padding:3rem 0;">
    <h2 style="font-family:Georgia,serif;">Deseja receber mais informações?</h2>
    <p class="text">
        As inscrições ainda não estão abertas oficialmente, mas você pode manifestar seu interesse.
    </p>
    <a class="button" href="{INTERESSE_URL}" target="_blank">Manifestar interesse</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    <strong>Instituto Bereano</strong><br>
    “Examinando cada dia nas Escrituras...” — Atos 17.11
</div>
""", unsafe_allow_html=True)
st.markdown(f"""
<div class="whatsapp-tooltip">
    Entre em nosso grupo oficial
</div>

<a href="{WHATSAPP_GROUP_URL}" target="_blank" class="whatsapp-float">
    <svg xmlns="http://www.w3.org/2000/svg" width="42" height="42" fill="white" viewBox="0 0 24 24">
        <path d="M20.52 3.48A11.83 11.83 0 0 0 12.05 0C5.55 0 .25 5.29.25 11.79c0 2.08.54 4.11 1.58 5.9L0 24l6.5-1.7a11.77 11.77 0 0 0 5.55 1.42h.01c6.49 0 11.79-5.29 11.79-11.79 0-3.15-1.23-6.1-3.33-8.45zM12.06 21.5a9.67 9.67 0 0 1-4.93-1.35l-.35-.21-3.86 1.01 1.03-3.76-.23-.39a9.64 9.64 0 0 1-1.49-5.01c0-5.34 4.35-9.69 9.7-9.69 2.58 0 5 .99 6.83 2.82a9.6 9.6 0 0 1 2.84 6.86c0 5.35-4.35 9.72-9.69 9.72zm5.31-7.28c-.29-.15-1.72-.85-1.98-.95-.27-.1-.46-.15-.65.15-.2.29-.75.95-.92 1.15-.17.2-.34.22-.63.08-.29-.15-1.24-.46-2.36-1.48-.87-.77-1.46-1.72-1.63-2.01-.17-.29-.02-.45.13-.6.13-.13.29-.34.44-.51.15-.17.2-.29.29-.49.1-.2.05-.37-.02-.52-.08-.15-.65-1.57-.89-2.15-.24-.58-.49-.5-.65-.5h-.56c-.2 0-.52.08-.79.37-.27.29-1.04 1.02-1.04 2.49s1.06 2.89 1.21 3.09c.15.2 2.08 3.18 5.04 4.46.71.31 1.27.5 1.71.64.72.23 1.37.2 1.89.12.58-.09 1.72-.7 1.96-1.38.24-.68.24-1.26.17-1.38-.07-.12-.26-.2-.56-.35z"/>
    </svg>
</a>
""", unsafe_allow_html=True)
