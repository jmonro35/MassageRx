# i run this file to start the whole application

from flask import Flask
from app.routes import main

app = Flask(__name__)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
    