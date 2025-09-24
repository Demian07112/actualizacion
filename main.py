from flask import Flask
from routes.pet_routes import set_pet_routes

app = Flask(__name__)

set_pet_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
