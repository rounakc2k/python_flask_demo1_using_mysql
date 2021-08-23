import MySQLdb.cursors
import re
from flask import Flask, render_template, request, redirect ,  url_for, session, jsonify
from flask_mysqldb import MySQL
import webbrowser
import threading
from threading import Timer

app = Flask(__name__)

app.secret_key = '8\x9b\x08`I\xd5\rh\xaa,.\xf3\xf8\x81\xe4MI\x06\xaf\xe4\xcd\x97X\xa1'
# Configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'world'

mysql = MySQL(app)

@app.route('/' ,methods=['GET','POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'type' in request.form:
       # Fetch form data
       username = request.form['username']
       password = request.form['password']
       type = request.form['type']
    
       cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       cur.execute('select * from login where username = %s and password = %s and type = %s',(username,password,type, ))
       account = cur.fetchone()

       if account and account['type'] == 'user':
            session['loggedin'] = True
            session['username'] = account['username']
            session['password'] = account['password']
            session['type'] = account['type']
            return redirect('/home1')

       if account and account['type'] == 'manager':
            session['loggedin'] = True
            session['username'] = account['username']
            session['password'] = account['password']
            session['type'] = account['type']
            return redirect('/home2')

       else:
           return 'Incorrect Credentials'

    return render_template('login.html')



@app.route('/home1' ,methods=['GET','POST'])
def home1():
    if request.method == 'POST':

            proceduresindex = [
            ['procedure1',"call Allusers"],
            ['procedure2',"SELECT ID, Name FROM city"]
            ]

            procedurename = ['Procedure 1','Procedure 2']

            x = []

            for i in range(len(proceduresindex)):

                if request.form.get(proceduresindex[i][0]):
                    cur = mysql.connection.cursor()
                    cur.execute(proceduresindex[i][1])
                    cur.close()
                    x.append(procedurename[i])

            # for i in range(len(proceduresindex)):

            #     if request.form.get(proceduresindex[i][0]):
            #         x.append(proceduresindex[i][0])
                   
                    # userDetails = [proceduresindex[i][0]]
                    
                    # msg = 'Procedure Executed'
                    # return jsonify(msg)

            return render_template('executed.html', x = x ) 
            
    return render_template('home1.html')

@app.route('/home2' ,methods=['GET','POST'])
def home2():
    if request.method == 'POST':

            proceduresindex = [
            ['procedure1',"call Allusers"],
            ['procedure2',"SELECT ID, Name FROM city"],
            ['procedure3',"SELECT Name FROM city"],
            ['procedure4',"SELECT ID FROM city"]
            ]

            procedurename = ['Procedure 1','Procedure 2','Procedure 3','Procedure 4']

            x = []

            for i in range(len(proceduresindex)):

                if request.form.get(proceduresindex[i][0]):
                    cur = mysql.connection.cursor()
                    cur.execute(proceduresindex[i][1])
                    cur.close()
                    x.append(procedurename[i])

            # for i in range(len(proceduresindex)):

            #     if request.form.get(proceduresindex[i][0]):
            #         return 'Procedure Executed'

            return render_template('executed.html', x = x ) 
     
    return render_template('home2.html')


# @app.route('/status', methods=['GET', 'POST'])
# def status():
#     if request.method == 'POST':
#         # Fetch form data
#         userDetails = request.form
#         ID = userDetails['ID']
#         status = userDetails['status']
#         cur = mysql.connection.cursor()
#         cur.execute("UPDATE CITY SET status = %s where ID = %s",(status,ID))
#         mysql.connection.commit()
#         cur.close()
#         return redirect('/users')
#     return render_template('status.html')

# @app.route('/index', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Fetch form data
#         userDetails = request.form
#         ID = userDetails['ID']
#         Name = userDetails['Name']
#         CountryCode = userDetails['CountryCode']
#         District = userDetails['District']
#         Population = userDetails['Population']
#         status = userDetails['status']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO city(ID, Name, CountryCode, District, Population, status) VALUES(%s, %s, %s, %s, %s ,%s)",(ID, Name, CountryCode, District, Population, status))
#         mysql.connection.commit()
#         cur.close()
#         return redirect('/users')
#     return render_template('index.html')

# @app.route('/users')
# def users():
#     cur = mysql.connection.cursor()
#     cur.execute("call Allusers")
#     cur.close()
#     return 'Executed Procedure'

# @app.route('/users1')
# def users1():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT ID, Name FROM city")
#     cur.close()
#     return render_template('users1.html',userDetails='Procedure 4')

def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == "__main__":
      Timer(1, open_browser).start();
      app.run(port=5000)
