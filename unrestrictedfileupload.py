from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def vulnerable_file_upload():
    file = request.files['file']
    file.save(file.filename)  # Saves the file without validation
    return "File uploaded"

if __name__ == "__main__":
    app.run(debug=True)
