from flask import Flask, request, make_response, jsonify, redirect, url_for, render_template, send_file, send_from_directory
from flask_restful import Resource, Api, reqparse
from routes.index import index_app
from routes.jadwalsholat import jadwalsholat_bp
from routes.useragent import useragent_bp
from routes.dash_login import dash_app
from routes.auth import auth_bp
from routes.dash_check import check_bp
from routes.dash_regis import regis_app
from routes.dashboard import dashboard_bp

app = Flask(__name__)
api = Api(app)
app.secret_key = 'inirahasia'

app.register_blueprint(regis_app)
app.register_blueprint(check_bp)
app.register_blueprint(index_app)
app.register_blueprint(dash_app)
app.register_blueprint(jadwalsholat_bp)
app.register_blueprint(useragent_bp)
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(debug=True)