# imports from flask to render templates, to store in session, to redirect pages and to request data
from flask import Flask, render_template, session, redirect,request
# app name
app = Flask(__name__)
#secret key used to access data
app.secret_key="Ami Chagol"
#route that returns (html page) rendered.
@app.route('/')
def index():
    return render_template("index.html")

#route that returns redirect to (route) rendered while defining what to store in session.
@app.route('/process',methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/success')
#route that returns (html page) rendered.
@app.route('/success')
def success():
    return render_template('success.html')

#for dev to debug app
if __name__=="__main__":
    app.run(debug=True)