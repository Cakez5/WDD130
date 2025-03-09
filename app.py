from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html', title="RoadMap")

@app.route('/games')
def games():
    return render_template('games.html', title="Games")

def home():
    return render_template('Logo.html', title='Flame Flair Studios')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


