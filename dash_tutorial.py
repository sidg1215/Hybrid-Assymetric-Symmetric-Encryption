import dash
import dash_core_components as dcc
import dash_html_components as html
import rsa
from dash.dependencies import Input, Output

app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'color' : '#B22222'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='RSA ENCRYPTER',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Encrypts any message/file you want and can only be decrypted using the right private key', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Div(children = [html.P("Key Generator", style = {'color': colors['color'],
                                                            'textAlign': 'center'})]),
    html.Button('Button 1', id='submit-val', n_clicks=0, style = {'textAlign' : 'center'}),
    html.Div(style={'color': colors['color'], 'textAlign' : 'center'},
                id='container-button-basic',
                children='hello')
])
])

@app.callback(
    dash.dependencies.Output('container-button-basic', 'children'),
    [dash.dependencies.Input('submit-val', 'n_clicks')])
def update_output(n_clicks):
    keys = rsa.key_generator()
    return 'The keys are {}'.format(
        str(keys)
    )

if __name__ == '__main__':
    app.run_server(debug=True)