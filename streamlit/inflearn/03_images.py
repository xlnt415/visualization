import streamlit as st
import os


#디렉터리의 이미지 경로를 가져옴
def load_imags(dirs):
  images = []
  for filename in os.listdir(dirs):
    if filename.endswith(".JPG") or filename.endswith(".PNG"):
      images_path = os.path.join(dirs, filename)
      images.append(images_path)
  return images


image_dir = "streamlit/inflearn/imgs"
images = load_imags(image_dir)

for image in images:
  st.image(image, width=500)
