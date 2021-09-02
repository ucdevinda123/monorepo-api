from src.database import db
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from src.models.User import User
from src.models.TokenBlocklist import TokenBlocklist
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth.route('/register', methods=['POST'])
def register():
    user_name = request.json.get("username", None)
    password = request.json.get("password", None)

    if(len(user_name) < 4):
        return jsonify({'error': 'Invalid user name length'})

    if(len(password) < 6):
        return jsonify({'error': 'Invalid password length'})

    if User.query.filter_by(username=user_name).first() is not None:
        return jsonify({'error': 'Email is taken'})

    password_hash = generate_password_hash(password)
    user = User(username=user_name, password=password_hash)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'msg': 'Registration Successfully',
        'success': True,
        'code': 201
    })


@auth.route('/token', methods=['POST'])
def login():
    user_name = request.json.get("username", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(username=user_name).first()
    if user is not None:
        is_password_correct = check_password_hash(user.password, password)
        if is_password_correct:
            refresh_token = create_refresh_token(identity=user.id)
            access_token = create_access_token(identity=user.id)
            return jsonify({
                'success': True,
                'code': 200,
                'refresh_token': refresh_token,
                'access_token': access_token
            })
        else:
            return jsonify({
                'msg': 'Invalid credentials',
                'success': False,
                'code': 400
            })

    return jsonify({
        'msg': 'Invalid credentials',
        'success': False,
        'code': 401
    })


@auth.route('/token/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()
    access_token = create_access_token(identity=user_id)
    return jsonify({
        'success': True,
        'code': 200,
        'access_token': access_token
    })


@auth.route("/logout", methods=["DELETE"])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    db.session.add(TokenBlocklist(jti=jti))
    db.session.commit()
    return jsonify(msg="JWT revoked")


@auth.route('/me', methods=['GET'])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    return jsonify({
        'success': True,
        'user': {
            "id": user.id,
            "name": user.username
        },
        'code': 200
    })
