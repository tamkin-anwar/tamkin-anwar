# imports from flask to render templates, to redirect pages and to request data
from flask import render_template, request, redirect
#import app from flask_app
from flask_app import app
#import User from flask_app.models.user
from flask_app.models.user import User

#route to redirect to /users

@app.route('/')
def index():
    return redirect('/users')

#route to render template for html and inject user data and get all class method from models.user
@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())

#route to render template for html page
@app.route('/user/new')
def new():
    return render_template("new_user.html")
#route to create and save data to database

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

#route to render template for html page and inject show data and classmethod from models.user

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=User.get_one(data))
#route to render template for html page and inject show data and classmethod from models.user

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_user.html",user=User.get_one(data))

#route to update data and to redirect to route 

@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')
#route to delete data from database

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')