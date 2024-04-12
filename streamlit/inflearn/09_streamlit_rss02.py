import streamlit as st
import feedparser

st.title("RSS 항목 정보 가져오기")

rss_urls = {
    "보안뉴스 Security": "http://www.boannews.com/media/news_rss.xml?mkind=1",
    "보안뉴스 IT": "http://www.boannews.com/media/news_rss.xml?mkind=2",
    "데일리시큐 IT": "https://www.dailysecu.com/rss/allArticle.xml"
}

selected_rss = st.selectbox("RSS 주소를 입력하세요.", list(rss_urls.keys()))

if st.button("가져오기"):
    rss_url = rss_urls.get(selected_rss)

    if not rss_url:
        st.warning("RSS 주소를 입력하세요.")
    else:
        feed = feedparser.parse(rss_url)
        if "entries" in feed:
            for entry in feed.entries:
                st.write(f"제목:{entry.title}")
                st.write(f"링크:{entry.link}")
                st.write(f"요약:{entry.summary}")
        else:
            st.warning("해당 RSS 주소로부터 항목을 가져올 수 없습니다.")