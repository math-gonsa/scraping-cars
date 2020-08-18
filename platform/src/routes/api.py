from flask import Blueprint, jsonify, request

from ..services import mongo

api = Blueprint('api', __name__, url_prefix="/api")

@api.route('/', methods=["GET"])
def hello_api():
    return "Hello API."

@api.route('/ads/brands', methods=['GET'])
def get_brands():
    brands = mongo.list_brands()
    return jsonify(brands)

@api.route('/ads/counts', methods=['GET'])
def get_counts():
    data = request.json if request.json else {}
    brands = mongo.counts(data)
    return jsonify(brands)