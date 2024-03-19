# A simple contact application with flask

Features:
- Database itegration
- Mails send to admin

Create your google app password
[https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

Install the requirements
```bash
pip install -r requirements.txt
```
OR
```bash
pip3 install -r requirements.txt
```
OR
(For Linux distributions & macOS)
```bash
sudo pip install -r requirements.txt
```

Add the following to .env file
```js
EMAIL_ADDRESS=""
EMAIL_APP_PASSWORD=""
```

Add your email to app.py (line no 45)
```python
msg = Message(subject=f'New contact message from {fname} {lname}', sender=os.getenv('EMAIL_ADDRESS'), recipients=['your_recipient_email'])
```
