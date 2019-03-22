from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import subprocess
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class FileCheck(Resource):
    def get(self):
        json_data = request.get_json(force=True)
        filename = json_data['file']
        process = subprocess.Popen(['cat', filename], stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        print(stdout.decode())
        return json.dumps({'content' : stdout.decode()})

api.add_resource(HelloWorld, '/')
api.add_resource(FileCheck, '/file')



if __name__ == '__main__':
    app.run(debug=True)