import streamlit as st
import Imports
import time
import pandas as pd
from datetime import datetime


st.title('FIFA 23 OFFICIAL DATASET!')
btn = st.link_button('Acesse os dados no Kaggle', 'https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset')


st.markdown('''
    Este dataset há **mais de 17.000 registros** de jogadores baseados em dados do FIFA
    23. Contém porte físico dos jogadores e os dados de **2017 a 2023,** e até detalhes
    dos contratos e preço dos jogadores.     
''')

if 'data' not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    st.session_state['data'] = df_data


Imports.escrevendo(st.markdown('''
      :gray[Feito por: Ronaldo Trindade Salustiano]  
'''))