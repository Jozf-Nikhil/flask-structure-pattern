from flask import Flask
from app.routes.products import products_bp
from app.routes.customers import customers_bp

def create_app():
    app = Flask(__name__)

    # Product API
    app.register_blueprint(products_bp, url_prefix="/api/v1/products")

    # Customer API
    app.register_blueprint(customers_bp, url_prefix="/api/v1/customers")

    @app.route("/")
    def home():
        return {
            "message": "Flask Product API is running!"
        }
    return app