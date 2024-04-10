import streamlit as st

def main():
    st.title("액자 사진 갤러리")
    uploaded_files = st.file_uploader("여러 사진 파일을 업로드하세요.", accept_multiple_files=True)

    if uploaded_files:
        image_files = list(uploaded_files)
        image_files.sort(key=lambda x: x.name)

        st.write(f"총 {len(image_files)}개의 사진이 업로드 되었습니다.")

        index = st.slider("이미지 선택", 0, len(image_files)-1, 0)
        st.image(image_files[index], use_column_width=True, caption=image_files[index].name)

if __name__ == '__main__':
    main()