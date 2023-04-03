from flask import Flask, render_template
import requests


app = Flask(__name__)
endpoint = "https://api.npoint.io/414d1d783ea5d91e3740"
response = requests.get(endpoint).json()


@app.route('/')
def home(blog_json):
    return render_template("index.html", blog_data=blog_json)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
