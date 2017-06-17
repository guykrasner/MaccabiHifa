import os
from flask import Flask, render_template
css_dir = os.path.abspath('../static')
template_dir = os.path.abspath('../templates')
app = Flask(__name__, template_folder=template_dir, static_folder=css_dir)

__author__ = 'Guy Krasner'

@app.route("/")
def home_page():
    return render_template('Homepage.html')

@app.route("/profile/<name>")
def profile_page(name):
    return render_template('ProfilePage.html', name=name)

if __name__ == '__main__':
    app.run()
