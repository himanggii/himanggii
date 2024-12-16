from flask import Flask, request

app = Flask(__name__)

@app.route('/read')
def vulnerable_file_read():
    filename = request.args.get('file')  # User-controlled file path
    with open(filename, 'r') as f:  # No validation of file path
        return f.read()

if __name__ == "__main__":
    app.run(debug=True)
