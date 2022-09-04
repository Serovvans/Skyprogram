from flask import Flask
from blueprint_posts.views import posts_blueprint
from blueprint_api.api import api_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)


if __name__ == "__main__":
    app.run()
