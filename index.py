from flask import Flask, render_template, request, redirect, session
import hashlib
import os
import shutil
from bs4 import BeautifulSoup
import cgi

app = Flask(__name__)
# session.get('status', "false") = "false"


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


videos = []  # Store the videos in a list


@app.route('/add_video', methods=['POST', 'GET'])
def add_video():
          
  #  category=['category1' , 'category2' , 'category3']
   source_path = "/videos"
   soup = BeautifulSoup('dashboard.html', 'html.parser')
   if request.method == 'POST':
        # Get the form data
###Has Error of getting data from form /////////
        form = cgi.FieldStorage()
        title = form.getvalue('title')
        category = form.getvalue('category')
        video_file = form.getfile('video_file')
        # title = request.form['title']
        # category = request.form['category']
        # video_file = request.form['video_file']
        option_tag = form.soup.find('option')
        option_value = form.option_tag.get('value')

###Has Error of getting data from form /////////
        
        if option_value == 'category1':
           destination_path = '/videos/Intsholongwane ka gawulayo ukhulelwe (HIV)'
           shutil.copy(source_path, destination_path)
           video_file.save(os.path.join('prgnancyvideos.html', video_file.filename))
           return render_template('prgnancyvideos.html', title=title)

        elif  option_value == 'category2':
           destination_path = 'videos/Nutrition'
           shutil.copy(source_path, destination_path)
           video_file.save(os.path.join('nutrition.html', video_file.filename))

           # Add the video to the list
        videos.append({
            'title': title,
            'category': category,
            'filename': video_file.filename
            })
        return redirect ('/dashboard')
   
##ADD Video /////////////////////////////////////////////
 

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
  return render_template('login.html',loggedin=session.get('status','false'), msg=msg)

@app.route('/login', methods=['POST'])
def loginform():
  username = request.form['username']
  password = request.form['password']

  if login(username, password):
     # Login successful
    session['username'] = username
    session['status'] = 'true'
  
  session['attempt'] = "Failed"

  return redirect('/dashboard')

# Test the functions
""" create_account('user1', 'password1')
create_account('user2', 'password2')

print(login('user1', 'password1'))  # True
print(login('user1', 'wrong_password'))  # False
print(login('wrong_username', 'password1'))  # False """


if __name__ == '__main__':
    app.run()


