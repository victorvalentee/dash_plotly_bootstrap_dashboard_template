# -*- coding: utf-8 -*-
import dash
import dash_html_components as dhtml
import dash_table_experiments as dt
import simulacao

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
                        "Simulação"
                    ], href="#", className="nav-link active")
                ], className="nav-item"),
                dhtml.Li([
                    dhtml.A([
                        "Relatório"
                    ], href="#", className="nav-link")
                ], className="nav-item")
            ], className="nav flex-column")
        ], className="sidebar-sticky")
    ], className='col-md-2 d-none d-md-block bg-light sidebar'),

    dhtml.Main([            # MAIN (TODO: VAI SER RELATIVA AO CLIQUE NOS BOTÕES DO MENU LATERAL.)
        dhtml.Div([
            dhtml.H2("Simulação", className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom"),
            dhtml.Div([
                simulacao.render_datatable(simulacao.df_iris, simulacao.colunas_df_iris, 'df_iris'),
            ])
    ], role="main", className="col-md-9 ml-sm-auto col-lg-10 px-4")]),

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