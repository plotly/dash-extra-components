import dash
import dash_html_components as html
import dash_extra_components as extra

from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.Div(id='page-content'),
    extra.Pager(
        id='pager',
        current_page=1,
        total_items=8,
        items_per_page=1,
    )
])


@app.callback(Output('page-content', 'children'),
              [Input('pager', 'current_page')])
def on_page(current_page):
    return 'You are on page {}'.format(current_page)


if __name__ == '__main__':
    app.run_server(debug=True, port=22500, threaded=True)
