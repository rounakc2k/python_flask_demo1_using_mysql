from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import webbrowser
from threading import Timer

app = Flask(__name__)

# Configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'world'

mysql = MySQL(app)

@app.route('/' ,methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        if request.form.get('status'):
            return redirect('/status')

        if request.form.get('index'):
            return redirect('/index')

        if request.form.get('users'):
            return redirect('/users')

        if request.form.get('users1'):
            return redirect('/users1')
    return render_template('home.html')

@app.route('/status', methods=['GET', 'POST'])
def status():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        ID = userDetails['ID']
        status = userDetails['status']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE CITY SET status = %s where ID = %s",(status,ID))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('status.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        ID = userDetails['ID']
        Name = userDetails['Name']
        CountryCode = userDetails['CountryCode']
        District = userDetails['District']
        Population = userDetails['Population']
        status = userDetails['status']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO city(ID, Name, CountryCode, District, Population, status) VALUES(%s, %s, %s, %s, %s ,%s)",(ID, Name, CountryCode, District, Population, status))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("call Allusers")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

@app.route('/users1')
def users1():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT ID, Name FROM city")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users1.html',userDetails=userDetails)

def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == "__main__":
      Timer(1, open_browser).start();
      app.run(port=5000)
