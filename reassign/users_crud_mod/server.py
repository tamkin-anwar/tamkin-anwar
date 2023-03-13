#import app from flask_app
from flask_app import app
#import users from flask_app.controllers
from flask_app.controllers import users







#for dev debugging
if __name__=="__main__":
    app.run(debug=True)