from lib2to3.pgen2.pgen import DFAState
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

#Importamos la base de datos
data=pd.read_csv("datosfinales.csv")

st.title("Exploración de Airbnb en la Ciudad de México")
st.markdown("Base de datos con la información pública de las ofertas de Airbnb en Ciudad de México")

#LOGO de airbnb
st.sidebar.image("airbnb.jpg")
st.sidebar.markdown("##")

@st.cache
def load_data(nrows):
    return data

data_load_state = st.text('Cargando datos...')
datax = load_data(501)
data_load_state.text("Los datos han sido cargados")

agreex = st.sidebar.checkbox("Mostrar los primeros datos")
if agreex:
    st.header("Todos los datos")
    st.dataframe(datax)


#paso nueve. 
agree9= st.sidebar.selectbox("Selecciona la delegación", data['neighbourhood'].unique())
if st.sidebar.button("Filtrar por delegación"):
    subset_del=data[(data["neighbourhood"]==agree9)]
    st.write(f"Opción seleccionada: {agree9!r}")
    st.write(data.query(f"""neighbourhood==@agree9"""))
    st.map(subset_del)
    st.markdown("_")

#paso 10
agree10= st.sidebar.expander("Rangos de precios", True)
price_minimun = agree10.slider(
    "Precios Mínimos",
    min_value=float(data['price'].min()),
    max_value=float(data['price'].max())
)
price_maximum = agree10.slider(
    "Precios Maximos",
    min_value=float(data['price'].min()),
    max_value=float(data['price'].max())
)
if st.sidebar.button("Filtrar por precios"):
    subset_price = data[ (data['price'] >= price_minimun) & (data['price'] <= price_maximum)]
    st.write(f"Número de registros con precio entre {price_minimun} y {price_maximum}: {subset_price.shape[0]}")
    st.write(subset_price)
    st.map(subset_price)
    st.markdown("_")

#paso 11
agree11= st.sidebar.selectbox("Selecciona tipo de habitación", data['room_type'].unique())
if st.sidebar.button("Filtrar por tipo de habitación"):
    subset_hab=data[(data["room_type"]==agree11)]
    st.write(f"Opción seleccionada: {agree11!r}")
    st.write(data.query(f"""room_type==@agree11"""))
    st.map(subset_hab)
    st.markdown("_")

#GRÁFICOS
#13. 
@st.cache
def load_data(nrows):
    data = pd.read_csv("datosfinales.csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

agree= st.sidebar.checkbox("Histograma de Distribución de los Precios ")
if agree:
    fig, ax = plt.subplots()
    ax.hist(data.price)
    st.header("Histograma Precios")
    st.pyplot(fig)
    st.markdown("_")

#14. 
agree2=st.sidebar.checkbox("Gráfico de precio promedio con tipo de habitación")
if agree2:
    avg_price_room=(data.groupby(by=['room_type'])[['price']].mean().sort_values(by="room_type"))
    fig_price_room=px.bar(avg_price_room,
                        x=avg_price_room.index,
                        y="price", 
                        orientation="v",
                        title="Tipo de habitacion con precio promedio",
                        labels=dict(room_type="Tipo de habitación", price="Precio promedio"),
                        color_discrete_sequence=["#7ECBB4"],
                        template="plotly_white")
    fig_price_room.update_layout(plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_price_room)
    st.markdown("_")

#15. 
agree3=st.sidebar.checkbox("Gráfico de precio promedio por delegación")
if agree3:
    avg_price_n=(data.groupby(by=['neighbourhood'])[['price']].mean().sort_values(by="neighbourhood"))
    fig_price_n=px.bar(avg_price_n,
                        x=avg_price_n.index,
                        y="price", 
                        orientation="v",
                        title="Tipo de delegación con precio promedio",
                        labels=dict(neighbourhood="Tipo de delegación", price="precio"),
                        color_discrete_sequence=["#7ECBB4"],
                        template="plotly_white")
    fig_price_n.update_layout(plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_price_n)


#16
#--- CONCLUSION ---#
agreeconc=st.sidebar.checkbox("Conclusión final")
if agreeconc:
    st.markdown("Conclusión")
    st.markdown("Dentro de esta página web podemos observar que se esta trabajando con una base de datos relacionada con la plataforma de Airbnb dentro de la Ciudad de México, el objetivo de esta página es estimar el precio de renta del departamento de Carina, de igual manera se busca encontrar los factores que dan plusvalia a las propiedades. A través de los diferentes elementos interactivos es más fácil interpretar la información de la base de datos y tomar decisiones. ")

