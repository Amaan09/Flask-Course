from flask import Flask, request, render_template, redirect, url_for
import simplejson as json
import re
import math
import random
import smtplib
import bcrypt

app = Flask(__name__)

gen_otp = None
new_user = None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if valid_login(email, password):
            return redirect(url_for('success'))
        else:
            error = 'Invalid username/password'            

    return render_template('login.html', error = error)

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    global gen_otp
    global new_user
    email_error = None
    password_error = None
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        new_user = {
            'first_name' : first_name,
            'last_name'  : last_name,
            'email'     : email,
            'password'  : password,
        }
        if re.match(r'^[a-z0-9]+\.?[a-z0-9]+@gmail\.com$', email) == None:
            email_error = 'Please choose a valid email' 
        if re.match(r'^[A-Za-z0-9@#$%^&+=]{8,}$', password) == None:
            password_error = 'Please choose a valid password'
        if email_error == None and password_error == None:
            gen_otp = str(math.floor(random.random() * 1000000))
            send_otp(gen_otp, email, 'aquaclan1508@gmail.com')
            return redirect(url_for('otp'))
    return render_template('signup.html', email_error = email_error, password_error = password_error)

@app.route('/otp', methods = ['GET', 'POST'])
def otp():
    global gen_otp
    global new_user
    if request.method == 'POST':
        entered_otp = request.form['otp']
        if entered_otp == gen_otp:
            save_user(new_user)
            return redirect(url_for('success'))
        else:
            return redirect(url_for('failure'))
    return render_template('otp.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/failure')
def failure():
    return render_template('failure.html')

def valid_login(email, password):
    user_list = []
    f = open('user-data.json',) 
    data = json.load(f) 
    for user in data['user_data']:
        d = json.loads(user)
        user_list.append(d)
    f.close()
    password = password.encode('utf-8')
    for u in user_list:
        if email == u['email'] and bcrypt.checkpw(password, u['password'].encode('utf-8')):
            return True
    return False

def send_otp(otp, email, admin):
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(admin, 'Faisal2350')
    header = 'To:' + email + '\n' + 'From: ' + admin + '\n' + 'Subject:Email Confirmation \n'
    msg = header + '\n This is your highly secured OTP: \n\n' + otp
    smtpserver.sendmail(admin, email, msg)
    smtpserver.close()

def save_user(user):
    password = user['password']
    password = password.encode('utf-8')
    password = bcrypt.hashpw(password, bcrypt.gensalt())
    user['password'] = password
    json_object = json.dumps(user)
    with open('user-data.json') as json_file:
        data = json.load(json_file)
        temp = data['user_data']
        temp.append(json_object)
    
    with open('user-data.json','w') as f:
        json.dump(data, f)

app.run(port=5000, debug=True)
