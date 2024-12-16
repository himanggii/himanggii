from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/redirect')
def vulnerable_redirect():
    url = request.args.get('url')  # User controls the redirect target
    return redirect(url)  # Open redirect vulnerability

if __name__ == "__main__":
    app.run(debug=True)
