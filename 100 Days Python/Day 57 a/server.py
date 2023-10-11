from flask import Flask
from flask import render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    today = datetime.date.today()
    year = today.year
    return render_template("index.html", num=random_number, num2=year)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io/?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", user_name=name, user_gender=gender, user_age=age )

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/f3a193807f24dc82f951"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template("blog.html", blogs=blog_data)

if __name__ == "__main__":
    app.run(debug=True)
