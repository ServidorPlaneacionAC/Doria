import streamlit as st
import pandas as pd
# from Optimizador import optimizar, generar_dataframe_calculo_Kg, generar_dataframe_calculo_total,calcular_kg_equivalentes
# import mplcursors
from plotly.subplots import make_subplots
import plotly.graph_objs as go

class CLS_Visualizacion_pricing:
    '''
    clase que permite tener todas las particularidades necesarias
      para la visualización del modelo de pricing
    '''
    def __init__(self) -> None:

        costo_capital = st.slider("Costo capital esperado (términos porcentuales)", 0, 100, value=12)

        archivo_usuario = st.file_uploader("Arcos", type=["xlsx"])

        if archivo_usuario is not None:
            df_arcos = pd.read_excel(archivo_usuario, sheet_name="arcos")
            df_vehiculos = pd.read_excel(archivo_usuario, sheet_name="vehiculos")
            parametrosWA = pd.read_excel(archivo_usuario, sheet_name="vehiculos")
            
        if st.button('Evaluar'):
            st.write('como ver la actualización')