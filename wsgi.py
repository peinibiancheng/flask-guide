from config import create_app
from flask_restful import Api
from app import HelloWorld

app = create_app()
api = Api(app)
api.add_resource(HelloWorld,'/')
