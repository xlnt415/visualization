import streamlit as st
import time

prograss_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

for i in range(1, 101):
  if i == 100:
    status_text.text('진행 완료')

  else:
    status_text.text(f'{i}% 진행중')

  prograss_bar.progress(i)
  time.sleep(0.05)

prograss_bar.empty()
st.button('다시 진행')


  