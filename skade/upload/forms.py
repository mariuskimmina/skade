from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField


class UploadForm(FlaskForm):
    yara_scan = BooleanField("Apply Yara Rules")
    submit = SubmitField("Upload")