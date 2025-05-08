import streamlit as st
#le pones de nick st a la libreria porque la llamamos mucho
import time

#---configuracion inicial de la pagina---
st.set_page_config(page_title="Demo de streamlit", page_icon=">:(", layout="wide")

#--ESCRITURA--

#titulo
st.title("Demo completa de componentes de streamlit")
#subtitulo o encabezado
st.header("Explorando los elementos basicos")

#---MENU--

menu1, menu2,menu3 = st.columns(3)
with menu1:
    if st.button("Inicio"):
        st.success("No va a pasar nada nunca")
with menu2:
    st.button("Productos")
with menu3:
    st.button("Sobre nosotros")



#--ELEMENTOS DEL TEXTO--

st.subheader("Texto enriquecido")
st.text("Esto es un texto simple")
st.markdown("**Este texto está en negrita** y este en *cursiva*")
st.code("print('Hola mundo')", language="python")

#--WIDGETS--

st.subheader("Widgets interactivos")
#boton
if st.button("Click aqui"):
    st.success("¡Bien hecho crak!")

opcion= st.selectbox("Selecciona una opción", ["A","B","C"])
st.write(f"Has seleccionado {opcion}")

ingredientes=st.multiselect("Selecciona tus ingredientes fav",
                            ["Huevo","Pollo","Patata"])

#--SLIDER--

st.subheader("Slider")
valor=st.slider("Selecciona un valor", 0, 100, 25)
st.write(f"Has seleccionado {valor}")

#--INPUTS--

st.subheader("Inputs")
nombre=st.text_input("Dime tu nombre")
edad=st.text_input("Dime tu edad")
edad2=st.number_input("Cual es tu edad? version mejorada", min_value=1, max_value=120, step=1)
st.write(f"Te llamas {nombre} y tienes {edad} años")

#--ELEMENTOS MULTIMEDIA--

st.subheader("Elementos multimedia")
st.image("https://static.wikia.nocookie.net/naruto/images/1/12/La_Promesa_de_Naruto.png/revision/latest?cb=20110825232746&path-prefix=es", caption="Imagen desde la web")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.video("https://www.youtube.com/watch?v=xvFZjo5PgG0")

#--ESTADOS--

st.subheader("Estados")
#este if lo que hace es reiniciar el contador cuando se recarga pag
if "contador" not in st.session_state:
    st.session_state.contador=0

incrementar= st.button("Incrementar contador")

if incrementar:
    st.session_state.contador+=1
st.write(f"Contador {st.session_state.contador}")

#--BARRA DE PROGRESO--

st.subheader("Barra de progreso")
progreso=st.progress(0)
for porcentaje in range(0,101,10):
    #esto hace que se rellene solo cada 1 segundo (pantallas de carga por ejemplo)
    time.sleep(0.7)
    progreso.progress(porcentaje)

#--DISEÑOS Y CONTENEDORES--

st.subheader("Diseños y contenedores")
col1, col2 = st.columns(2)

with col1:
    st.info("Esta es la columna 1")
with col2:
    st.warning("Esta es la columna 2")
with st.expander("Haz click para expandir"):
    st.write("Aqui puedes ocultar o mostrar contenido")

col3, col4 = st.columns(2)
with col3:
    st.info("Esta es la columna 1")
with col4:
    st.warning("Esta es la columna 2")

st.success("¡Fin de la demostración!")




