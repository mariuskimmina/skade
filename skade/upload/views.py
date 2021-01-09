from flask.globals import current_app
from flask_login.utils import login_user, logout_user
from . import upload
from skade.models import User
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user
from skade.yara import scan


@upload.route('/', methods=["GET"])
def main_screen():
    return render_template('main.html')