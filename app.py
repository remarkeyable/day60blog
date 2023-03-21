from flask import Flask, render_template, request
import requests
import os
import smtplib


app = Flask(__name__)


@app.route('/')
def home():
    req = requests.get('https://api.npoint.io/906adb31c902f13769de')
    result = req.json()
    return render_template('index.html', blog=result)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post<num>')
def postt(num):
    req = requests.get('https://api.npoint.io/906adb31c902f13769de')
    result = req.json()
    return render_template('post.html', blog=result, number=int(num))


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['POST'])
def get_response():
    EMAIL = os.environ.get("EMAIL")
    PASSWORD = os.environ.get("PASSWORD")
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(f"{name} {email} {message}")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject: A Message from your Blog.\n\nName: {name}\nEmail: {email}\nMessage: {message}")
    return render_template('contact.html')



if __name__ == "__main__":
    app.run(debug=True)
