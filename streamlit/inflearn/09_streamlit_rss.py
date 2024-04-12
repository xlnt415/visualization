import streamlit as st
import feedparser

st.title('RSS 항목 정보 가져오기')

rss_url = st.text_input('RSS 주소를 입력하세요.')

if st.button('가져오기'):
  if not rss_url:
    st.warning("RSS 주소를 입력하세요.")

  else:
    feed = feedparser.parse(rss_url)

    if 'entries' in feed:
      for entry in feed.entries:
        st.write(f"제목 :{entry.title}")
        st.write(f"링크 :{entry.link}")
        st.write(f"요약 :{entry.summary}")

    else:
      st.warning("해당 RSS 주소로부터 항목을 가져올 수 없습니다.")
