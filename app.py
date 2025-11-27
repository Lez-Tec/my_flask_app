from flask import Flask
from controllers import home_controller, users_controller

app = Flask(__name__)

# Routes
app.add_url_rule("/", "home", home_controller)
app.add_url_rule("/users", "users", users_controller)

if __name__ == "__main__":
    app.run(debug=True)
