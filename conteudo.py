import streamlit as st

st.set_page_config(
    page_title="Instituto Bereano | Curso de Interpretação e Pregação Expositiva",
    page_icon="📖",
    layout="wide",
)

INTERESSE_URL = "https://institutobereano.streamlit.app/"

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
    st.markdown('<div class="card"><h3>Carga</h3><p class="text">1 aula por semana, de 2h a 2h30.</p></div>', unsafe_allow_html=True)
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
