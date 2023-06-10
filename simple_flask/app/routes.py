from . import models, db
from flask import current_app as app, request, jsonify


@app.route('/', methods=['GET'])
def index():
    return "Hello World!", 200


@app.route('/users', methods=['GET'])
def users():
    if request.method == "GET":
        result = []
        for user in models.User.query.all():
            result.append(user.to_dict())
        return jsonify(result), 200
    elif request.method == "POST":
        user_data = request.json

        new_user = models.User(**user_data)

        db.session.add(new_user)
        db.session.commit()

        result = []
        for user in models.User.query.all():
            result.append(user.to_dict())

        return jsonify(result), 200


@app.route('/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def user_function(uid):
    if request.method == "GET":
        user = models.User.query.get(uid)
        return jsonify(user.to_dict()), 200
    if request.method == "PUT":
        user_data = request.json
        user = models.User.query.get(uid)
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.age = user_data['age']
        user.email = user_data['email']
        user.role = user_data['role']
        user.phone = user_data['phone']

        db.session.add(user)
        db.session.commit()

        user = models.User.query.get(uid)
        return jsonify(user.to_dict()), 200

    if request.method == "DELETE":
        user = models.User.query.get(uid)
        db.session.delete(user)
        db.session.commit()

        return "", 204
