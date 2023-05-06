from flask import Flask,render_template, request, redirect,session,url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
import os,jinja2
import pandas as pd
import io
import xlsxwriter
from flask import make_response




app = Flask(__name__)

app.jinja_loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://pyuser:1132006@localhost/enikiazomena'
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Reload templates during development
db = SQLAlchemy(app)
engine = create_engine('mysql+mysqlconnector://pyuser:1132006@localhost/enikiazomena')
Session = sessionmaker(bind=engine)
class FirstFloor(db.Model):
    __tablename__ = 'FirstFloor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    apartment_number = db.Column(db.Integer, nullable=False)
    square_feet = db.Column(db.Integer, nullable=False)
    payment_month = db.Column(db.String(20), nullable=False)
    payment_method = db.Column(db.String(20), nullable=False, default='Bank')

@app.route('/', methods=['GET', 'POST'])
def first_floor():
 try:
    session = Session()
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            id = request.form.get('id')
            name = request.form.get('name')
            apartment_number = request.form.get('apartment_number')
            square_feet = request.form.get('square_feet')
            payment_month = request.form.get('payment_month')
            payment_method = request.form.get('payment_method')
            row = FirstFloor(id=id,name=name, apartment_number=apartment_number,
                             square_feet=square_feet, payment_month=payment_month,
                             payment_method=payment_method)
            session.add(row)
            session.commit()
            return redirect('/')
        elif action == 'delete':
            id = request.form.get('id')
            row = session.query(FirstFloor).filter_by(id=id).first()
            session.delete(row)
            session.commit()
            return redirect('/')
        elif action == 'update':
            id = request.form.get('id')
            row = session.query(FirstFloor).filter_by(id=id).first()
            row.name = request.form.get('name')
            row.apartment_number = request.form.get('apartment_number')
            row.square_feet = request.form.get('square_feet')
            row.payment_month = request.form.get('payment_month')
            row.payment_method = request.form.get('payment_method')
            session.commit()
            return redirect('/')
    return render_template('indexall.html', first_floor=session.query(FirstFloor).all())
 
 except Exception as e:
        print("An error occurred: ", e)
        return "Sorry, there was an error processing your request. Please try again later."
#------------------------------------------------------------------------------------------
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

@app.route('/', methods=['GET', 'POST'])
def second_floor_apartment1():
  try:
    session = Session()
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            id = request.form.get('id')
            name = request.form.get('name')
            apartment_number = request.form.get('apartment_number')
            square_feet = request.form.get('square_feet')
            payment_month = request.form.get('payment_month')
            payment_method = request.form.get('payment_method')
            phone_number = request.form.get("phone_number")
            email = request.form.get('email')
            row = SecondFloorApartment1(id=id,name=name, apartment_number=apartment_number,
                             square_feet=square_feet, payment_month=payment_month,
                             payment_method=payment_method,phone_number=phone_number,email=email)
            session.add(row)
            session.commit()
            return redirect('/')
        elif action == 'delete':
            id = request.form.get('id')
            row = session.query(SecondFloorApartment1).filter_by(id=id).first()
            session.delete(row)
            session.commit()
            return redirect('/')
        elif action == 'update':
            id = request.form.get('id')
            row = session.query(SecondFloorApartment1).filter_by(id=id).first()
            row.name = request.form.get('name')
            row.apartment_number = request.form.get('apartment_number')
            row.square_feet = request.form.get('square_feet')
            row.payment_month = request.form.get('payment_month')
            row.payment_method = request.form.get('payment_method')
            row.phone_number = request.form.get('phone_number')
            row.email = request.form.get('email')
            session.commit()
            return redirect('/')
    return render_template('indexall.html', second_floor_apartment1=session.query(SecondFloorApartment1).all())
  
  except Exception as e:
        print("An error occurred: ", e)
        return "Sorry, there was an error processing your request. Please try again later."
#-----------------------------------------------------------------------------------------------------------------

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



@app.route('/', methods=['GET', 'POST'])
def second_floor_apartment2():
 try:
    session = Session()
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            id = request.form.get('id')
            name = request.form.get('name')
            apartment_number = request.form.get('apartment_number')
            square_feet = request.form.get('square_feet')
            payment_month = request.form.get('payment_month')
            payment_method = request.form.get('payment_method')
            phone_number = request.form.get('phone_number')
            email = request.form.get('email')
            row = SecondFloorApartment2(id=id,name=name, apartment_number=apartment_number,
                             square_feet=square_feet, payment_month=payment_month,
                             payment_method=payment_method,phone_number=phone_number,email=email)
            session.add(row)
            session.commit()
            return redirect('/')
        elif action == 'delete':
            id = request.form.get('id')
            row = session.query(SecondFloorApartment2).filter_by(id=id).first()
            session.delete(row)
            session.commit()
            return redirect('/')
        elif action == 'update':
            id = request.form.get('id')
            row = session.query(SecondFloorApartment2).filter_by(id=id).first()
            row.name = request.form.get('name')
            row.apartment_number = request.form.get('apartment_number')
            row.square_feet = request.form.get('square_feet')
            row.payment_month = request.form.get('payment_month')
            row.payment_method = request.form.get('payment_method')
            row.phone_number = request.form.get('phone_number')
            row.email = request.form.get('email')
            session.commit()
            return redirect('/')
    return render_template('indexall.html', second_floor_apartment2=session.query(SecondFloorApartment2).all())
  
 except Exception as e:
        print("An error occurred: ", e)
        return "Sorry, there was an error processing your request. Please try again later."
