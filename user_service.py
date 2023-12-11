# user_service.py
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo  # Example: MongoDB for simplicity

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/social_media'
mongo = PyMongo(app)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user = {
        'username': data['username'],
        'password': data['password'],
        # Other user details...
    }
    mongo.db.users.insert_one(user)
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    # Implement user authentication logic using JWT...
    return jsonify({'message': 'User logged in successfully'}), 200

if __name__ == '__main__':
    app.run(port=5001)
