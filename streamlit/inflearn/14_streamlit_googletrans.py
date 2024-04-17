import streamlit as st
from googletrans import Translator


def translate_text(text):
  translator = Translator()
  translation = translator.translate(text, src='ko', dest='en')
  return translation.text


def main():
  st.title('한국어-영어 번역 프로그램')
  text_input = st.text_input('한국어 문장을 입력하세요.')
  if st.button('번역'):
    if text_input:
      translated_text = translate_text(text_input)
      st.success(f'번역 결과 : {translated_text}')
    else:
      st.warning('입력된 테스트가 없습니다.')


if __name__ == "__main__":
  main()