#---------------------------------------------------------------------------------------------------------------
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


    
@app.route('/', methods=['GET', 'POST'])
def third_floor_apartment1():
  try:
    session = Session()
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            id = id = request.form.get('id')
            name = request.form.get('name')
            apartment_number = request.form.get('apartment_number')
            square_feet = request.form.get('square_feet')
            payment_month = request.form.get('payment_month')
            payment_method = request.form.get('payment_method')
            phone_number = request.form.get('phone_number')
            email = request.form.get('email')
            row = ThirdFloorApartment1(id=id,name=name, apartment_number=apartment_number,
                             square_feet=square_feet, payment_month=payment_month,
                             payment_method=payment_method,phone_number=phone_number,email=email)
            session.add(row)
            session.commit()
            return redirect('/')
        elif action == 'delete':
            id = request.form.get('id')
            row = session.query(ThirdFloorApartment1).filter_by(id=id).first()
            session.delete(row)
            session.commit()
            return redirect('/')
        elif action == 'update':
            id = request.form.get('id')
            row = session.query(ThirdFloorApartment1).filter_by(id=id).first()
            row.name = request.form.get('name')
            row.apartment_number = request.form.get('apartment_number')
            row.square_feet = request.form.get('square_feet')
            row.payment_month = request.form.get('payment_month')
            row.payment_method = request.form.get('payment_method')
            row.phone_number = request.form.get('phione_number')
            row.email = request.form.get('email')
            session.commit()
            return redirect('/')
    return render_template('indexall.html', second_floor_apartment2=session.query(ThirdFloorApartment1).all())
  
  except Exception as e:
        print("An error occurred: ", e)
        return "Sorry, there was an error processing your request. Please try again later."
#--------------------------------------------------------------------------------------------------------------

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




@app.route('/', methods=['GET', 'POST'])
def third_floor_apartment2():
  try:
    session = Session()
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            id = request.form.get('id')
            name = request.form.get('name')
            apartment_number = request.form.get('apartment_number')
            square_feet = request.form.get('square_feet')
            payment_month = request.form.get('payment_month')
            payment_method = request.form.get('payment_method')
            phone_number = request.form.get('phone_number')
            email = request.form.get('email')
            row = ThirdFloorApartment2(id=id,name=name, apartment_number=apartment_number,
                             square_feet=square_feet, payment_month=payment_month,
                             payment_method=payment_method,phone_number=phone_number,email=email)
            session.add(row)
            session.commit()
            return redirect('/')
        elif action == 'delete':
            id = request.form.get('id')
            row = session.query(ThirdFloorApartment2).filter_by(id=id).first()
            session.delete(row)
            session.commit()
            return redirect('/')
        elif action == 'update':
            id = request.form.get('id')
            row = session.query(ThirdFloorApartment2).filter_by(id=id).first()
            row.name = request.form.get('name')
            row.apartment_number = request.form.get('apartment_number')
            row.square_feet = request.form.get('square_feet')
            row.payment_month = request.form.get('payment_month')
            row.payment_method = request.form.get('payment_method')
            row.phone_number = request.form.get('phone_number')
            row.email = request.form.get('email')
            session.commit()
            return redirect('/')
    return render_template('indexall.html', second_floor_apartment2=session.query(ThirdFloorApartment2).all())
  
  except Exception as e:
        print("An error occurred: ", e)
        return "Sorry, there was an error processing your request. Please try again later."
#----------------------------------------------------------------------------------------------------------------


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




