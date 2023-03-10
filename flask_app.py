from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap5
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            server_email = os.getenv('EMAIL')
            server_pass = os.getenv('PASSWORD')
            admin_email = os.getenv('ADMIN_EMAIL')
            connection.login(server_email, server_pass)
            connection.sendmail(from_addr=server_email,
                                to_addrs=admin_email,
                                msg="Subject: New Message From ElevAds\n\n"
                                    f"Name: {data.get('name')}\n"
                                    f"Email: {data.get('email')}\n"
                                    f"Subject: {data.get('subject')}\n"
                                    f"Message: {data.get('message')}\n")
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
