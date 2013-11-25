from app import db
from hashlib import md5

"""
author: Andriy Rudyk
        Tim Sizemore

date:   21.10.2013

Represents the database scheme used by the application.
"""

ROLE_USER = 0
ROLE_ADMIN = 1
OPERATIONAL = 0
NON_OPERATIONAL = 1

class User(db.Model):
    """
    Represents the user of our application.
    """
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    first_name = db.Column(db.String(35), index = True, unique = False)
    last_name = db.Column(db.String(35), index = True, unique = False)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname = nickname).first() == None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname = new_nickname).first() == None:
                break
            version += 1
        return new_nickname

    def avatar(self, size):
        """
        Returns a user avator with a specified size from gravatar service.
        """
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Pibot(db.Model):
    """
    Represents a PiBot robot to be controlled by the user.
    """
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(35), index = True, unique = True)
    location = db.Column(db.String(36), index = True, unique = True)
    operational = db.Column(db.SmallInteger, default = OPERATIONAL)
    net_address = db.Column(db.String(16), index = True, unique = True)

    def __repr__(self):
        return '<Pibot %r>' % (self.name)

class Tour(db.Model):
    """
    Represents a tour when a user takes control of a PiBot.
    """
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime)
    deadline = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pibot_id = db.Column(db.Integer, db.ForeignKey('pibot.id'))

    def __repr__(self):
        return '<Tour Time %r>' % (self.date)
