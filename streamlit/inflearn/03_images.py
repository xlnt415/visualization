import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Streamlit 웹 애플리케이션의 제목 설정
st.title('URL을 통해 이미지 로드하기')

# 사용자로부터 이미지 URL 입력 받기
image_url = st.text_input('이미지 URL을 입력하세요:')
