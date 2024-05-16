from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources import Pulse



app = Flask(__name__)
CORS(app)
api = Api(app)



api.add_resource(Pulse, '/api/pulse')


if __name__ == '__main__':
    app.run(debug=True)