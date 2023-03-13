# imports from flask to render templates, to redirect pages and to request data
from flask import render_template, redirect, request
# imports app from flask_app
from flask_app import app
#imports file dojo and ninja from flask_app/models
from flask_app.models import dojo, ninja
# route to render template for ninja html and use classmethod made in models.dojo
@app.route('/ninjas')
def ninjas():
    
    return render_template('ninja.html',dojos= dojo.Dojo.get_all())

# route to create and save ninja
@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')