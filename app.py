from flask import Flask, request, jsonify
from passlib.hash import bcrypt
import re

app = Flask(__name__)

# Function to evaluate password strength
def evaluate_password_strength(password):
    length_criteria = len(password) >= 12
    digit_criteria = re.search(r'\d', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&#]', password) is not None

    criteria = [length_criteria, digit_criteria, uppercase_criteria, lowercase_criteria, special_char_criteria]
    score = sum(criteria)

    return {
        "length_criteria": length_criteria,
        "digit_criteria": digit_criteria,
        "uppercase_criteria": uppercase_criteria,
        "lowercase_criteria": lowercase_criteria,
        "special_char_criteria": special_char_criteria,
        "score": score,
        "strength": "Weak" if score < 3 else "Moderate" if score < 5 else "Strong"
    }

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    password = data.get('password')
    result = evaluate_password_strength(password)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
