from flask import Blueprint

upload = Blueprint(
    'upload',
    __name__,
    template_folder='../templates/upload',
    static_folder="../static/"
)