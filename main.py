from flask import Flask, render_template, request, redirect, url_for, session
import bcrypt
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key='h+\xe1GP]\x9eyB\xcf\xf4\x88_z\x01>'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'recommendation_system'

mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route("/register/", methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        mobile = request.form['mobile']
        pwd = request.form['password']
        cpwd = request.form['cpassword']
        if len(username) > 0 and len(fname) > 0 and len(lname) > 0 and len(pwd) > 0 and len(email) > 0 and len(
                mobile) > 0 and len(cpwd) > 0:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM useraccount WHERE username = % s', (username,))
            account = cursor.fetchone()
            cursor.execute('SELECT * FROM useraccount WHERE email = % s', (email,))
            account1 = cursor.fetchone()
            cursor.execute('SELECT * FROM useraccount WHERE mobile = % s', (mobile,))
            account2 = cursor.fetchone()
            if account:
                msg = 'Account already exists with this username!'
            elif account1:
                msg = 'Account already exists with this email !'
            elif account2:
                msg = 'Account already exists with this mobile number !'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Username must contain only characters and numbers !'
            elif not username or not pwd or not email or not mobile or not cpwd or not fname or not lname:
                msg = 'Please fill out the form !'
            elif len(mobile) != 10:
                msg = 'Enter 10 digit number !'
            elif cpwd != pwd:
                msg = 'Password does not match!'
            else:
                hashed = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())
                cursor.execute('INSERT INTO useraccount VALUES (NULL, % s, % s, % s,% s,% s,% s, %s)',
                               (username, fname, lname, email, mobile, hashed, hashed,))
                mysql.connection.commit()
                cursor.close()
                msg = 'You have successfully registered !'
        else:
            msg = 'Please fill out the form !'

    return render_template('register.html', msg=msg)



app.run(debug=True )
