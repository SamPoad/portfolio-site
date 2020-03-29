"""
This is the Python script to create the localized server.
"""

# dependencies
from flask import Flask, render_template

# create instance of the Flask application
app = Flask(__name__)

# create the homepage
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/aboutme/")
def about():
    return render_template('about.html')

@app.route("/myprojects/")
def projects():
    return render_template('projects.html')


# run the server
if __name__ == "__main__":
    app.run()