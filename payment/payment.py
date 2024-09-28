from flask import Flask
app = Flask(__name__)

@app.route('/payments')
def payments():
    return "Welcome to the Payment Service!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

