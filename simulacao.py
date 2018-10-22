import dash_table_experiments as dt
import pandas as pd

DF_SIMPLE = pd.DataFrame({
    'x': ['A', 'B', 'C', 'D', 'E', 'F'],
    'y': [4, 3, 1, 2, 3, 6],
    'z': ['a', 'b', 'c', 'a', 'b', 'c']
})


def render_datatable():
    datatable = dt.DataTable(
        rows=DF_SIMPLE.to_dict('records'),

        # optional - sets the order of columns
        columns=sorted(DF_SIMPLE.columns),

        row_selectable=True,
        filterable=True,
        sortable=True,
        selected_row_indices=[],
        id='datatable-simple'
    )

    return datatable
