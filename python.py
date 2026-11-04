
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Welcome to Cloud Computing</title>
            <style>
                body {
                    background: linear-gradient(135deg, #0078D4, #5B2C83);
                    color: white;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 150px;
                }
                h1 { font-size: 45px; }
                p { font-size: 22px; }
            </style>
        </head>
        <body>
            <h1>Welcome to Cloud Computing!</h1>
            <p>Successfully deployed using Python Flask</p>
            <p>Hosted on Microsoft Azure App Service</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
