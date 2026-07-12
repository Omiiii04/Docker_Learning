from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# 1. Basic Home Route
@app.route("/")
def home():
    return "<h1>Welcome to Flask!</h1><p>The basic web application is running.</p>"

# 2. Dynamic Route with URL Parameters
@app.route("/user/<name>")
def greet_user(name):
    # Capitalize the name for display
    return f"Hello, {name.capitalize()}! Welcome to your dashboard."

# 3. JSON API Endpoint
@app.route("/api/status")
def api_status():
    return jsonify({
        "status": "success",
        "message": "The Flask API is up and running!",
        "version": "1.0"
    })

if __name__ == "__main__":
    # Run the built-in development server
    # debug=True automatically reloads the server when code changes
    app.run(host="0.0.0.0", port = 5000, debug = True)