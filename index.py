from flask import Flask, render_template, request, redirect, session
import hashlib
import os
# import shutil
#from bs4 import BeautifulSoup
# import cgi
# import urllib.request
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField, SelectField
from wtforms.validators import InputRequired


UPLOAD_FOLDER = 'static/uploads/'  # craete forlder for upload video


app = Flask(__name__)
# session.get('status', "false") = "false"

# for upload video
app.config['SECURET_KEY'] = 'supersecretkey'
# app.config['UPLOAD_FOLDER'] = 'static/files'
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# for upload video


@app.route('/')
def index():
    return render_template('home.html', loggedin=session.get('status', "false"))


@app.route('/videos')
def catergories():
    return render_template('categories.html', loggedin=session.get('status', "false"))


@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html', loggedin=session.get('status', "false"))


@app.route('/newMothers')
def newMothers():
    return render_template('newMothers.html', loggedin=session.get('status', "false"))


@app.route('/prgnancyvideos')
def prgnancyvideos():
    return render_template('prgnancyvideos.html', loggedin=session.get('status', "false"))


@app.route('/about')
def about():
    return render_template('about.html', loggedin=session.get('status', "false"))


@app.route('/pictures')
def pictures():
    return render_template('pictures.html', loggedin=session.get('status', "false"))


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', loggedin=session.get('status', "false"))
    else:
        return redirect('/loginpage')


@app.route('/adminpage')
def adminpage():
    return render_template('adminpage.html', loggedin=session.get('status', "false"))


@app.route('/logout')
def logout():
    # Remove the session ID
    session['status'] = 'false'
    session.pop('username', None)
    return redirect('/loginpage')

# add video in the database/////////////////////////////////////////


# add file in upload file
class uploadfileform(FlaskForm):
    title = StringField(label=("Description"))
    file = FileField("File", validators=[InputRequired()])
    Dropdown = SelectField('Dropdown',
                           choices=[('option1', 'Pregnancy'), ('option2', 'Nutrition'), ('option3', 'New Mother')])
    submit = SubmitField("Upload File")

    # @app.route('/', methods=['GET', "POST"])
    @app.route('/upload', methods=['GET', "POST"])
    def upload_file():
        form = uploadfileform()
        if 'username' in session:
          if form.validate_on_submit():
            file = form.file.data  # first grap the file
        # Retrieve the selected option from the dropdown list
            selected_option = form.Dropdown.data
            # Determine the path where the file should be saved based on the selected option
            if selected_option == 'option1':
                # file_path = '/static/videos/Isifo sephepha (TB)'
                app.config['UPLOAD_FOLDER'] = 'static/videos/Isifo_sephepha (TB)'
            elif selected_option == 'option2':
                # file_path = '/static/videos/Nutrition'
                app.config['UPLOAD_FOLDER'] = 'static/videos/Nutrition'
            elif selected_option == 'option3':
                # file_path = '/static/videos/Early Childhood'
                app.config['UPLOAD_FOLDER'] = 'static/videos/Early_Childhood'
            # file.save(file_path)
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))  # Then save the file
            # return "File with {form.title.data} has been uploaded."
          return render_template('upload.html', form=form, loggedin=session.get('status', "false"))
        else:
           return redirect('/loginpage')
        

# ADD Video /////////////////////////////////////////////


def create_account(username, password):
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Save the username and hashed password to a file
    with open('credentials.txt', 'a') as f:
        f.write(f'{username},{hashed_password}\n')


app.secret_key = 'your secret key'


def login(username, password):
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the username and password match a stored credential
    with open('credentials.txt', 'r') as f:
        for line in f:
            stored_username, stored_password = line.strip().split(',')
            if stored_username == username and stored_password == hashed_password:
                return True
        return False


@app.route('/loginpage')
def loginpage():
    msg = ""
    if session.get('attempt') == "Failed":
        msg = "Login attempt failed. Check your username/password"
    return render_template('login.html', loggedin=session.get('status', 'false'), msg=msg)


@app.route('/login', methods=['POST'])
def loginform():
    username = request.form['username']
    password = request.form['password']

    if login(username, password):
       # Login successful
        session['username'] = username
        session['status'] = 'true'

    session['attempt'] = "Failed"

    return redirect('/upload')


# Test the functions
""" create_account('user1', 'password1')
create_account('user2', 'password2')

print(login('user1', 'password1'))  # True
print(login('user1', 'wrong_password'))  # False
print(login('wrong_username', 'password1'))  # False """


if __name__ == '__main__':
    app.run()
