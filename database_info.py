
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+mysqlconnector://pyuser:1132006@localhost/enikiazomena')
db = SQLAlchemy(app)

engine = create_engine('mysql+mysqlconnector://pyuser:1132006@localhost/enikiazomena')

Session = sessionmaker(bind=engine)

# First Floor
class FirstFloor(db.Model):
    __tablename__ = 'firstfloor'
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False)
    apartment_number = db.Column(db.Integer, nullable=False)
    square_feet = db.Column(db.Integer, nullable=False)
    payment_month = db.Column(db.String(20), nullable=False)
    payment_method = db.Column(db.String(20), nullable=False, default='Bank')
    
# Second Floor
class SecondFloorApartment1(db.Model):
    __tablename__ = 'second_floor_apartment1'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    apartment_number = db.Column(db.Integer, nullable=False)
    square_feet = db.Column(db.Integer, nullable=False)
    payment_month = db.Column(db.String(15), nullable=False)
    payment_method = db.Column(db.String(10), nullable=False, default='Bank')
    phone_number = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(45), nullable=False, unique=True)

class SecondFloorApartment2(db.Model):
    __tablename__ = 'second_floor_apartment2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    apartment_number = db.Column(db.Integer, nullable=False)
    square_feet = db.Column(db.Integer, nullable=False)
    payment_month = db.Column(db.String(15), nullable=False)
    payment_method = db.Column(db.String(10), nullable=False, default='Bank')
    phone_number = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(45), nullable=False, unique=True)
    
# Third Floor
class ThirdFloorApartment1(db.Model):
    __tablename__ = 'third_floor_apartment_1'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    apartment_number = db.Column(db.Integer, nullable=False)
    square_feet = db.Column(db.Integer, nullable=False)
    payment_month = db.Column(db.String(255), nullable=False)
    payment_method = db.Column(db.String(255), nullable=False, default='bank')
    phone_number = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(45), nullable=False, unique=True)

class ThirdFloorApartment2(db.Model):
    __tablename__ = 'third_floor_apartment_2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    apartment_number = db.Column(db.Integer, nullable=False)
    square_feet = db.Column(db.Integer, nullable=False)
    payment_month = db.Column(db.String(255), nullable=False)
    payment_method = db.Column(db.String(255), nullable=False, default='bank')
    phone_number = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(45), nullable=False, unique=True)
    
# Fourth Floor
class FourthFloorApartment1(db.Model):
    __tablename__ = 'fourth_floor_apartment_1'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    apartment_number = db.Column(db.Integer, nullable=False)
    square_feet = db.Column(db.Integer, nullable=False)
    payment_month = db.Column(db.String(255), nullable=False)
    payment_method = db.Column(db.String(255), nullable=False, default='bank')
    phone_number = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(45), nullable=False, unique=True)


class FourthFloorApartment2(db.Model):
    __tablename__ = 'fourth_floor_apartment_2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    apartment_number = db.Column(db.Integer, nullable=False)
    square_feet = db.Column(db.Integer, nullable=False)
    payment_month = db.Column(db.String(255), nullable=False)
    payment_method = db.Column(db.String(255), nullable=False, default='bank')
    phone_number = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(45), nullable=False, unique=True)

    

if __name__ == 'main':
    app.run(debug=True)