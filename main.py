from flask import Flask, request, render_template, redirect
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route ("/")
def index():
    return render_template('base.html')


@app.route ("/validate", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']    
    validatepassword = request.form['validatepassword']
    email = request.form['email']
    email_error = ""
    pwdval_error = ""
    pwd_error = ""
    username_error = ""

    if len(username) < 3 or len(username) > 20 or " " in username:
       username_error = 'Not a valid username'


    if len(password) <3 or len(password) >20 or " " in password:
        pwd_error = 'Please enter a password between 3 and 20 characters.'

    if validatepassword is "":
        pwdval_error = "Enter a valid password."
    
    elif validatepassword != password:
        pwdval_error = 'Passwords do not match.'

    if email != "" and len(email) < 3 or len(email) > 20:
        email_error = 'Not a valid email'

    elif email !="" and ('.' and '@') not in email:
        email_error = "Not a valid email."
 

    if not username_error and not pwd_error and not pwdval_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('base.html', username=username, email=email, username_error=username_error, pwd_error=pwd_error, 
        pwdval_error=pwdval_error, email_error=email_error)

if __name__ == "__main__":
    app.run()