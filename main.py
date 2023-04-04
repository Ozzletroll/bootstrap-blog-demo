from flask import Flask, render_template, request
import requests
import smtplib


app = Flask(__name__)
endpoint = "https://api.npoint.io/414d1d783ea5d91e3740"
response = requests.get(endpoint).json()


@app.route('/')
def home(blog_json=response):
    return render_template("index.html", blog_data=blog_json)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/<post_title>')
def post(post_title, blog_json=response):

    def get_post_data(blog_json, post_title):
        post_result = []
        for entry in blog_json:
            if post_title in entry.values():
                post_result.append(entry)
        return post_result[0]

    blog_entry = get_post_data(blog_json, post_title)

    return render_template("post.html", post=blog_entry)


@app.route('/form_entry', methods=["POST"])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone_number = request.form["phone_number"]
    message = request.form["message"]

    from_email = email
    to_email = "EXAMPLE_EMAIL_ADDRESS"
    app_password = "SMTPLIB_APP_PASSWORD"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email, password=app_password)
        connection.sendmail(
            from_addr=from_email, to_addrs=to_email,
            msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone_number}\nMessage: {message}"
        )

    return render_template("contact.html", message_status=True)


if __name__ == "__main__":
    app.run(debug=True)
