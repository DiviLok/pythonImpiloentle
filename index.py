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

@app.route('/autoplay')
def autoplay():
    return render_template('autoplay.html')

@app.route('/adminpage')
def adminpage():
    return render_template('adminpage.html')





if __name__ == '__main__':
    app.run()


