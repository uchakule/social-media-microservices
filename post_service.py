# post_service.py
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo  # Example: MongoDB for simplicity

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/social_media'
mongo = PyMongo(app)

@app.route('/create_post', methods=['POST'])
def create_post():
    data = request.get_json()
    post = {
        'user_id': data['user_id'],
        'content': data['content'],
        # Other post details...
    }
    mongo.db.posts.insert_one(post)
    return jsonify({'message': 'Post created successfully'}), 201

@app.route('/get_posts', methods=['GET'])
def get_posts():
    # Implement logic to retrieve posts...
    posts = mongo.db.posts.find()
    return jsonify(posts)

if __name__ == '__main__':
    app.run(port=5002)
