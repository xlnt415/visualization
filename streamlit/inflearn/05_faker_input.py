import streamlit as st
from faker import Faker

fake = Faker()
st.title("가짜 데이터 정보 생성")

num_users = st.number_input("생성한 사용자 수", min_value=1, max_value=100)

if st.button("사용자 생성하기"):
  for _ in range(num_users):
    name = fake.name()
    email = fake.email()
    address = fake.address()

    st.write(f"이름: {name}")
    st.write(f"이메일: {email}")
    st.write(f"주소: {address}")
    st.write('-------------------')
