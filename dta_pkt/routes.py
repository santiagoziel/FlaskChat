from flask import render_template

from dta_pkt import app, db

@app.route('/', methods = ['GET', 'POST'])
def log_in():
    return render_template('index.html')

@app.route('/chat', methods = ['GET', 'POST'])
def chat():
    return render_template('chat.html')
