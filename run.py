from flask import Flask, request
from flask_restx import Resource, Api
from flask_cors import CORS
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'localhost',  # Replace with your MongoDB host
    'port': 27017,  # Default MongoDB port
    'db': 'HMS',  # Replace with your database name
    # 'username': 'your_username',  # If authentication is required
    # 'password': 'your_password'  # If authentication is required
}

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mongodb://localhost:27017/HMS'

api = Api(app, version='1.0', title='HMC API',
    description='Backend APIs for HMC management',)

cors = CORS()

cors.init_app(app)

db=MongoEngine()
db.init_app(app)

from run import app, api
from controllers.owner import owner_ns

api.add_namespace(owner_ns, "/")

# print("Database URL:", app.config['SQLALCHEMY_DATABASE_URI'])

if __name__ == '__main__':
    app.run(debug=True, port=5010)
