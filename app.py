import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

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
    background: #07111f;
    color: white;
}

.block-container {
    padding-top: 1rem;
    max-width: 1250px;
}

[data-testid="stHeader"] {
    background: rgba(7,17,31,.85);
}

div.stButton > button {
    background: linear-gradient(135deg, #1da1f2, #2257d6);
    color: white;
    border: 1px solid rgba(255,255,255,.25);
    border-radius: 16px;
    padding: .9rem 1.8rem;
    font-weight: 800;
    font-size: 1.05rem;
}

div.stButton > button:hover {
    border-color: #74ACDF;
    box-shadow: 0 8px 24px rgba(29,161,242,.35);
}

[data-testid="stRadio"] label {
    background: rgba(255,255,255,.06);
    border: 1px solid rgba(255,255,255,.14);
    border-radius: 16px;
    padding: 16px 18px;
    margin: 10px 0;
    font-size: 1.1rem;
}

.quiz-box {
    background: linear-gradient(145deg, rgba(19,48,80,.96), rgba(7,20,38,.98));
    border: 1px solid rgba(116,172,223,.25);
    border-radius: 26px;
    padding: 32px;
    box-shadow: 0 18px 55px rgba(0,0,0,.35);
}

.category-pill {
    display: inline-block;
    background: rgba(116,172,223,.20);
    color: #8dd3ff;
    border: 1px solid rgba(116,172,223,.50);
    border-radius: 12px;
    padding: 8px 14px;
    font-weight: 800;
    margin-bottom: 18px;
}

.question-title {
    font-size: 2rem;
    font-weight: 900;
    line-height: 1.25;
    margin-bottom: 22px;
}

.info-box {
    background: rgba(19,48,80,.75);
    border: 1px solid rgba(116,172,223,.20);
    border-radius: 20px;
    padding: 20px;
    margin-top: 20px;
    color: #dbeafe;
}

.final-box {
    background: linear-gradient(145deg, rgba(19,48,80,.96), rgba(7,20,38,.98));
    border: 1px solid rgba(116,172,223,.25);
    border-radius: 26px;
    padding: 42px;
    text-align: center;
    box-shadow: 0 18px 55px rgba(0,0,0,.35);
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Estado
# -------------------------
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


# -------------------------
# Pantalla inicial
# -------------------------
if not st.session_state.inicio:
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        components.html("""
        <div style="
            min-height:680px;
            border-radius:28px;
            padding:30px;
            color:white;
            font-family:Arial, sans-serif;
            text-align:center;
            background:
                linear-gradient(rgba(5,20,38,.76), rgba(5,20,38,.94)),
                radial-gradient(circle at 20% 15%, rgba(116,172,223,.35), transparent 35%),
                radial-gradient(circle at 80% 75%, rgba(29,161,242,.25), transparent 38%),
                linear-gradient(145deg, #16395f, #07111f);
            border:1px solid rgba(116,172,223,.28);
            box-shadow:0 20px 60px rgba(0,0,0,.45);
        ">
            <div style="text-align:right;">
                <span style="
                    border:1px solid rgba(255,255,255,.25);
                    padding:9px 16px;
                    border-radius:14px;
                    color:#dbeafe;
                    font-size:15px;
                ">ⓘ Acerca de esta trivia</span>
            </div>

            <div style="font-size:52px;margin-top:12px;">🇦🇷</div>

            <h1 style="
                font-size:58px;
                line-height:1.05;
                margin:14px 0 10px;
                font-weight:900;
            ">
                De la Chueca<br>
                <span style="color:#74ACDF;">a la Gloria</span>
            </h1>

            <p style="font-size:20px;color:#dbeafe;line-height:1.4;margin:18px 0;">
                Un recorrido interactivo por la historia<br>
                del deporte argentino
            </p>

            <div style="
                display:flex;
                justify-content:center;
                align-items:center;
                gap:14px;
                margin:22px 0;
                font-size:28px;
            ">
                🏹 <span style="color:#74ACDF;">→</span> 🐎 <span style="color:#74ACDF;">→</span> ⚽ <span style="color:#74ACDF;">→</span> 🥇 <span style="color:#74ACDF;">→</span> 🏆
            </div>

            <div style="
                display:grid;
                grid-template-columns:repeat(4,1fr);
                gap:10px;
                margin:22px 0;
                border:1px solid rgba(255,255,255,.16);
                border-radius:20px;
                padding:15px;
                background:rgba(255,255,255,.06);
            ">
                <div>
                    <div style="font-size:30px;">🏃‍♂️</div>
                    <div style="font-size:14px;">Pueblos<br>originarios</div>
                </div>
                <div>
                    <div style="font-size:30px;">🏆</div>
                    <div style="font-size:14px;">Clubes e<br>instituciones</div>
                </div>
                <div>
                    <div style="font-size:30px;">🥇</div>
                    <div style="font-size:14px;">Juegos Olímpicos<br>y hazañas</div>
                </div>
                <div>
                    <div style="font-size:30px;">🕊️</div>
                    <div style="font-size:14px;">Mundial 1978<br>y memoria</div>
                </div>
            </div>

            <p style="font-size:17px;color:#e5eefc;line-height:1.45;">
                Poné a prueba tus conocimientos sobre los momentos, protagonistas
                y hechos que marcaron la historia del deporte en Argentina.
            </p>

            <div style="
                margin:22px auto 0;
                max-width:560px;
                padding:15px;
                border-radius:18px;
                background:rgba(0,0,0,.18);
                border:1px solid rgba(255,255,255,.16);
                color:#dbeafe;
                font-size:15px;
            ">
                💡 Cada pregunta incluye una explicación para que sigas aprendiendo.<br>
                <span style="color:#38bdf8;">¡Muchos éxitos!</span>
            </div>
        </div>
        """, height=700)

    with col2:
        components.html("""
        <div style="
            min-height:620px;
            border-radius:28px;
            padding:32px;
            color:white;
            font-family:Arial, sans-serif;
            background:linear-gradient(145deg, rgba(13,37,63,.96), rgba(5,14,27,.98));
            border:1px solid rgba(116,172,223,.28);
            box-shadow:0 20px 60px rgba(0,0,0,.45);
        ">
            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
                border-bottom:1px solid rgba(255,255,255,.10);
                padding-bottom:16px;
                gap:14px;
            ">
                <div>⌂ Inicio</div>
                <h2 style="margin:0;font-size:22px;">De la Chueca a la Gloria</h2>
                <div style="
                    border:1px solid rgba(255,255,255,.20);
                    padding:10px 14px;
                    border-radius:14px;
                ">🏆 Puntaje: 0 / 10</div>
            </div>

            <div style="
                margin:28px 0;
                height:12px;
                background:rgba(255,255,255,.12);
                border-radius:20px;
            ">
                <div style="
                    width:6%;
                    height:12px;
                    border-radius:20px;
                    background:linear-gradient(135deg,#1da1f2,#2257d6);
                "></div>
            </div>

            <p style="text-align:center;color:#cbd5e1;font-size:18px;">Pregunta 1 de 10</p>

            <div style="
                background:linear-gradient(145deg, rgba(19,48,80,.96), rgba(7,20,38,.98));
                border:1px solid rgba(116,172,223,.22);
                border-radius:24px;
                padding:28px;
                margin-top:22px;
            ">
                <div style="
                    display:inline-block;
                    background:rgba(116,172,223,.2);
                    border:1px solid rgba(116,172,223,.45);
                    color:#8dd3ff;
                    padding:8px 14px;
                    border-radius:12px;
                    font-weight:700;
                ">👥 Categoría: Orígenes</div>

                <h2 style="font-size:27px;line-height:1.25;">
                    ¿Cuáles son las dos raíces principales del deporte argentino?
                </h2>

                <div style="display:grid;gap:12px;">
                    <div style="padding:14px;border-radius:14px;background:rgba(255,255,255,.06);">○ a) Fútbol y rugby</div>
                    <div style="padding:14px;border-radius:14px;background:rgba(255,255,255,.06);">○ b) Pato y polo</div>
                    <div style="padding:14px;border-radius:14px;background:rgba(255,255,255,.06);">○ c) Juegos indígenas y deportes introducidos por los ingleses</div>
                    <div style="padding:14px;border-radius:14px;background:rgba(255,255,255,.06);">○ d) Atletismo y boxeo</div>
                </div>
            </div>

            <div style="
                margin-top:18px;
                padding:18px;
                border-radius:20px;
                background:rgba(19,48,80,.65);
                border:1px solid rgba(116,172,223,.20);
                color:#dbeafe;
                line-height:1.45;
            ">
                📖 <strong style="color:#38bdf8;">¿Sabías que?</strong><br>
                El deporte argentino tiene dos grandes raíces: las prácticas de los pueblos originarios,
                como el Palin y el Pato, y los deportes introducidos por los ingleses.
            </div>
        </div>
        """, height=700)

        st.write("")

        if st.button("🚀 Comenzar recorrido", use_container_width=True):
            st.session_state.inicio = True
            st.toast("¡Comienza el desafío! 🇦🇷🏆")
            st.rerun()


# -------------------------
# Juego
# -------------------------
else:
    total = len(st.session_state.preguntas)
    indice = st.session_state.indice

    if indice < total:
        pregunta_actual = st.session_state.preguntas.iloc[indice]

        st.progress(indice / total)

        col_a, col_b, col_c = st.columns([1, 1, 1])
        with col_a:
            st.caption(f"Pregunta {indice + 1} de {total}")
        with col_b:
            st.markdown("<h3 style='text-align:center;'>De la Chueca a la Gloria</h3>", unsafe_allow_html=True)
        with col_c:
            st.caption(f"🏆 Puntaje: {st.session_state.puntaje}/{total}")

        col1, col2, col3 = st.columns([.15, .7, .15])

        with col2:
            st.markdown(f"""
<div class="quiz-box">
    <div class="category-pill">👥 Categoría: {pregunta_actual["categoria"]}</div>
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

            porcentaje = int((indice / total) * 100)

            st.markdown(f"""
<div class="info-box">
    📊 Llevás respondidas {indice} de {total} preguntas
    <span style="float:right;">{porcentaje}%</span>
</div>
""", unsafe_allow_html=True)


# -------------------------
# Final
# -------------------------
    else:
        puntaje = st.session_state.puntaje
        porcentaje = round((puntaje / total) * 100, 1)

        col1, col2, col3 = st.columns([.15, .7, .15])

        with col2:
            st.markdown("""
<div class="final-box">
    <div style="font-size:56px;">🏁</div>
    <h1>Resultado final</h1>
</div>
""", unsafe_allow_html=True)

            c1, c2 = st.columns(2)
            c1.metric("Puntaje", f"{puntaje}/{total}")
            c2.metric("Porcentaje de aciertos", f"{porcentaje}%")

            if puntaje <= 4:
                nivel = "🏹 Exploradora de los Orígenes"
                mensaje = "Conocés algunos puntos de partida, pero todavía queda mucho recorrido histórico por descubrir."
            elif puntaje <= 8:
                nivel = "🥈 Cronista del Deporte Argentino"
                mensaje = "Tenés una muy buena base para interpretar hechos, protagonistas e instituciones."
            elif puntaje < total:
                nivel = "🏆 Guardiana de la Historia Deportiva"
                mensaje = "Dominás gran parte del recorrido histórico del deporte argentino."
            else:
                nivel = "👑 Leyenda de la Chueca a la Gloria"
                mensaje = "¡Puntaje perfecto! Conocés los hitos principales de la historia deportiva nacional."

            st.success(f"Tu nivel: {nivel}")

            st.markdown(f"""
<div class="info-box">
    <h3>Reflexión final</h3>
    <p>{mensaje}</p>
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