from flask.globals import current_app
from flask_login.utils import login_user, logout_user
from . import upload
from .forms import UploadForm
from skade.models import User
from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, login_required
from skade.analyze.yara_module import scanner


@upload.route('/', methods=["GET"])
@login_required
def main_screen():
    form = UploadForm()
    return render_template('main.html', form=form)

@upload.route('/upload', methods=["POST"])
@login_required
def upload_endpoint():
    current_app.logger.debug("Upload Endpoint has been hit")
    uploaded_file = request.files['file[0]']
    yara = request.form.get("yarascan")

    if yara:
        current_app.logger.debug("Initalizing yara scan")
        try:
            scanner.start(uploaded_file)
        except scanner.NoRulesError as err:
            current_app.logger.debug("No Rules")

    return redirect(url_for('upload.main_screen'))


@upload.route('/result/<filehash>', methods=["GET", "POST"])
@login_required
def result_page(filehash):
    pass
