from flask import Flask, request, jsonify

app = Flask(__name__)

# Track logged-in users
logged_in_users = set()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Please provide both email and password'}), 400

    # Authenticate the user against a user database
    if authenticate_user(email, password):
        logged_in_users.add(email)
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid email or password'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'message': 'Please provide an email'}), 400

    if email in logged_in_users:
        logged_in_users.remove(email)
        return jsonify({'message': 'Logout successful'}), 200
    else:
        return jsonify({'message': 'User is not logged in'}), 401

def authenticate_user(email, password):
    # Simulating user authentication against a user database
    users = {
        "john@example.com": "password123",
        "jane@example.com": "password456"
    }
    if email in users and users[email] == password:
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)
