from flask import Flask, request

app = Flask(__name__)

@app.route('/xss', methods=['GET'])
def vulnerable_xss():
    user_input = request.args.get('input')  # No sanitization
    return f"<h1>{user_input}</h1>"  # Reflects user input

if __name__ == "__main__":
    app.run(debug=True)
