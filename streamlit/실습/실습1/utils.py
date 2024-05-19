import requests
import pandas as pd
import streamlit as st
import requests


@st.cache_data
def load_data():

    url = 'https://query.data.world/s/kgf77cgiqf3bmqm27rhov6lmkh6m3x?dws=00000'
    df = pd.read_excel(url, engine='openpyxl')
    return df


