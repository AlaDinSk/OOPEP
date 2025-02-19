from datetime import datetime
from email.policy import default

from ..extensions import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    p_p = db.Column(db.Integer)
    subject = db.Column(db.String(50))
    teacher = db.Column(db.String(50))
    student = db.Column(db.String(50))
    date = db.Column(db.DateTime, default=datetime.utcnow())

class Operator_db(db.Model):
    __tablename__ = 'operator_db'
    id = db.Column(db.Integer, primary_key=True)
    item_journal = db.Column(db.String(20), nullable=True)
    conditional_name = db.Column(db.String(20), nullable=True)
    valid_name = db.Column(db.String(20), nullable=True)
    subordination = db.Column(db.String(20), nullable=True)
    out_number = db.Column(db.String(20), nullable=True)
    in_number = db.Column(db.String(20), nullable=True)
    oid = db.Column(db.String(20), nullable=True, unique=True)
    name = db.Column(db.String(30), nullable=True)
    type_certificate = db.Column(db.String(4), nullable=True)
    status = db.Column(db.String(10), nullable=True)
    electronic_request = db.Column(db.String(20), nullable=True)
    release = db.Column(db.String(20), nullable=True)
    number_notification = db.Column(db.String(20), nullable=True)
    date_notification = db.Column(db.String(20), nullable=True)
    return_certificate = db.Column(db.String(10), nullable=True)
    filing_case = db.Column(db.String(10), nullable=True)
    note = db.Column(db.String(40), nullable=True)

class Holder_db(db.Model):
    __tablename__ = 'holder_db'
    id = db.Column(db.Integer, primary_key=True)
    item_journal = db.Column(db.String(20), nullable=True)
    conditional_name = db.Column(db.String(20), nullable=True)
    valid_name = db.Column(db.String(20), nullable=True)
    subordination = db.Column(db.String(20), nullable=True)
    out_number = db.Column(db.String(20), nullable=True)
    in_number = db.Column(db.String(20), nullable=True)
    oid = db.Column(db.String(20), nullable=True, unique=True)
    name = db.Column(db.String(30), nullable=True)
    status = db.Column(db.String(10), nullable=True)
    electronic_request = db.Column(db.String(20), nullable=True)
    release = db.Column(db.String(20), nullable=True)
    number_notification = db.Column(db.String(20), nullable=True)
    date_notification = db.Column(db.String(20), nullable=True)
    return_certificate = db.Column(db.String(10), nullable=True)
    filing_case = db.Column(db.String(10), nullable=True)
    note = db.Column(db.String(40), nullable=True)

class Unqualified_db(db.Model):
    __tablename__ = 'unqualified_db'
    id = db.Column(db.Integer, primary_key=True)
    item_journal = db.Column(db.String(20), nullable=True)
    conditional_name = db.Column(db.String(20), nullable=True)
    valid_name = db.Column(db.String(20), nullable=True)
    subordination = db.Column(db.String(20), nullable=True)
    out_number = db.Column(db.String(20), nullable=True)
    in_number = db.Column(db.String(20), nullable=True)
    oid = db.Column(db.String(20), nullable=True, unique=True)
    name = db.Column(db.String(30), nullable=True)
    status = db.Column(db.String(10), nullable=True)
    electronic_request = db.Column(db.String(20), nullable=True)
    release = db.Column(db.String(20), nullable=True)
    number_notification = db.Column(db.String(20), nullable=True)
    date_notification = db.Column(db.String(20), nullable=True)
    return_certificate = db.Column(db.String(10), nullable=True)
    filing_case = db.Column(db.String(10), nullable=True)
    note = db.Column(db.String(40), nullable=True)

class Cancellation_db(db.Model):
    __tablename__ = 'cancellation_db'
    id = db.Column(db.Integer, primary_key=True)
    item_journal = db.Column(db.String(20), nullable=True)
    conditional_name = db.Column(db.String(20), nullable=True)
    valid_name = db.Column(db.String(20), nullable=True)
    subordination = db.Column(db.String(20), nullable=True)
    out_number = db.Column(db.String(20), nullable=True)
    in_number = db.Column(db.String(20), nullable=True)
    oid = db.Column(db.String(20), nullable=True, unique=True)
    name = db.Column(db.String(30), nullable=True)
    status = db.Column(db.String(10), nullable=True)
    date_cancellation = db.Column(db.String(20), nullable=True)
    oid_cancellation = db.Column(db.String(20), nullable=True, unique=True)
    number_notification = db.Column(db.String(10), nullable=True)
    date_notification = db.Column(db.String(10), nullable=True)
    filing_case = db.Column(db.String(10), nullable=True)
    note = db.Column(db.String(40), nullable=True)