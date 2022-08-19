from flask import Flask
from db import db
from apps.Transactions.views import transactions


app = Flask(__name__)

# setup the config
app.config.from_object('config.DevelopmentConfig')

db.init_app(app)

# register blueprint
app.register_blueprint(transactions, url_prefix='/transactionservice')

if __name__ == "__main__":
    app.run()