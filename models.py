from app import db


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))

    def __repr__(self):
        return f'<User {self.mail}>'


class Candidates(db.Model):
    __tablename__ = 'candidates'
    candidate_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    votes = db.Column(db.Integer)
    description = db.Column(db.String(255))

    def __repr__(self):
        return f'<Candidate {self.name}>'


class Votes(db.Model):
    __tablename__ = 'votes'
    vote_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    candidate_id = db.Column(
        db.Integer, db.ForeignKey('candidates.candidate_id'))

    def __repr__(self):
        return f'<Vote {self.vote_id}>'
