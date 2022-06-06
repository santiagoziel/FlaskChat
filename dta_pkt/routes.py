from flask import render_template, url_for, redirect

from dta_pkt import app, db
from dta_pkt.forms import RegisterForm


@app.route('/', methods = ['GET', 'POST'])
def log_in():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        return redirect(url_for("chat", username = username))
    return render_template('index.html', form = form)

@app.route('/chat/<username>', methods = ['GET', 'POST'])
def chat(username):
    return render_template('chat.html', username = username)