@app.route('/', methods=['GET', 'POST'])
def fourth_floor_apartment1():
  try:
    session = Session()
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            id = request.form.get('id')
            name = request.form.get('name')
            apartment_number = request.form.get('apartment_number')
            square_feet = request.form.get('square_feet')
            payment_month = request.form.get('payment_month')
            payment_method = request.form.get('payment_method')
            phone_number = request.form.get('phone_number')
            email = request.form.get('email')
            row = FourthFloorApartment1(id=id,name=name, apartment_number=apartment_number,
                             square_feet=square_feet, payment_month=payment_month,
                             payment_method=payment_method,phone_number=phone_number,email=email)
            session.add(row)
            session.commit()
            return redirect('/')
        elif action == 'delete':
            id = request.form.get('id')
            row = session.query(FourthFloorApartment1).filter_by(id=id).first()
            session.delete(row)
            session.commit()
            return redirect('/')
        elif action == 'update':
            id = request.form.get('id')
            row = session.query(FourthFloorApartment1).filter_by(id=id).first()
            row.name = request.form.get('name')
            row.apartment_number = request.form.get('apartment_number')
            row.square_feet = request.form.get('square_feet')
            row.payment_month = request.form.get('payment_month')
            row.payment_method = request.form.get('payment_method')
            row.phone_number = request.form.get('phone_number')
            row.email = request.form.get('email')
            session.commit()
            return redirect('/')
    return render_template('indexall.html', second_floor_apartment2=session.query(FourthFloorApartment1).all())
  
  except Exception as e:
        print("An error occurred: ", e)
        return "Sorry, there was an error processing your request. Please try again later."
#----------------------------------------------------------------------------------------------------------------

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

@app.route('/', methods=['GET', 'POST'])
def fourth_floor_apartment2():
  try:
    session = Session()
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            id = request.form.get('id')
            name = request.form.get('name')
            apartment_number = request.form.get('apartment_number')
            square_feet = request.form.get('square_feet')
            payment_month = request.form.get('payment_month')
            payment_method = request.form.get('payment_method')
            phone_number = request.form.get('phone_number')
            email = request.form.get('email')
            row = FourthFloorApartment2(id=id,name=name, apartment_number=apartment_number,
                             square_feet=square_feet, payment_month=payment_month,
                             payment_method=payment_method,phone_number=phone_number,email=email)
            session.add(row)
            session.commit()
            return redirect('/')
        elif action == 'delete':
            id = request.form.get('id')
            row = session.query(FourthFloorApartment2).filter_by(id=id).first()
            session.delete(row)
            session.commit()
            return redirect('/')
        elif action == 'update':
            id = request.form.get('id')
            row = session.query(FourthFloorApartment2).filter_by(id=id).first()
            row.name = request.form.get('name')
            row.apartment_number = request.form.get('apartment_number')
            row.square_feet = request.form.get('square_feet')
            row.payment_month = request.form.get('payment_month')
            row.payment_method = request.form.get('payment_method')
            row.phone_number = request.form.get('phone_number')
            row.email = request.form.get('email')
            session.commit()
            return redirect('/')
    return render_template('indexall.html', second_floor_apartment2=session.query(FourthFloorApartment2).all())
  except Exception as e:
        print("An error occurred: ", e)
        return "Sorry, there was an error processing your request. Please try again later."
#--------------------------------------------------------------------------------------------------------------


@app.route('/data', methods=['GET', 'POST'])
def data():
    try:
        # select queries to fetch all data from each table
        df = pd.read_sql_query('SELECT * FROM firstfloor', engine)
        df2 = pd.read_sql_query('SELECT * FROM second_floor_apartment1', engine)
        df3 = pd.read_sql_query('SELECT * FROM second_floor_apartment2', engine)
        df4 = pd.read_sql_query('SELECT * FROM third_floor_apartment1', engine)
        df5 = pd.read_sql_query('SELECT * FROM third_floor_apartment2', engine)
        df6 = pd.read_sql_query('SELECT * FROM fourth_floor_apartment1', engine)
        df7 = pd.read_sql_query('SELECT * FROM fourth_floor_apartment2', engine)

        # concatenate the dataframes into a single dataframe
        df_final = pd.concat([df, df2, df3, df4, df5, df6, df7], ignore_index=True)

        # Convert the dataframe to a list of dictionaries
        apartments = df_final.to_dict('records')

        # Create an in-memory output file for the workbook
        output = io.BytesIO()

        # Create a workbook and worksheet
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        # Write the headers to the worksheet
        headers = ['Id', 'Name', 'Apartment Number', 'Square Feet', 'Payment Month', 'Payment Method']
        for i, header in enumerate(headers):
            worksheet.write(0, i, header)

        # Write the data to the worksheet
        for i, apartment in enumerate(apartments):
            worksheet.write(i+1, 0, apartment['id'])
            worksheet.write(i+1, 1, apartment['name'])
            worksheet.write(i+1, 2, apartment['apartment_number'])
            worksheet.write(i+1, 3, apartment['square_feet'])
            worksheet.write(i+1, 4, apartment['payment_month'])
            worksheet.write(i+1, 5, apartment['payment_method'])

        # Close the workbook
        workbook.close()

        # Set the content type and disposition headers
        response = make_response(output.getvalue())
        response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        response.headers['Content-Disposition'] = 'attachment; filename=apartments.xlsx'

        return response

    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred while fetching the data."    


#--------------------------------------------------------------------------------------------------------------
if __name__ ==('__main__'):
    app.run(debug=True)
