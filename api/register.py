from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulating a user database
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Please provide both email and password'}), 400

    if email in users:
        return jsonify({'message': 'User already exists'}), 409

    users[email] = password
    return jsonify({'message': 'Registration successful'}), 201

if __name__ == '__main__':
    app.run(debug=True)
