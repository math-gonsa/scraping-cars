from flask import Flask
from src.routes.api import api

app = Flask(__name__)
app.register_blueprint(api)

app.config['JSON_AS_ASCII'] = False
app.secret_key = "0IwxpT03*`~In2.B"

@app.route('/')
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)