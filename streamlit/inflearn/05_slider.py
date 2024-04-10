import streamlit as st

number = st.slider("숫자 선택", 0, 10)
st.write(f"선택한 숫자는 {number}입니다.")

