import time
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_extra_components as dec
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='notification-text'),
    html.Button('Send notification', id='send-btn'),
    html.Div([
        dec.Notification(
            id='notification',
            title='dummy',
            key=str(time.time())
        )
    ], id='notification-output'),
    html.Div(id='permission')
])


@app.callback(Output('notification-output', 'children'),
              [Input('send-btn', 'n_clicks')],
              [State('notification-text', 'value')])
def on_click(n_clicks, text):
    if n_clicks is None:
        raise PreventUpdate

    return dec.Notification(
        id='notification',
        title='Notification',
        displayed=True,
        body=text,
        key=str(time.time())
    )


@app.callback(Output('permission', 'children'),
              [Input('notification', 'permission')])
def on_permission(perm):
    if perm is None:
        raise PreventUpdate

    return perm


if __name__ == '__main__':
    app.run_server(port=6061, debug=True)
