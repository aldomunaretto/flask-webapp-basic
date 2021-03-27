from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth',__name__)


@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 5:
            flash("Email must be greater than 4 characters", category="error")
        elif len(firstName) < 2 or len(lastName) < 2:
            flash("First & last name must be greater than 1 character", category="error")
        elif password1 != password2:
            flash("Passwords don\'t match", category="error")
        elif len(password1) < 8:
            flash("Password must be greater at least 8 characters", category="error")
        else:
            flash("ACcount created!",category="success")
            pass
            # add user to the database

    return render_template("sign_up.html")