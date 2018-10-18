import dash_html_components as dhtml
import pandas as pd


def generate_table(dataframe, max_rows = 10):
    return dhtml.Table(
        # Header
        [dhtml.Tr([dhtml.Th(col) for col in dataframe.columns])] +

        # Body
        [dhtml.Tr([
            dhtml.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

def show_dataset(dataset_name):
    df = pd.read_csv('Z:/Victor/projeto_aprovacao_venda/notebooks/experimentos_modelos_tunados/compras_acima_do_limite_model_input.csv')

    # TODO: show columns of interest and default contracts only.
    df = df[df['target'] == 0]
    df = df[['entrada_perc', 'parcela_qtd', 'target']]

    return generate_table(df)

