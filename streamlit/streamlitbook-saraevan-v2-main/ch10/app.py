# -*- coding:utf-8 -*-

import streamlit as st 
import matplotlib.pyplot as plt 

def main():
    st.title("Hello GCP from Local")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot([1, 2, 3, 4, 3, 2, 1])
    ax.set_title("Hello Plot from Local PC")
    st.pyplot(fig)

if __name__ == "__main__":
    main()