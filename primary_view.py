# -*- coding: utf-8 -*-
# import dash_table_experiments as dt
import dash_html_components as dhtml
import dash_core_components as dcc
import pandas as pd


DF_SIMPLE = pd.DataFrame({
    'x': ['A', 'B', 'C', 'D', 'E', 'F'],
    'y': [4, 3, 1, 2, 3, 6],
    'z': ['a', 'b', 'c', 'a', 'b', 'c']
})

def render():
    return dhtml.Div([
        dcc.Tabs(id="tabs", value='tab-1', children=[
            dcc.Tab(label='Simulacao', value='tab-simulation'),
            dcc.Tab(label='Relatorio - Model Explorer', value='tab-report'),
        ]),
        dhtml.Div(id='tabs-content')
])

'''
        dhtml.Div([
        dhtml.H4('Table'),
        dt.DataTable(
            rows=DF_SIMPLE.to_dict('records'),

            # optional - sets the order of columns
            columns=sorted(DF_SIMPLE.columns),

            row_selectable=True,
            filterable=True,
            sortable=True,
            selected_row_indices=[],
            id='datatable-gapminder'
        )
    ], className="container")
'''