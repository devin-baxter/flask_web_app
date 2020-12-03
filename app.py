from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'm3g4byt3$'
app.config['MYSQL_DB'] = 'flask_app_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# Init MySQL
mysql = MySQL(app)

# Index and Home routes both render Home Page
@app.route('/')
def index():
	return render_template('home.html')

@app.route('/home')
def home():
	return render_template('home.html')

# About Us route
@app.route('/about')
def about():
	return render_template('about.html')

# Articles display page route
@app.route('/articles')
def articles():
	return render_template('articles.html', articles = Articles)

@app.route('/articles/<string:id>/')
def article(id):
	return render_template('article.html', id=id)

# Register form necessary for new user sign-up
class RegisterForm(Form):
	name = StringField('Name', [validators.Length(min=1, max=50)])
	email = StringField('Email', [validators.Length(min=6, max=50)])
	username = StringField('Username', [validators.Length(min=4, max=25)])
	password = PasswordField('Password', [
		validators.DataRequired(),
		validators.EqualTo('confirm_pw', message='Passwords do not match')
	])
	confirm_pw = PasswordField('Confirm Password', [
		validators.DataRequired(),
		validators.EqualTo('password', message='Passwords do not match')
	])
# Register Page route
@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		name = form.name.data
		email = form.email.data
		username = form.username.data
		password = sha256_crypt.encrypt(str(form.password.data))
		# Create Cursor
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
		# Commit data to DB
		mysql.connection.commit()
		#Close connection
		cur.close()
		# Successful Flash Message
		flash('Registration Successful', 'success')
		redirect(url_for('home'))
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

# Login Page route
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		# Get Form Fields
		username = request.form['username']
		password_candidate = request.form['password']
		# Create Cursor and MySQL Connection
		cur = mysql.connection.cursor()
		# Get user via username
		result = cur.execute("SELECT * FROM users WHERE username = %s", [username])
		if result > 0:
			# Get stored hash
			data = cur.fetchone()
			password = data['password']
			# Compare Passwords
			if sha256_crypt.verify(password_candidate, password):
				# Successful Login
				session["logged_in"] = True
				session['username'] = username
				flash('You are logged in', 'success')
				return redirect(url_for('dashboard'))
			else:
				error = 'Invalid login'
				app.logger.info('INVALID LOGIN ATTEMPT')
				return render_template('login.html', error=error)
			# Close Connection
			cur.close()
		else:
			error = 'Username not found'
			return render_template('login.html', error=error)
	return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
	session.clear
	flash('You are now logged out', 'success')
	return redirect(url_for('login'))

# Dashboard Page route
@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')



if __name__ == '__main__':
	app.secret_key='12345'
	app.run(debug=True)
