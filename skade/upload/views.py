from flask.globals import current_app
from flask_login.utils import login_user, logout_user
from . import upload
from skade.models import User
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, login_required
from skade.analyze.yararules import yara_scan


@upload.route('/', methods=["GET"])
@login_required
def main_screen():
    return render_template('main.html')

@upload.route('/upload', methods=["POST"])
@login_required
def upload_endpoint():
    print("upload endpoint has been hit")
    print(request.form)
    uploaded_file = request.form.get('test')
    print(uploaded_file)
    return redirect(url_for('upload.main_screen'))