import dash
import dash_core_components as dcc
import dash_html_components as html
# from scipy.optimize import minimize, rosen, rosen_der

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)
#     x0 = [1.3, 0.7, 0.8, 1.9, 1.2]
#     for i in range(100):
#       res = minimize(rosen, x0, method='BFGS', jac=rosen_der,
#                      options={'gtol': 1e-6, 'disp': True})
#       print(f"{res.x}")
