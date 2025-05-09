import streamlit as st

#--configuración de la pestaña--
st.set_page_config(page_title="Ciudades del mundo", page_icon="https://cdn-icons-png.flaticon.com/512/1034/1034253.png", layout="wide")

#--título y subtítulo--
st.title("Ciudades del mundo")
st.subheader("Explora tres ciudades fascinantes")

#--definimos las imagenes y descripciones como arrays para usarlos mas sencillo (ya que solo son 3 y quiero probar)--
imagenes = [
    "https://www.hola.com/horizon/square/31b5c744d9b7-zaragoza-imprescindibles-t.jpg?im=Resize=(640),type=downsize",
    "https://beachatlas.s3.us-east-2.amazonaws.com/platja-la-grava.jpg",
    "https://www.hola.com/horizon/original_aspect_ratio/c621e545d725-catedral-jaen-a.jpg?im=Resize=(640),type=downsize"
]
descripcion = [
    "Zaragoza es la ciudad más calurosa en la que he vivido. Jamás en mi vida he pasado tanto calor como aquí en verano.",
    "Jávea es la ciudad donde he veraneado siempre, tiene las calas más bonitas que haya podido ver por esta zona.",
    "Jaén es una ciudad curiosa que, desde que fui, ha crecido bastante. Aún me acuerdo cuando no existía ni el ferrocarril fantasma que hay ahora."
]

#--creamos las columnas--
col1, col2, col3 = st.columns(3)

#--mostramos las columnas con su descripción--
with col1:
    #uso use_container_width para ajustar la imagen en caso de que alguna fuera más grande
    st.image(imagenes[0], use_container_width=True)
    #con el expander muestro el nombre de la ciudad sin usar headers antes ni nada
    with st.expander("Descripción de Zaragoza"):
        st.write(descripcion[0])

with col2:
    st.image(imagenes[1], use_container_width=True)
    with st.expander("Descripción de Jávea"):
        st.write(descripcion[1])

with col3:
    st.image(imagenes[2], use_container_width=True)
    with st.expander("Descripción de Jaén"):
        st.write(descripcion[2])
