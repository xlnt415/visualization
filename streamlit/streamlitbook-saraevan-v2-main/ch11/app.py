# -*- coding:utf-8 -*-

import streamlit as st 
import matplotlib.pyplot as plt 
from google.oauth2 import service_account
from google.cloud import bigquery
import plotly.express as px
import google.auth
from google.auth import compute_engine

# Local에 저장된 json 파일 불러오기
try:
    credentials = service_account.Credentials.from_service_account_file(r'secrets/streamlitbook-evan-56b081bf2897.json')
except:
    credentials, project_id = google.auth.default()
    credentials = compute_engine.Credentials(
        service_account_email=credentials.service_account_email)

# GCP 프로젝트
project_id = 'streamlitbook-evan'
client = bigquery.Client(credentials = credentials, project=project_id)

@st.cache_data(ttl=600)
def getData(query):
    data = client.query(query).to_dataframe()
    int64_columns = data.select_dtypes(include='Int64').columns
    data[int64_columns] = data[int64_columns].astype('float64')
    print(data.info())
    return data

def plotly_chart(data, feature):
    main_features = ['LotArea', 'GrLivArea', 'SalePrice']
    chart_features = main_features + [feature]
    DF = data[chart_features]

    # main plot (scatter)
    fig = px.scatter(DF,
                    x='GrLivArea',
                    y='SalePrice',
                    color=feature,
                    size='LotArea',
                    width=750,
                    height=400)

    # annotation (text)
    fig.add_annotation(text="Possible outliers",
                    xref="x", yref="y",
                    x=6200,y=160000,
                    showarrow = True,                   
                    yshift=30,
                    xshift=-60,
                    font=dict(
                        family="sans serif",
                        size=12,
                        color="LightSeaGreen"
                        )
                    )
    # annotation (box)
    fig.add_shape(type="rect",
                xref="x", yref="y",
                x0=4500, x1=5800, y0=100000, y1=250000,
                fillcolor="lightgray",    
                line_color="black",
                opacity=0.3
                )
    # update the plot
    fig.update_layout(title='<b>House Price vs GrLivArea<b>',
                    titlefont={'size': 24}
                    )
    st.plotly_chart(fig)

def main():
    st.title("Hello GCP from Local")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot([1, 2, 3, 4, 3, 2, 1])
    ax.set_title("Hello Plot from Local PC")
    st.pyplot(fig)
    
    st.markdown("<hr>", unsafe_allow_html = True)
    st.markdown("""
    <style>
    .gcp-font {
        font-size:32px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="gcp-font">BigQuery with Streamlit</p>', unsafe_allow_html=True)

    query = '''
        SELECT * FROM `streamlitbook-evan.kaggle.transformed_train`
    '''

    data = getData(query)
    st.dataframe(data.head(3))

    object_feature = st.selectbox("Select....", ("OverallQual", "ExterQual", "RoofStyle"), index=0) 
    plotly_chart(data, object_feature)
    st.markdown('<p class="gcp-font">BigQuery with Streamlit in GCP 성공!!</p>', unsafe_allow_html=True)

    

if __name__ == "__main__":
    main()
