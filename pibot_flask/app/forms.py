from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

"""
author: Andriy Rudyk
        Tim Sizemore

date:   21.10.2013

Forms used in the application.
"""

class LoginForm(Form):
    """
    Form used to login into the system using openid
    """
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
