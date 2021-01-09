from flask.globals import current_app
from flask_login.utils import login_user, logout_user
from . import auth
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user


@auth.route('/login', methods=["GET", "POST"])
def login_screen():
    print("yes")
    if current_user.is_authenticated:
        return redirect(url_for('upload.main_screen'))
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            login_user(user)
        except Exception as err:
            current_app.logger.info("Login failed for user %s", username)
            current_app.logger.info(err)
            return redirect(url_for('auth.login_screen'))
        current_app.logger.info("Succesfull login for user %s", username)
        return redirect(url_for('upload.main_screen'))
    return render_template('login.html', form=form)


@auth.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login_screen'))