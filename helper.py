def is_empty(field):
    fieldlen=len(field)
    if field==" ":
        return False
    if (fieldlen<3) or (fieldlen>=20):
        return False
    else:
        True

     or
    try:
        field=" "
        return True
    except ValueError:
        return False

def some(User_Name,Password):
    if is_empty(User_Name):
        print("enter valid value")
    else:
        print("good job")
    """User_Name_length=len(User_Name)
    Password_length=len(Password)
    print(Password_length)
    print(User_Name_length)
    if (User_Name_length < 3) or (User_Name_length >= 20):
        username_error =" Not a valid user name"
        print(username_error)"""

some("c","a")

@app.route("/validate", methods="POST")
def validate():
    # look inside the request to figure out what the user typed

    User_Name=request.form['User_Name']
    Password =request.form['Password']
    Confirm_Password=request.form['Confirm_Password']
    Emaid_Id=request.form['Emaid_Id']

    username_error =''
    password_error=''
    confirmpassword_error=''
    emailId_error=''

    User_Name_length=len(User_Name)
    Password_length=len(Password)
    print(Password_length)
    if User_Name_length <3 and User_Name_length >=20:
        username_error = 'Not a valid integer'


    # if the user typed nothing at all, redirect and tell them the error
    if (not User_Name) or (User_Name.strip() == ""):
        username_error = "Please enter valid input."
        #return redirect("/?error=" + error)

        #   return redirect("/?error=" + error)

    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    new_movie_escaped = cgi.escape(user_name, quote=True)

    return render_template('welcome.html', name=user_name)