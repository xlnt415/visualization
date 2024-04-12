import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader('엑셀 파일 업로드', type=['log'])

if uploaded_file is not None:
  logs = uploaded_file.read().decode('utf-8')

  log_lines = logs.split('\n')
  # log_datas = []

  # for line in log_lines:
  #   log_data = line.split(' ')
  #   log_datas.append(log_data)

  log_data = [line.split(' ') for line in log_lines]

  df = pd.DataFrame(log_data)
  st.write(df)
