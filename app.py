# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Alexandru Schneider
# Created Date: 23. 11. 2021
# =============================================================================
# Dashboard App about Olympia data
# =============================================================================

# =============================================================================
# Imports
# =============================================================================
import dash
import dash_core_components as dcc
import dash_html_components as html

def main():
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    app.layout = html.Div([
        html.H2('Hello World'),
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
            value='LA'
        ),
        html.Div(id='display-value')
    ])

    @app.callback(dash.dependencies.Output('display-value', 'children'),
                  [dash.dependencies.Input('dropdown', 'value')])
    def display_value(value):
        return 'You have selected "{}"'.format(value)

    return app, app.server


app, server = main()
if __name__ == '__main__':
    app.run_server(debug=True)
