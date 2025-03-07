import streamlit as st
import pandas as pd
from datetime import datetime


df_data = pd.read_csv("FIFA23/datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]

clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_filtered = df_data[(df_data['Club'] == club)].set_index('Name')
st.image(df_filtered.iloc[0]['Club Logo'])
st.markdown(f'## {club}')

collumns = ['Age', 'Photo', 'Flag', 'Overall', 'Value(£)', 'Wage(£)', 'Joined', 'Height(cm.)', 'Weight(lbs.)', 'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtered[collumns], 
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     'Overall', format='%d', min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn(
                     'Weekly Wage', format='£%f', min_value=0, max_value=df_filtered['Wage(£)'].max()),
                'Photo': st.column_config.ImageColumn(),
                'Flag': st.column_config.ImageColumn('Country')
             })
