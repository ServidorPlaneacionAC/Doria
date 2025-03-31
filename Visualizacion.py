import streamlit as st
# from Optimizador import optimizar, generar_dataframe_calculo_Kg
from Visualizador_Pricing import CLS_Visualizacion_pricing
# from Visualizador_variacion_costos import CLS_Visualizacion_variacion_costos

class CLS_Estructura_Visualizacion:
    '''
    clase que permite ser la estrutura inicial de la visualización en streamlit, primer paso en la estandarización de desarrollos 
    '''
    def __init__(self) -> None:
      self.mostrar_navegabilidad(["Inicio"])
      
    def mostrar_navegabilidad(self,paginas=["Inicio"]):
        '''
        Genera el slider que permite navegar entre interfaces del desarrollo

        Parametros:
        paginas [list]: definir las paginas que iran en el slider
        '''
        st.sidebar.header("Navegación")
        page = st.sidebar.radio("Ir a:", paginas)

        if page == "Inicio":
            self.Mostrar_Pantalla_principal('Ingreso de datos')
        # elif page == "Archivos de muestra":
        #     self.Mostrar_Pantalla_variacion_costos('Archivos de muestra')
        # elif page=="¿Cómo funciona?":
        #     self.Mostrar_Pantalla_como_funciona('¿Cómo funciona?')
      
    def Mostrar_Pantalla_principal(self, titulo) -> None:
        '''
        Genera la pantalla principal, habilita la impresión del df de muestra, carga y trasnformación de datos
        
        Parametros:
        titulo (str): Indica el titulo de la página actual
        '''
        st.title(titulo)
        st.header("Validación de costos")

        pricing=CLS_Visualizacion_pricing()    
      
  
    def Mostrar_Pantalla_variacion_costos(self, titulo) -> None:
        '''
        Genera la pantalla principal, habilita la impresión del df de muestra, carga y trasnformación de datos
        '''
        # variacion_costos=CLS_Visualizacion_variacion_costos()
