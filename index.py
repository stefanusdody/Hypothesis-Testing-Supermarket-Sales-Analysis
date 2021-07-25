import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
from app import server

from apps import hypothesis, visualization

app.layout = html.Div([
  dbc.NavbarSimple(

      dbc.Row([
          dbc.Col(
              children=[
                    dbc.NavItem(dbc.NavLink("My GitHub", href="https://github.com/stefanusdody")),
              ],
          ),

          dbc.Col(
              children=[
                    dbc.NavItem(dbc.NavLink("Hypothesis", href='/apps/hypothesis')),
              ],
          ),

          dbc.Col(
              children=[
                    dbc.NavItem(dbc.NavLink("Visualization", href='/apps/visualization')),
              ],
          ),
      ]),
      brand="Supermarket Analysis",
      brand_href="/apps/hypothesis",
      color="dark",
      dark=True,
      sticky='top'
  ),
  dcc.Location(id='url', refresh=False),
  html.Div(id='page-content', children=[])
])


# add callback for toggling the collapse on small screens
@app.callback(
    Output(component_id='page-content', component_property='children'),
    [Input(component_id='url', component_property='pathname')]
)
def display_page(pathname):
    if pathname == '/apps/visualization':
        return visualization.layout
    else:
        return hypothesis.layout

if __name__ == '__main__':
    app.run_server(debug=True)
