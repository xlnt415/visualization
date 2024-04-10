import streamlit as st

name = st.text_input("이름을 작성하세요., ex)홍길동")

st.write(f"안녕하세요. {name}님")

age = st.number_input("나이를 입력하세요", min_value=0, max_value=999)
st.write(f'당신의 나이는 {age}입니다.')

options = ["서울시", "성남시", "수원시"]

selected_option = st.selectbox("지역을 선택하세요", options)

st.write(f'{name}님은 {selected_option}에 사시네요!')
