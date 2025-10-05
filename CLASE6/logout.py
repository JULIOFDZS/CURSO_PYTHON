from flask import Blueprint, request, jsonify

logout = Blueprint('logout', __name__)
@logout.route('/logout', methods=['POST'])
def login_user():
    print("Headers:",request.headers)