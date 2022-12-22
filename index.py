from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/videos')
def catergories():
    return render_template('categories.html')
    
@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@app.route('/newMothers')
def newMothers():
    return render_template('newMothers.html')

@app.route('/prgnancyvideos')
def prgnancyvideos():
    return render_template('prgnancyvideos.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/pictures')
def pictures():
    return render_template('pictures.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/adminpage')
def adminpage():
    return render_template('adminpage.html')

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



if __name__ == '__main__':
    app.run()


