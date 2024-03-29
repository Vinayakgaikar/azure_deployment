from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def hello():
    return "<center><h1>Flask app deplyment</h1></center>"

# Run the Flask application
if __name__ == '__main__':
    app.run()
