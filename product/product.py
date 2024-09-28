from flask import Flask
app = Flask(__name__)

@app.route('/products')
def products():
    return "Welcome to the Product Service!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)