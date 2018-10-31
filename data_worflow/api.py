import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
from flask import Flask

import mapper

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout=html.Div(children=[
        html.H1(children="Arson Density", style={"textAlign": "center"}),
        dcc.Graph(id="arson", figure=mapper.create_map())
    ])

if __name__ == "__main__":
    app.run_server(debug=True)
'''

https://github.com/plotly/dash/issues/214
https://community.plot.ly/t/dash-on-multi-page-site-app-route-flask-to-dash/4582/15

import flask
from flask import Flask
from flask_cors import CORS

import mapper

app = Flask(__name__)

@app.route("/")
def root():
    density_map = mapper.create_map()
    return flask.render_template("index.html", graphJSON=density_map)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5001")
'''