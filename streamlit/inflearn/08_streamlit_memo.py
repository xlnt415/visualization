import streamlit as st

st.title('memo app')

memo = st.text_area('메모 입력 :', height=200)
save_button = st.button('저장')

if save_button:
  with open('memo.txt', 'w', encoding='UTF-8') as file:
    file.write(memo)
    st.success("메모가 정상적으로 저장되었습니다.")

st.subheader('저장된 메모')

try:
  with open('memo.txt', 'r', encoding='UTF-8') as file:
    saved_memo = file.read()
    st.write(saved_memo)

except FileNotFoundError:
  st.info('저장된 메모가 없습니다.')
