from flask import Flask
from api.http_api import bp
from core.settings import get_settings

settings = get_settings()
app = Flask(__name__)

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)