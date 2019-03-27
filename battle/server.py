from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import subprocess
import hashlib

app = Flask(__name__)
api = Api(app)

seed = 'hashseed'


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class FileCheck(Resource):
    def get(self):
        json_data = request.get_json(force=True)
        filename = json_data['file']
        process = subprocess.Popen(['cat ' + filename], stdout=subprocess.PIPE, shell=True)
        stdout, _ = process.communicate()
        print(stdout.decode())
        return jsonify({'content' : stdout.decode()})

    def post(self):
        json_data = request.get_json(force=True)
        filename = json_data['file']
        content = seed + filename
        with open(filename, 'w') as f:
            f.write(str(hashlib.sha224(content.encode()).hexdigest()))

class Secrets(Resource):

    secrets_files = []

    def get(self):
        json_data = request.get_json(force=True)
        id = json_data['id']
        print(id)
        print(self.secrets_files)
        if id <= 4:
            secret_filename = self.secrets_files[id]
            print(secret_filename)
            process = subprocess.Popen(['cat ' + secret_filename], stdout=subprocess.PIPE, shell=True)
            stdout, _ = process.communicate()
            print(stdout.decode())
            return jsonify({'content' : stdout.decode()})
        else:
            return jsonify({'error' : 'No Access'})

    def post(self):
        json_data = request.get_json(force=True)
        id = json_data['id']
        secret_filename = 'secrets/secret{}'.format(id)
        content = seed + secret_filename
        with open(secret_filename, 'w') as f:
            f.write(str(hashlib.sha224(content.encode()).hexdigest()))

        self.secrets_files.append(secret_filename)
        self.secrets_files.sort()



api.add_resource(HelloWorld, '/hello')
api.add_resource(FileCheck, '/file')
api.add_resource(Secrets, '/secrets')


if __name__ == '__main__':
    app.run(debug=False)