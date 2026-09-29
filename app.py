from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>My Azure App</title>
        </head>
        <body>
            <h1>Hello from Azure App Service!</h1>
            <p>This is my first Python web application deployed to Azure.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
