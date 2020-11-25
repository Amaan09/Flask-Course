import re
import bcrypt
import smtplib
import random
import math
import simplejson as json

gmail_user = 'aquaclan1508@gmail.com'
gmail_pwd = 'Faisal2350'
to = None
user_email = None
user_password = None

print("Enter 1 for Signup and 2 for Login!")

selection = input()

if selection == '1':
    print("Enter a email:")
    while True:
        print("Please enter your gmail Id:")
        email = input()
        to = email
        if re.fullmatch(r'^[a-z0-9]+\.?[a-z0-9]+@gmail\.com$', email):
            print("Good your gmail is valid")
            user_email = email
            break
        else:
            print("Choose a valid gmail Id")
    while True:
        print("Please enter a strong password:")
        password = input()
        if re.fullmatch(r'^[A-Za-z0-9@#$%^&+=]{8,}$', password):
            
            print("Great you chose a strong password!")
            
            password = password.encode('utf-8')
            password = bcrypt.hashpw(password, bcrypt.gensalt())
            user_password = password

            gen_otp = str(math.floor(random.random() * 1000000))
            
            smtpserver = smtplib.SMTP("smtp.gmail.com",587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo
            smtpserver.login(gmail_user, gmail_pwd)
            header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
            msg = header + '\n this is test msg from Amaan.com \n\n' + gen_otp
            smtpserver.sendmail(gmail_user, to, msg)
            smtpserver.close()

            print('Please enter the OTP sent to your email Id: ' + to)

            while True:
                enter_otp = input()
                if gen_otp == enter_otp:
                    print('Awesome!! You have created your account.')
                    # store in a file
                    user_details = {
                        "email": user_email,
                        "password": user_password
                    }
                    json_object = json.dumps(user_details)
                    with open('user-data.json') as json_file:
                        data = json.load(json_file)
                        temp = data['user_data']
                        temp.append(json_object)
                    
                    with open('user-data.json','w') as f:
                        json.dump(data, f,indent=4)
                    break
                else:
                    print('Please check the otp you have entered')
            break
        else:
            print("Not a valid password")
    
else:
    user_list = []
    f = open('user-data.json',) 
    data = json.load(f) 
    for user in data['user_data']:
        d = json.loads(user)
        user_list.append(d)
    f.close() 
    print("Enter Email to login:")
    login_email = input()
    print("Enter Password to login:")
    login_password = input()
    login_password = login_password.encode('utf-8')
    flag = 0
    for u in user_list:
        if login_email == u['email'] and bcrypt.checkpw(login_password, u['password'].encode('utf-8')):
            flag = 1
            print('Congratulations you have successfully loggedIn!!')

    if flag == 0:
        print('Your username or password is incorrect')