from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class Hi(Resource):
    def get(self):
        hi="Hi "+request.args['nombre']        
        return {'Hi': hi}

api.add_resource(Hi, '/Hi')

class Bye(Resource):
    def get(self):
        bye="Bye "+request.args['nombre']        
        return {'Bye': bye}

api.add_resource(Bye, '/Bye')

if __name__ == '__main__':
    app.run(debug=False)
