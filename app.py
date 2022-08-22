import random
from flask_restful import Resource, Api
from lib import cache, db
from config import create_app


class Person(db.Model):
    id = db.Column(db.Integer, autoincrement=True,
                   primary_key=True, nullable=False)
    name = db.Column(db.String(4), nullable=False)


app = create_app()
api = Api(app)


@app.get('/hi')
@cache.cached(5)
def hello():
    i = random.randint(1, 50)
    return {"number": f"{i}"}


def is_weekday():
    return False


class HelloWorld(Resource):
    @cache.cached(timeout=5, unless=is_weekday)
    def get(self):
        i = random.randint(1, 50)
        return {"number": f"{i}"}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    for k, v in app.config.items():
        print(f'{k}={v}')
