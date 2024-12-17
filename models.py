from app import db


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    quota = db.Column(db.Integer)

    def __repr__(self):
        return f'<User {self.mail}>'


class Events(db.Model):
    __tablename__ = 'events'
    event_id = db.Column(db.Integer, primary_key=True)
    event_title = db.Column(db.String(100))
    description = db.Column(db.String(255))
    location = db.Column(db.String(100))
    date = db.Column(db.Date)
    participants = db.Column(db.Integer)

    def __repr__(self):
        return f'<Event {self.event_title}>'


class Bookings(db.Model):
    __tablename__ = 'bookings'
    vote_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))

    def __repr__(self):
        return f'<Booking {self.vote_id}>'
