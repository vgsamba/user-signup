from flask import Flask, request, redirect,render_template
import cgi
import os
import jinja2
import re

template_dir=os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template= jinja_env.get_template('home_page.html')
    return template.render()
def validate(fieldname, fieldval, fieldlen):
    msg=''
    if (not fieldval) or (fieldval.strip() == "") or (" " in fieldval) or (fieldlen < 3) or (fieldlen > 20):
        msg = "Please enter a valid "+fieldname
    return msg

def validateemail(Email_Id, email_id_length):
    msg=''
    pattern = re.compile("^\w+[@]{1}\w+[.]{1}\w+$")
    if (email_id_length>0) and ((" " in Email_Id) or ("@" not in Email_Id) or ("." not in Email_Id) or (email_id_length < 3) or (email_id_length > 20) or not pattern.match(Email_Id)):
        msg = "Please enter a valid email_id."
    return msg


@app.route("/home", methods=['POST'])  #request handler for home page
def welcome():
    user_name = request.form['User_Name']
    Password =request.form['Password']
    Confirm_Password=request.form['Confirm_Password']
    Email_Id=request.form['Email_Id']
    email_id_length = len(Email_Id)

    User_Name_length=len(user_name)
    Password_length=len(Password)
    Confirm_Password_length=len(Confirm_Password)
    username_error = validate("user name",user_name,User_Name_length)
    password_error=validate("password",Password,Password_length)
    confirmpassword_error=''
    emailId_error=validateemail(Email_Id,email_id_length)
    passwordmatch_error=''

    #if (not user_name) or (user_name.strip() == "") or (" " in user_name):
        #username_error = "Please enter a valid user name."
    #if (not Password) or (Password.strip() == "") or (" " in Password):
       # password_error = "Please enter a valid Password."
    #if (not (Password == Confirm_Password) and (confirmpassword_error== "")):
    #if Confirm_Password.strip() == "":
       # Confirm_Password = "Please enter a valid Confirm_Password."
    if not Password == Confirm_Password or Confirm_Password.strip() == "" :
        confirmpassword_error = "Passwords do not match"
    # if (email_id_length>0) and ((" " in Email_Id) or ("@" not in Email_Id) or ("." not in Email_Id) or (email_id_length < 3) or (email_id_length > 20)):
    #     emailId_error = "Please enter a valid email_id."
    #
    # pattern = re.compile("^\w+[@]{1}\w+[.]{1}\w+$")
    # if (email_id_length>0) and not pattern.match(Email_Id):
    #         emailId_error = "Please enter a valid email_id."
    #if (User_Name_length < 3) or (User_Name_length > 20):
     #   username_error =" Not a valid user name"
    #if (Password_length < 3) or (Password_length > 20):
     #   password_error =" Not a valid password"

    if not username_error and not password_error and not confirmpassword_error and not passwordmatch_error and not emailId_error:
        return render_template('welcome_page.html', name=user_name)
    else:
        template=jinja_env.get_template('home_page.html')
        return template.render(username=user_name,
                               emailId=Email_Id,
                               username_error=username_error,
                               password_error=password_error,
                               confirmpassword_error=confirmpassword_error,
                               passwordmatch_error=passwordmatch_error,
                               emailId_error=emailId_error
                            )
app.run()