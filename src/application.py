from flask import Flask, Response, request, redirect
import json
from products import ProductsResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__)

CORS(app)

@app.route("/")
def landing():
    return "Welcome to the first microservice"

@app.route("/products", methods=["GET"])
def get_products():
    limit = request.args.get("limit", default=5)
    offset = request.args.get("offset", default=0)

    results = ProductsResource.get_products_list(limit, offset)
    if results:
        rsp = Response(json.dumps(results), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/products/<product_id>", methods=["GET"])
def get_product_id(product_id):
    result = ProductsResource.get_products_by_id(product_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/create_product", methods=["POST"])
def create_product():
    data = request.json

    product_id = data["product_id"]
    name = data["name"]
    category = data["category"]
    price = data["price"]
    print(f"Creating product {product_id} : {name}")
    if not ProductsResource.create_product(product_id, name, category, price):
        Response("Unable to add data", status=201, content_type="text/plain")

    return redirect(f'/products/{product_id}')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)

