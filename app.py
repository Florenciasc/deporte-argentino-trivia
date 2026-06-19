import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="De la Chueca a la Gloria",
    page_icon="🇦🇷",
    layout="wide"
)

@st.cache_data
def cargar_preguntas():
    return pd.read_csv("data/preguntas.csv")

df = cargar_preguntas()

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #07111f, #0b1f36);
    color: white;
}

.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

.hero, .quiz-card, .final-card, .info-card {
    background: linear-gradient(145deg, rgba(13, 37, 63, .95), rgba(5, 14, 27, .95));
    border: 1px solid rgba(116, 172, 223, .25);
    border-radius: 28px;
    padding: 36px;
    box-shadow: 0 20px 60px rgba(0,0,0,.35);
}

.hero {
    min-height: 720px;
    text-align: center;
}

.hero-title {
    font-size: 72px;
    font-weight: 900;
    line-height: 1;
    margin-top: 20px;
}

.hero-title span {
    color: #74ACDF;
}

.hero-subtitle {
    font-size: 22px;
    color: #dbeafe;
    margin: 24px 0;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin: 28px 0;
}

.feature {
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,255,255,.14);
    border-radius: 18px;
    padding: 18px 10px;
}

.feature-icon {
    font-size: 32px;
}

.category {
    display: inline-block;
    background: rgba(116,172,223,.18);
    border: 1px solid rgba(116,172,223,.45);
    color: #9dd7ff;
    padding: 8px 16px;
    border-radius: 12px;
    font-weight: 700;
    margin-bottom: 18px;
}

.question-title {
    font-size: 34px;
    font-weight: 800;
    line-height: 1.25;
    margin-bottom: 24px;
}

.small-text {
    color: #cbd5e1;
    font-size: 16px;
}

