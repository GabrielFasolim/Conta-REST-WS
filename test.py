from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

contas = {
    "1": {
        "saldo": 10.0
    },
    "2": {
        "saldo": 20.0
    }
}

class getValorConta(Resource):
    def get(self, conta_id):
        if conta_id not in contas:
            return "Conta não encontrada", 404
        else:
            return contas[conta_id], 200

class Deposito(Resource):
    def post(self, conta_id):
        parser = reqparse.RequestParser()
        parser.add_argument("valor")
        args = parser.parse_args()

        if conta_id not in contas:
            return "Conta não encontrada", 404
        else:
            contas[conta_id]["saldo"] += float(args["valor"])
            return contas[conta_id], 201

api.add_resource(getValorConta, '/conta/<string:conta_id>')
api.add_resource(Deposito, '/conta/deposito/<string:conta_id>')

if __name__ == '__main__':
    app.run(debug=True)
