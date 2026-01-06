from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    app.logger.info("Application accessed successfully!")
    return "Hello from Zahir's Azure CI/CD Project!"

if __name__ == "__main__":
    app.run()
