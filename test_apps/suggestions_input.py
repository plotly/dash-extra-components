import dash

import dash_html_components as html
import dash_extra_components as extra

from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)
app.scripts.config.serve_locally = True

suggestion_list = [
    'one',
    'two',
    'three',
    'five',
]

callback_suggestions = [
    'callback',
    'react',
    'dash'
]


app.layout = html.Div([
    extra.SuggestionsInput(
        id='suggestions',
        suggestions=[
            {
                'trigger': '$',
                'options': [
                    {
                        'value': 'Rambo',
                        'description': 'Bob description'
                    },
                    {
                        'value': 'Terminator',
                        'description': 'Arnold description'
                    }
                ],
            },
            {
                'trigger': '@',
                'options': []
            }
        ],
        multi_line=True,
        # Style for the component single suggestions.
        suggestion_style={'padding': '0.5rem'},
        # Style for when a suggestion is selected.
        suggestion_selected_style={'backgroundColor': 'green', 'color': 'white'},
        # Style for the modal list of suggestions.
        suggestions_style={
            'backgroundColor': '#dcdcdc',
            'border': 'solid black 1px',
        },
        include_trigger=False
    ),
    html.Br(),
    html.Div(id='capture-output'),
    html.Div(id='suggestions-output'),
])


# Callback powered suggestions
@app.callback(Output('suggestions', 'filtered_options'),
              [Input('suggestions', 'captured')],
              [State('suggestions', 'current_trigger')])
def on_captured(captured, current_trigger):
    if captured is None or current_trigger != '@':
        raise PreventUpdate

    return [{'value': x} for x in callback_suggestions if captured in x]


@app.callback(Output('capture-output', 'children'), [Input('suggestions', 'captured')])
def on_capture(captured):
    if captured is None:
        raise PreventUpdate

    return captured


for output in (
        'suggestions-output',
):
    @app.callback(Output(output, 'children'),
                  [Input(output.replace('-output', ''), 'value')])
    def on_output(value):
        if value is None:
            raise PreventUpdate

        return value


if __name__ == '__main__':
    app.run_server(port=10960, threaded=True, debug=True)
