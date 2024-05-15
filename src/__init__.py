from flask import Flask 
from flask_cors import CORS 
from flask_jwt_extended import JWTManager
from mongoengine import connect
from src.user_blueprint import user
from src.customer_blueprint import customer
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "super secret and difficult to guess key"

mongodb_uri = os.getenv("MONGODB_URI")
mongodb_db = os.getenv("MONGODB_DB")
connect(
    host= mongodb_uri,
    db= mongodb_db,
    alias="coding-factory",
)

cors = CORS(
    app,
    resources={r"*": {"origins": ["http://localhost:4200"]}},
)

app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(customer, url_prefix="/customer")
