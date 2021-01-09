from flask.globals import current_app
from flask_login.utils import login_user, logout_user
from . import auth
from skade.models import User
from skade import db
from .forms import LoginForm, RegisterForm
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user


@auth.route('/login', methods=["GET", "POST"])
def login_screen():
    if current_user.is_authenticated:
        return redirect(url_for('upload.main_screen'))
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            current_app.logger.info("login failed for user: %s", username)
            flash('Invalid username or password')
            return redirect(url_for('auth.login_screen'))
        try:
            login_user(user)
        except Exception as err:
            current_app.logger.info("Login failed for user %s", username)
            current_app.logger.info(err)
            return redirect(url_for('auth.login_screen'))
        current_app.logger.info("Succesfull login for user %s", username)
        return redirect(url_for('upload.main_screen'))
    return render_template('login.html', form=form)

@auth.route('/register', methods=["GET", "POST"])
def register_screen():
    form = RegisterForm()
    if form.validate_on_submit():
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login_screen'))
    return render_template('register.html', form=form)



@auth.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login_screen'))