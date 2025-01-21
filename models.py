# models.py (Create database model)
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLALchemy instance
db=SQLAlchemy()

# Database model for user registration
class User(db.Model):
    __tablename__='user_registration'
    id=db.Column(db.Integer(), primary_key=True)
    username=db.Columnn(db.String(length=30), nullable=False, unique=True)
    email_address=db.Column(db.String(length=60), nullalble=False, unique=True)
    password_hash=db.Column(db.Integer(length=12), nullalble=False, unique=True)

