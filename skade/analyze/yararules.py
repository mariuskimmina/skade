import yara
from flask.globals import current_app

def yara_scan():
    rulefile = current_app.config.get("YARA_RULES")
    rules = yara.compile(rulefile)
    pass
