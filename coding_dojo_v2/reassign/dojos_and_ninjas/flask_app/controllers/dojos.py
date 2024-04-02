# imports from flask to render templates, to redirect pages and to request data
from flask import render_template, redirect, request
# imports app from flask_app
from flask_app import app
#imports file dojo from flask_app/models
from flask_app.models.dojo import Dojo

#route to redirect to /dojos route
@app.route('/')
def index():
    return redirect('/dojos')
#route to render template of index html file and injecting data into it so we can access data on the page
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html",all_dojos = dojos)

# route to create new dojo, save and then redirect to /dojos route
@app.route('/create/dojo',methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')
#route to show specific dojo by id and then returning html page and injecting classmethod from models.dojo
@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo=Dojo.get_one_with_ninjas(data))