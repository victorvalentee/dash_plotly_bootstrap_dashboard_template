# -*- coding: utf-8 -*-
import dash
from utils import *
from css import *
import primary_view

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dhtml.Div([    # BODY.
    dhtml.Div([             # HEADER.
        dhtml.Div([
            dhtml.H2('Explorer'),
            dhtml.Img(src='https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe-inverted.png')
        ], className='container scalable')
    ], className='banner'),

    dhtml.Div(              # PRIMARY VIEW.
        primary_view.render()
    ),

    dhtml.Footer([          # FOOTER.
        dhtml.P('Victor Valente'),
        dhtml.P('victorvalentee@gmail.com'),
        dhtml.P('If you like this template, buy me a coffee. BTC: XaBlAu')
    ], className='footer')
], className='body')

if __name__ == '__main__':
    app.run_server(debug=True)