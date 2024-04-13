import streamlit as st
import yfinance as yf
import time

def get_nasdaq_data():
    symbols = ["MSFT", "AAPL", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "AVGO", "CSCO", "ADBE"]
    nasdaq_data = {}

    progress_bar = st.progress(0)

    for i, symbol in enumerate(symbols):
        data = yf.download(symbol, period="1d", interval="1d")
        nasdaq_data[symbol] = data

        time.sleep(0.05)

        progress_bar.progress((i + 1) / len(symbols))

    return nasdaq_data # 딕셔너리에 저장

# Streamlit 앱 생성
st.title("나스닥 상위 10개 데이터")
st.write("데이터 조회")

# 조회 버튼 클릭 시
if st.button("조회"):
    st.write("나스닥 데이터 조회중..")
    nasdaq_data = get_nasdaq_data()

    # 데이터 출력
    for symbol, data in nasdaq_data.items():
        st.subheader(f"{symbol} 주식")
        st.write(data)