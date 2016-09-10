from app import db

DEFAULT_TZ = "Asia/Kolkata"
DEFAULT_LOCALE = "en_in"


class User(db.Model):
    """
    The User model which stores the email, password and the names of the users
    @TODO: add from_json properties
    """
    id = db.column(db.Integer, primary_key=True)
    email = db.Column(db.String, default=None)
    first_name = db.Column(db.String, default=None)
    last_name = db.Column(db.String, default=None)
