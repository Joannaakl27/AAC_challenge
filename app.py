import pandas as pd

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import utils

app = dash.Dash(
    __name__, suppress_callback_exceptions = True,
    use_pages=True, external_stylesheets=[dbc.themes.LITERA],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1", 'charSet':'“UTF-8”'}])

server = app.server
app.title = "AAC Dashboard"

app.layout = html.Div([
    dbc.Navbar(
        dbc.Container([
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/aac.jpeg",
                                         height="50px"))
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://www.austintexas.gov/austin-animal-center",
                style={"textDecoration": "none"},
            ),
            html.P('AAC Data Explorer', style = {'margin-left': '-58vw', 'margin-top': '15px', 'font-weight': 'bold', 'font-size': '20px', 'font-family': 'Arial, sans serif'}),
            
            html.Div([
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Home", href="/"),
                        dbc.DropdownMenuItem("Explore", href="/explore"),
                        dbc.DropdownMenuItem("Predict", href='/predict'),
                        dbc.DropdownMenuItem("Documentation", href='https://joannaakl27.notion.site/AAC-Data-Explorer-Docs-30bff26402d340c8a55d170773c1e205?pvs=4', target = "_blank")
                    ],
                    nav=True,
                    in_navbar=True,
                    label="≡",
                    size = 'lg',
                    style = {'font-weight': 'bold', 'color': 'black', 'font-size': '35px'},
                ),
            ], ),
        ])),

    # Main content ----------------------------------------------------------
    html.Div([]),
    dash.page_container
])

merged_with_locations = utils.read_json_data('raw_data/merged_with_locations.json')
data = pd.DataFrame(merged_with_locations)

# Runs the app ------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=False, use_reloader=True)
