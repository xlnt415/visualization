import streamlit as st
import pandas as pd
from collections import Counter

uploaded_file = st.file_uploader('엑셀 파일 업로드', type=['log'])

if uploaded_file is not None:
  logs = uploaded_file.read().decode('utf-8')

  log_lines = logs.split('\n')

  ip_addresses = [line.split(' ') for line in log_lines]

  top_ip_addresses = Counter(ip_addresses).most_common(10)

  st.subheader('상위 10개 IP 주소')

  for ip, count in top_ip_addresses:
    st.write(f'IP주소: {ip}, 출현 횟수: {count}')
