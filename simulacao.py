import dash_table_experiments as dt
import pandas as pd
from sklearn import datasets

df_compras_acima_do_limite = pd.read_csv(
    'Z:/Victor/projeto_aprovacao_venda/notebooks/experimentos_modelos_tunados/compras_acima_do_limite_model_input.csv',
    nrows = 1000
)
df_compras_acima_do_limite = df_compras_acima_do_limite.to_dict('records')
colunas_df_compras_acima_do_limite = ['entrada_perc', 'entrada_vlr', 'parcela_qtd', 'parcela_vlr', 'total_financiado_vlr', 'total_compra_vlr', 'target']

iris = datasets.load_iris()
colunas_df_iris = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
df_iris = pd.DataFrame(data=iris.data, columns=colunas_df_iris).to_dict('records')

def render_datatable(data, colunas, id):
    datatable = dt.DataTable(
        id=id,
        rows=data,
        columns = colunas,
        enable_drag_and_drop=False,
        editable = False,
        filterable=True,
        sortable=True,
        max_rows_in_viewport=5,
        selected_row_indices=[],
        row_selectable=True
    )

    return datatable
