import pandas as pd
import streamlit as st

uploaded_file = st.file_uploader('엑셀 파일 업로드', type=['xlsx'])

if uploaded_file is not None:
  df = pd.read_excel(uploaded_file)
  st.write(df)
