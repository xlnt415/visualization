# -*- coding: utf-8 -*-
# 파일명 : 13_select.py

import streamlit as st
import pandas as pd
import seaborn as sns

# 데이터 불러오기
@st.cache_data
def load_data():
    df = sns.load_dataset('iris')
    return df

def main():
    st.title("Choose a plotting library")
    iris = load_data()
    st.markdown("## Raw Data")
    st.dataframe(iris)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("## Select")
    val = st.selectbox("1개의 종을 선택하세요", iris.species.unique())
    st.write("선택된 species : ", val)
    st.dataframe(iris.loc[iris['species']==val, :].reset_index())

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("## MultiSelect")
    cols = st.multiselect("복수의 컬럼을 선택하세요", iris.columns)
    st.write(cols)
    filtered_iris = iris.loc[:, cols]
    st.dataframe(filtered_iris)

if __name__ == '__main__':
    main()
