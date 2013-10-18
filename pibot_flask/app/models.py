from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

OPERATIONAL = 0
NON_OPERATIONAL = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    first_name = db.Column(db.String(35), index = True, unique = False)
    last_name = db.Column(db.String(35), index = True, unique = False)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Pibot(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(35), index = True, unique = True)
    location = db.Column(db.String(35), index = True, unique = True)
    operational = db.Column(db.SmallInteger, default = OPERATIONAL)
    net_address = db.Column(db.String(16), index = True, unique = True)
    
    def __repr__(self):
        return '<Pibot %r>' % (self.name)

class Tour(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime)
    deadline = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pibot_id = db.Column(db.Integer, db.ForeignKey('pibot.id'))
    
    def __repr__(self):
        return '<Tour Time %r>' % (self.date)
