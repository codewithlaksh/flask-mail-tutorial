from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
from datetime import datetime
import os
import mysql.connector as mysql

load_dotenv()

app = Flask(__name__)
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = os.getenv('EMAIL_ADDRESS'),
    MAIL_PASSWORD = os.getenv('EMAIL_APP_PASSWORD')
)
mail = Mail(app)

connection = mysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='flask_crash_course'
)
cursor = connection.cursor()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=['POST'])
def send():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    timestamp = datetime.now()

    cursor.execute('INSERT INTO `contacts` (`fname`, `lname`, `email`, `phone`, `message`) VALUES ("{}", "{}", "{}", "{}", "{}")'.format(fname, lname, email, phone, message))
    connection.commit()
    connection.close()

    msg = Message(subject=f'New contact message from {fname} {lname}', sender=os.getenv('EMAIL_ADDRESS'), recipients=['your_recipient_email'])
    # msg.body = render_template('mail.html', name=name, email=email, phone=phone, message=message)
    msg.html = render_template('mail.html', name=f'{fname} {lname}', email=email, phone=phone, message=message, timestamp=timestamp)
    mail.send(msg)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=8080, host='0.0.0.0')
