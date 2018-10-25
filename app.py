# -*- coding: utf-8 -*-
import dash
import dash_html_components as dhtml
import dash_table_experiments as dt
import simulacao
from dash.dependencies import Input, Output

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
            dhtml.H2("Simulação de Compra Acima do Limite", className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom"),
            dhtml.Div([
                dt.DataTable(
                    rows=simulacao.df_compras_acima_do_limite.to_dict('records'),
                    columns=['entrada_perc', 'entrada_vlr', 'parcela_qtd', 'parcela_vlr', 'total_financiado_vlr', 'total_compra_vlr', 'target'],
                    enable_drag_and_drop=False,
                    editable=False,
                    filterable=True,
                    sortable=True,
                    max_rows_in_viewport=5,
                    id='df_compras_acima_do_limite',
                    selected_row_indices=[],
                    row_selectable=True
                )
            ]),
            dhtml.Div([
                dt.DataTable(
                    rows=[{}],
                    columns = ['entrada_perc', 'entrada_vlr', 'parcela_qtd', 'parcela_vlr', 'total_financiado_vlr', 'total_compra_vlr', 'target'],
                    enable_drag_and_drop=False,
                    editable = False,
                    filterable=True,
                    sortable=True,
                    max_rows_in_viewport=5,
                    id='datatable'
                ),
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

@app.callback(
    Output('datatable', 'rows'),
    [Input('df_compras_acima_do_limite', 'selected_row_indices')]
)
def update_datatable(user_selection_indices):
    try:
        print(user_selection_indices)
        last_selected_index = [user_selection_indices[0]]
        rows = simulacao.df_compras_acima_do_limite.iloc[last_selected_index].to_dict('records')
        return rows
    except:
        return []

if __name__ == '__main__':
    app.run_server(debug=True)