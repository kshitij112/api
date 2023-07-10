from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user database (replace this with your own database implementation)
users = {
    "john_doe": {
        "username": "john_doe",
        "password": "password123",
        "email": "john.doe@example.com"
    },
    "jane_smith": {
        "username": "jane_smith",
        "password": "secret456",
        "email": "jane.smith@example.com"
    }
}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid request'}), 400
    
    username = data['username']
    password = data['password']
    
    if username in users and users[username]['password'] == password:
        user = users[username]
        response = {
            'message': 'Login successful',
            'username': user['username'],
            'email': user['email']
        }
        return jsonify(response), 200
    
    return jsonify({'error': 'Invalid username or password'}), 401

if __name__ == '__main__':
    app.run()
