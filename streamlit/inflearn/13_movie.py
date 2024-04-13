import requests
import streamlit as st

def search_movie(title):
    # OMDB API 요청을 위한 URL
    url = f"http://www.omdbapi.com/?apikey=276718f0&t={title}"

    # API 요청 보내기
    response = requests.get(url)

    # 응답 데이터 확인
    data = response.json()

    if data["Response"] == "False":
        return None

    # 영화 정보 추출
    movie_title = data["Title"]
    movie_year = data["Year"]
    movie_poster = data["Poster"]

    return movie_title, movie_year, movie_poster

# Streamlit 애플리케이션 시작
st.title("영화 검색 앱")
movie_title = st.text_input("영화 제목을 입력하세요")

if st.button("검색"):
    if movie_title:
        movie_data = search_movie(movie_title)

        if movie_data is not None:
            title, year, poster = movie_data

            # 영화 정보 출력
            st.subheader("검색 결과")
            st.write("제목:", title)
            st.write("제작년도:", year)
            st.image(poster, caption=title, use_column_width=True)
        else:
            st.error("검색 결과를 찾을 수 없습니다.")
    else:
        st.warning("영화 제목을 입력하세요.")