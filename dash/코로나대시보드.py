import pandas as pd
import numpy as np

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import plotly.graph_objects as go
from plotly.colors import DEFAULT_PLOTLY_COLORS
import plotly.subplots as make_subplots

import io
import base64
import os


# 파일이 저장된 경로 설정
file_path = r"G:\내 드라이브\xlnt_space\dash\rawdata"

# 디렉토리 내의 모든 파일 리스트 가져오기
file_list = os.listdir(file_path)

# 'disease'를 포함하는 파일만 선택하여 결합
disease_files = [file for file in file_list if 'disease' in file]

# 파일들을 읽어서 DataFrame으로 결합
dfs = [pd.read_csv(os.path.join(file_path, file)) for file in disease_files]

# DataFrame들을 결합하여 하나의 DataFrame으로 만들기
df_disease = pd.concat(dfs)

button = ['Accute Respiratory Infection', 'Influenza', 'Streptococcus Pneumoniae']
# 상단 중앙에 제목 위치, 하단 영역은 탭 기능 사용

# App structure
app = dash.Dash(__name__)
app.title = ('Dashboard | COVID-19 & Resiratory Disease Data')
server = app.server

# App layout
app.layout = html.Div([
    # main title
    html.H2('COVID-19 유행이 한국의 호흡기 질환 발생 추이에 미치는 영향', style={'textAlign': 'center'}),

    dcc.Tabs([
        # Tab 1
        dcc.Tab(label='대시보드',
                style={'padding': '3px', 'fontWeight': 'bold', 'borderBottom': '1px solid #d6d6d6'},
                selected_style={'padding': '3px', 'backgroundColor': '#119DFF', 'color': 'white',
                              'borderBottom': '1px solid #d6d6d6', 'borderTop': '1px solid #d6d6d6'},

                children=[
                    html.Div([
                        html.P('질병 유형: '),
                        dcc.RadioItems(id='radio',
                                       options=[{'label': i, 'value': i} for i in button],
                                       value='급성 호흡기 감염',
                                       labelStyle={'display': 'block'})
                    ])
                ]),
        # Tab 2
        dcc.Tab(label='업로드',
                style={'padding': '3px', 'fontWeight': 'bold', 'borderBottom': '1px solid #d6d6d6'},
                selected_style={'padding': '3px', 'backgroundColor': '#119DFF', 'color': 'white',
                                'borderBottom': '1px solid #d6d6d6', 'borderTop': '1px solid #d6d6d6'})

    ])
])




# Run App
if __name__ == '__main__':
    app.run_server(debug=False)
