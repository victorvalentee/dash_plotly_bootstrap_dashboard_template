import dash_table_experiments as dt
import pandas as pd

df_compras_acima_do_limite = pd.read_csv(
    'Z:/Victor/projeto_aprovacao_venda/notebooks/experimentos_modelos_tunados/compras_acima_do_limite_model_input.csv',
    nrows = 1000
)

def render_datatable():
    datatable = dt.DataTable(
        rows=df_compras_acima_do_limite.to_dict('records'),
        columns = ['entrada_perc', 'entrada_vlr', 'parcela_qtd', 'parcela_vlr', 'total_financiado_vlr', 'total_compra_vlr', 'target'],
        enable_drag_and_drop=False,
        editable = False,
        filterable=True,
        sortable=True,
        max_rows_in_viewport=5,
        id='df_compras_acima_do_limite',

        selected_row_indices=[],
        row_selectable=True
    )

    return datatable
