# -*- coding: utf-8 -*-
import dash
import dash_html_components as dhtml

external_stylesheets = ["https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dhtml.Div([    # BODY.
    dhtml.Nav([             # HEADER.
        dhtml.A([
            "Explorer"
        ], className='navbar-brand col-sm-3 col-md-2 mr-0', href="#")
    ], className='navbar navbar-dark fixed-top bg-dark flex-md-nowrap p-0'),

    dhtml.Nav([             # SIDEBAR.
        dhtml.Div([
            dhtml.Ul([
                dhtml.Li([
                    dhtml.A([
                        "Dashboard"
                        # <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-home"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    ], href="#", className="nav-link active")
                ], className="nav-item")
            ], className="nav flex-column")
        ], className="sidebar-sticky")
    ], className='col-md-2 d-none d-md-block bg-light sidebar'),

    dhtml.Footer([          # FOOTER.
        dhtml.Div([
            dhtml.P('Victor Valente'),
            dhtml.P('victorvalentee@gmail.com'),
            dhtml.P('If you like this template, buy me a coffee. BTC: XaBlAu')
        ], className="container")
    ], className='footer mt-auto fixed-bottom py-3')
], className='body')

if __name__ == '__main__':
    app.run_server(debug=True)