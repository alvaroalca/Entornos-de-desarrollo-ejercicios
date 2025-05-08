import streamlit as st
#le pones de nick st a la libreria porque la llamamos mucho

#---configuracion inicial de la pagina---
st.set_page_config(page_title="Demo de streamlit", page_icon=">:(", layout="wide")

#--ESCRITURA--

#titulo
st.title("Demo completa de componentes de streamlit")
#subtitulo o encabezado
st.header("Explorando los elementos basicos")

#--ELEMENTOS DEL TEXTO--

st.subheader("Texto enriquecido")
st.text("Esto es un texto simple")
st.markdown("**Este texto está en negrita** y este en *cursiva*")
st.code("print('Hola mundo')", language="python")

#--WIDGETS--

st.subheader("Widgets interactivos")
if st.button("Click aqui"):
    st.success("¡Bien hecho crak!")
