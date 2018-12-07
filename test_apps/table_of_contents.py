import json
from textwrap import dedent

import dash

import dash_html_components as html
import dash_core_components as dcc
import dash_extra_components as extra

from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)
app.scripts.config.serve_locally = True

app.layout = html.Div([
    extra.TableOfContents(content_selector='#content', id='toc'),
    html.Div(dcc.Markdown(dedent('''
                # level one

                content

                ## level two

                content

                ### level 2-1

                content

                ### level 2-2

                content

                ### level 2-3

                content

                ## level two-two

                ### level three

                content

                #### level four

                content

                ##### level five

                content
            ''')), id='content'),
    html.Div(id='output')
])


@app.callback(Output('output', 'children'),
              [Input('toc', 'table_of_contents')])
def on_toc(toc):
    if toc is None:
        raise PreventUpdate
    return json.dumps(toc)


if __name__ == '__main__':
    app.run_server(debug=True, port=10111, threaded=True)
