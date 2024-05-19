import streamlit as st
import pandas as pd

# from home import run_home
# from eda.eda_home import run_eda
from utils import load_data

def main():


    # total_df = pd.read_excel(r'G:\내 드라이브\xlnt_space\시각화\Streamlit\Superstore.xls', engine='openpyxl')
    total_df = pd.read_csv(r'G:\내 드라이브\xlnt_space\시각화\Streamlit\Superstore.csv')

    # total_df = pd.read_excel('https://query.data.world/s/74lebxp22q3ki6cepj24rfreadliby?dws=00000')

    # 페이지 제목 설정
    st.title("Sales Dashboard")

    # 주요 메트릭 설정
    total_sales = int(total_df.Sales.sum())
    total_profit = int(total_df.Profit.sum())
    total_quantity = int(total_df.Quantity.sum())
    avg_discount = total_df.Discount * 100

    # 메트릭 표시
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Sales", f"${total_sales:,}")
    with col2:
        st.metric("Profit", f"${total_profit:,}")
    with col3:
        st.metric("Quantity", f"{total_quantity:,}")
    with col4:
        st.metric("Avg. Discount", f"{avg_discount}%")


if __name__ == "__main__":
    main()