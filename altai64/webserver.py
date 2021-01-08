from flask import Flask, url_for, render_template, request, redirect
from googleapi import Api
from notification import Notification
app = Flask(__name__)
api = Api()
n = Notification('1599455363:AAFjvwD5L6DUd6ky14s95tQNSrnao5pafto')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sendcallback", methods=['POST'])
def callback():
    if request.form['name'] and request.form['phone']:
        api.write(request.form['name'], request.form['phone'])
        n.send_n(phone=request.form['phone'], name=request.form['name'])
        return redirect(url_for('index'))
    abort(401)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9090
