from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message
@app.route("/", methods=["GET"])
def homepage():
    return jsonify({"message": "Welcome to our product API!"}), 200

# TODO: Implement GET /products route that returns all products or filters by category
@app.route("/products", methods=["GET"])
def get_products():
    # TODO: Return all products or filter by ?category=, list comprehension
    category = request.args.get("category")
    if category:
        filtered = [product for product in products if product["category"].lower() == category.lower()]
        return jsonify(filtered), 200
    return jsonify(products), 200

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    # TODO: Return product by ID or 404, generator expression
    product = next((product for product in products if product["id"] == id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404
    
if __name__ == "__main__":
    app.run(debug=True)