div.stButton > button {
    background: linear-gradient(135deg, #1da1f2, #2257d6);
    color: white;
    border: 1px solid rgba(255,255,255,.25);
    border-radius: 14px;
    padding: .85rem 1.6rem;
    font-weight: 800;
    font-size: 1rem;
}

div.stButton > button:hover {
    border-color: #74ACDF;
    box-shadow: 0 8px 24px rgba(29,161,242,.28);
}

[data-testid="stRadio"] label {
    background: rgba(255,255,255,.06);
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 14px;
    padding: 13px 16px;
    margin: 8px 0;
}

@media(max-width: 900px) {
    .hero-title { font-size: 44px; }
    .feature-grid { grid-template-columns: repeat(2, 1fr); }
}
</style>
""", unsafe_allow_html=True)

# Estado
if "inicio" not in st.session_state:
    st.session_state.inicio = False

if "preguntas" not in st.session_state:
    st.session_state.preguntas = df.sample(frac=1).reset_index(drop=True)

if "indice" not in st.session_state:
    st.session_state.indice = 0

if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0

if "respondido" not in st.session_state:
    st.session_state.respondido = False

if "respuesta_usuario" not in st.session_state:
    st.session_state.respuesta_usuario = None


# Inicio
if not st.session_state.inicio:
    col1, col2 = st.columns([1.05, .95], gap="large")

    with col1:
        st.markdown("""
<div class="hero">
    <div style="font-size:52px;">🇦🇷</div>
    <div class="hero-title">De la Chueca<br><span>a la Gloria</span></div>
    <div class="hero-subtitle">
        Un recorrido interactivo por la historia del deporte argentino
    </div>

    <div class="feature-grid">
        <div class="feature">
            <div class="feature-icon">🏃‍♂️</div>
            <div>Pueblos<br>originarios</div>
        </div>
        <div class="feature">
            <div class="feature-icon">🏆</div>
            <div>Clubes e<br>instituciones</div>
        </div>
        <div class="feature">
            <div class="feature-icon">🥇</div>
            <div>Juegos<br>Olímpicos</div>
        </div>
        <div class="feature">
            <div class="feature-icon">🕊️</div>
            <div>Mundial 1978<br>y memoria</div>
        </div>
    </div>

    <p class="small-text">
        Poné a prueba tus conocimientos sobre los momentos, protagonistas
        y hechos que marcaron la historia del deporte en Argentina.
    </p>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class="quiz-card">
    <h2>¿Cómo se juega?</h2>
    <p class="small-text">
        Vas a responder preguntas de opción múltiple sobre los contenidos trabajados en clase.
    </p>
    <br>
    <h3>Incluye:</h3>
    <p>📚 Explicaciones históricas después de cada respuesta.</p>
    <p>🎯 Puntaje acumulado durante la trivia.</p>
    <p>🏁 Resultado final con nivel de conocimiento.</p>
    <br>
    <p class="small-text">
        Ideal para repasar de una forma más visual, interactiva y entretenida.
    </p>
</div>
""", unsafe_allow_html=True)

        st.write("")
        if st.button("🚀 ¡Comenzar a jugar!", use_container_width=True):
            st.session_state.inicio = True
            st.rerun()


# Juego
else:
    total = len(st.session_state.preguntas)
    indice = st.session_state.indice

    if indice < total:
        pregunta_actual = st.session_state.preguntas.iloc[indice]

        st.progress(indice / total)

        col_top1, col_top2, col_top3 = st.columns([1, 1, 1])
        with col_top1:
            st.caption(f"Pregunta {indice + 1} de {total}")
        with col_top3:
            st.caption(f"🏆 Puntaje: {st.session_state.puntaje}/{total}")

        st.write("")

        col1, col2, col3 = st.columns([.15, .7, .15])

        with col2:
            st.markdown(f"""
<div class="quiz-card">
    <div class="category">Categoría: {pregunta_actual["categoria"]}</div>
    <div class="question-title">{pregunta_actual["pregunta"]}</div>
</div>
""", unsafe_allow_html=True)

            opciones = [
                pregunta_actual["opcion_a"],
                pregunta_actual["opcion_b"],
                pregunta_actual["opcion_c"],
                pregunta_actual["opcion_d"],
            ]

            respuesta = st.radio(
                "Elegí una opción:",
                opciones,
                index=None,
                key=f"pregunta_{indice}",
                disabled=st.session_state.respondido
            )

            if st.button(
                "Responder",
                disabled=st.session_state.respondido or respuesta is None,
                use_container_width=True
            ):
                st.session_state.respuesta_usuario = respuesta
                st.session_state.respondido = True

                if respuesta == pregunta_actual["respuesta_correcta"]:
                    st.session_state.puntaje += 1

                st.rerun()

            if st.session_state.respondido:
                correcta = pregunta_actual["respuesta_correcta"]

                if st.session_state.respuesta_usuario == correcta:
                    st.success("✅ ¡Correcto!")
                else:
                    st.error(f"❌ Incorrecto. La respuesta correcta era: {correcta}")

                st.info(f"📚 {pregunta_actual['explicacion']}")

                if st.button("Siguiente pregunta ➡️", use_container_width=True):
                    st.session_state.indice += 1
                    st.session_state.respondido = False
                    st.session_state.respuesta_usuario = None
                    st.rerun()

            st.markdown(f"""
<div class="info-card">
    📊 Llevás respondidas {indice} de {total} preguntas.
</div>
""", unsafe_allow_html=True)


    # Final
    else:
        puntaje = st.session_state.puntaje
        porcentaje = round((puntaje / total) * 100, 1)

        col1, col2, col3 = st.columns([.15, .7, .15])

        with col2:
            st.markdown("""
<div class="final-card" style="text-align:center;">
    <div style="font-size:52px;">🏁</div>
    <h1>Resultado final</h1>
</div>
""", unsafe_allow_html=True)

            st.write("")

            c1, c2 = st.columns(2)
            c1.metric("Puntaje", f"{puntaje}/{total}")
            c2.metric("Porcentaje de aciertos", f"{porcentaje}%")

            if puntaje <= 4:
                nivel = "Principiante del deporte argentino 🐣"
            elif puntaje <= 7:
                nivel = "Aficionada histórica del deporte argentino 🥈"
            else:
                nivel = "Historiadora del deporte nacional 🏆"

            st.success(f"Tu nivel: {nivel}")

            st.markdown("""
<div class="info-card">
    <h3>Reflexión final</h3>
    La historia del deporte argentino no es solo una historia de resultados.
    También habla de identidad, instituciones, política, memoria, género,
    clase social y cultura popular.
</div>
""", unsafe_allow_html=True)

            if st.button("🔄 Reiniciar trivia", use_container_width=True):
                st.session_state.inicio = False
                st.session_state.preguntas = df.sample(frac=1).reset_index(drop=True)
                st.session_state.indice = 0
                st.session_state.puntaje = 0
                st.session_state.respondido = False
                st.session_state.respuesta_usuario = None
                st.rerun()