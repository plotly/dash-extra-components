import json

import dash
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

import dash_extra_components as extra
import dash_html_components as html


app = dash.Dash(__name__)

total_items = 33546
items_per_pages = 5

app.layout = html.Div([
    extra.Pager(
        id='pager',
        items_per_page=items_per_pages,
        total_items=total_items,
        current_page=1,  # Still blocked by the none callbacks.
    ),

    html.Div(id='output'),
])


@app.callback(Output('output', 'children'),
              [Input('pager', 'current_page')],
              [State('pager', 'start_offset'),
               State('pager', 'end_offset'),
               State('pager', 'total_pages')])
def on_output(current_page, start_offset, end_offset, total):
    if current_page is None:
        raise PreventUpdate

    return json.dumps({
        'current_page': current_page,
        'start': start_offset,
        'end': end_offset,
        'total': total,
    }, indent=4)


if __name__ == '__main__':
    app.run_server(debug=True, port=20300)
