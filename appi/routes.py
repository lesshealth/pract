# app/routes.py
from flask import Blueprint, request, jsonify, render_template
from models import db, User

api = Blueprint('api', __name__)

# Роут для главной страницы (форма регистрации)
@api.route('/')
def home():
    return render_template('index.html')

# Роут для регистрации пользователя
@api.route('/api/register', methods=['POST'])
def register_user():
    data = request.get_json()

    # Валидация данных
    if not data.get('name'):
        return jsonify({"error": "Поле 'Имя' обязательно для заполнения"}), 400
    if not data.get('email'):
        return jsonify({"error": "Поле 'Email' обязательно для заполнения"}), 400
    if not data.get('password') or len(data['password']) < 8:
        return jsonify({"error": "Пароль должен содержать минимум 8 символов"}), 400

    # Проверка на существование email
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email уже зарегистрирован"}), 400

    # Создание пользователя и сохранение в БД
    user = User(name=data['name'], email=data['email'])
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Пользователь успешно зарегистрирован"}), 200

def register_routes(app):
    app.register_blueprint(api)
