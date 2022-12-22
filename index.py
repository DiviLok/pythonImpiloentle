from flask import Flask, render_template, request, redirect, session
import hashlib

app = Flask(__name__)
#session.get('status', "false") = "false"

@app.route('/')
def index():
    return render_template('home.html',loggedin=session.get('status', "false"))

@app.route('/videos')
def catergories():
    return render_template('categories.html',loggedin=session.get('status', "false"))
    
@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html',loggedin=session.get('status', "false"))

@app.route('/newMothers')
def newMothers():
    return render_template('newMothers.html',loggedin=session.get('status', "false"))

@app.route('/prgnancyvideos')
def prgnancyvideos():
    return render_template('prgnancyvideos.html',loggedin=session.get('status', "false"))

@app.route('/about')
def about():
    return render_template('about.html',loggedin=session.get('status', "false"))

@app.route('/pictures')
def pictures():
    return render_template('pictures.html',loggedin=session.get('status', "false"))

@app.route('/dashboard')
def dashboard(): 
  if 'username' in session:
    return render_template('dashboard.html',loggedin=session.get('status', "false"))
  else:
    return redirect('/loginpage')
  

@app.route('/adminpage')
def adminpage():
    return render_template('adminpage.html',loggedin=session.get('status', "false"))

@app.route('/logout')
def logout():
    # Remove the session ID
    session['status']='false'
    session.pop('username', None)
    return redirect('/loginpage')

# add video in the database/////////////////////////////////////////

# videos = []  # Store the videos in a list

# @app.route('/autoplay')
# def autoplay():
#     # Get the list of categories
#     categories = get_categories()
#     return render_template('autoplay.html', categories=categories)

# @app.route('/add_video', methods=['GET', 'POST'])
# def add_video():
#     if request.method == 'POST':
#         # Get the form data
#         title = request.form['title']
#         category = request.form['category']
#         video_file = request.files['video_file']

#         # Save the video file to the server
#         video_file.save(os.path.join('path/to/save/location', video_file.filename))

#         # Add the video to the list
#         videos.append({
#             'title': title,
#             'category': category,
#             'filename': video_file.filename
#         })

#         # Redirect to the dashboard page
#         return redirect('/autoplay')

# login credentials
 

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


