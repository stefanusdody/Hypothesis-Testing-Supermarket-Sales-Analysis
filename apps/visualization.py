import plotly.express as px
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app


# Data Preprocessing
df = pd.read_csv('supermarket_sales - Sheet1.csv')

# Merubah format date
df['Date'] = pd.to_datetime(df['Date'])

# Membuat variabel Year dan Month
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# membuat variabel available_city
available_city = df['City'].unique()

layout = html.Div([
    dbc.Container([

      # Penjualan and Gross Income Visualization
         dbc.Row([
             dbc.Col(
                 html.H3("Visualisasi Total Penjualan dan Gross Income"),
                 className="mb-2 mt-4"
             )
         ]),
         dbc.Row([
             dbc.Col(
                 html.A(children='Visualisasi untuk melihat Total Penjualan dan Gross Income diseluruh Cabang'),
                 className="mb-4"
             )
         ]),
         dbc.Row([
             dbc.Col(
                 dcc.Dropdown(
                     id='selected_payment',
                     options=[
                        {'label': city, 'value': city} for city in available_city
                     ],
                     value='Yangon',
                 ),
                 className="mb-4"
             )
         ]),
         dbc.Row([
             dbc.Col(
                 dcc.Graph(
                     id='main-graph-payment'
                 )
             )
         ]),

      # Total Penjualan Per Customer Type Visualization
         dbc.Row([
             dbc.Col(
                 html.H3("Visualisasi Total Penjualan Per Customer Type"),
                 className="mb-2 mt-4"
             )
         ]),
         dbc.Row([
             dbc.Col(
                 html.A(children='Visualisasi untuk melihat Total Penjualan perbulan yang diterima oleh kantor cabang dari setiap Member atau Non Member Customer '),
                 className="mb-4"
             )
         ]),
         dbc.Row([
             dbc.Col(
                 dcc.Dropdown(
                     id='selected_city_total',
                     options=[
                        {'label': city, 'value': city} for city in available_city
                     ],
                     value='Yangon',
                 ),
                 className="mb-4"
             )
         ]),
         dbc.Row([
             dbc.Col(
                 dcc.Graph(
                     id='main-graph-city-total'
                 )
             )
         ]),


      # Gross Income per Customer Type Visualization
        dbc.Row([
            dbc.Col(
                html.H3("Visualisasi Gross Income per Customer Type"),
                className="mb-2 mt-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.A(children='Visualisasi untuk melihat Gross Income perbulan yang diterima oleh kantor cabang dari setiap Member atau Non Member Customer'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_city_gross',
                    options=[
                       {'label': city, 'value': city} for city in available_city
                    ],
                    value='Yangon',
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='main-graph-city-gross'
                )
            )
        ]),


    # Product Line Visualization
       dbc.Row([
           dbc.Col(
               html.H3("Visualisasi Gross Income Per Product Line"),
               className="mb-2 mt-4"
           )
       ]),
       dbc.Row([
           dbc.Col(
               html.A(children='Visualisasi untuk melihat Gross Income dari setiap pembelian jenis product yang dilakukan oleh Member atau Non Member'),
               className="mb-4"
           )
       ]),
       dbc.Row([
           dbc.Col(
               dcc.Dropdown(
                   id='selected_product',
                   options=[
                      {'label': city, 'value': city} for city in available_city
                   ],
                   value='Yangon',
               ),
               className="mb-4"
           )
       ]),
       dbc.Row([
           dbc.Col(
               dcc.Graph(
                   id='main-graph-product'
               )
           )
       ])

    ])
])

# Penjualan and Gross Income Callback
@app.callback(
    Output('main-graph-payment', 'figure'),
    Input('selected_payment', 'value')
)
def update_payment_chart(city):
    fig = px.scatter(df, x='Total' , y='gross income')
    return fig

# Total Penjualan Per Customer Type Callback
@app.callback(
    Output('main-graph-city-total', 'figure'),
    Input('selected_city_total', 'value')
)
def update_customer_chart(city):
    fig = px.scatter(df[df['City'] == city] , x="Month" , y='Total', color='Customer type',  title=f'Total Penjualan dari setiap Member atau Non Member Customer perbulan di cabang {city}')
    return fig

# Gross Income per Customer Type Callback
@app.callback(
    Output('main-graph-city-gross', 'figure'),
    Input('selected_city_gross', 'value')
)
def update_city_gross_chart(city):
    fig = px.scatter(df[df['City'] == city] , x='Month' , y='gross income', color='Customer type',  title=f'Gross Income dari setiap Member atau Non Member Customer perbulan di cabang {city}')
    return fig

# Product Line Visualization Callback
@app.callback(
    Output('main-graph-product', 'figure'),
    Input('selected_product', 'value')
)
def update_product_chart(city):
    fig = px.bar(df[df['City'] == city], x="Product line", y="gross income", color='Customer type', barmode="group", title=f'Gross Income dari setiap pembelian jenis product yang dilakukan oleh Member atau Non Member di cabang {city}')
    return fig
