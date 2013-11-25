from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectField, DateTimeField
from wtforms.validators import Required
from app import db, models

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

class EditForm(Form):
    """
    Form used to edit user profile.
    """
    nickname = TextField('nickname', validators = [Required()])
    first_name = TextField('first_name', validators = [Required()])
    last_name = TextField('first_name', validators = [Required()])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname = self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True

class TourRegisterForm(Form):
    pibots = models.Pibot.query.all()
    for i, bot in enumerate(pibots):
        pibots[i] = (bot.name, bot.location)
    start = DateTimeField('start', validators = [Required()], format='%Y-%m-%d %H:%M:%S')
    finish = DateTimeField('finish', validators = [Required()], format='%Y-%m-%d %H:%M:%S')
    pibot = SelectField('pibot', choices=pibots)

