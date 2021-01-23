import yara
import os
from flask.globals import current_app

def start(susfile):
    """
    This function applies yara rules to the upload file, looking a for a match

    Args:
        susfile (file): the file that yara rules should be applied on

    Returns:
        boolean: true if a match was found 
    """
    current_app.logger.debug("start applying Yara rules")
    rulefolder = current_app.config.get("YARA_RULES")
    rules = compile_yara_rules(rulefolder) 

    if rules is None:
        current_app.logger.error("No yara rules found, aborting scan")
        raise NoRulesError

    matches = rules.match(data=susfile.read())

    print(matches)
    if matches:
        current_app.logger.debug("Match found")
        return False

    current_app.logger.debug("No Match found")
    return True


def compile_yara_rules(rulefolder):
    """
    This function takes a folder name and tries to compile all yara rules in that given folder

    Args:
        rulefolder string: name of the folder containing yara rules 

    Returns:
        yara.Rules: compiled rules object
    """
    current_app.logger.debug("Compiling yara rules from source: %s", rulefolder)
    dFilepaths = {}
    for root, dirs, files in os.walk(rulefolder):
        for file in files:
            filename = os.path.join(root, file)
            dFilepaths[filename] = filename
    
    try:
        rules = yara.compile(filepaths=dFilepaths)
    except yara.SyntaxError as err:
        current_app.logger.error("Syntax error in Yara rule encountered")
        current_app.logger.error(err)
        return None
    return rules



class NoRulesError(Exception):
    """
    This Exception will be raised if there are no rules to work with
    """
    pass