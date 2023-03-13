#importing the app from flask_app
from flask_app import app
#importing dojos and ninjas 
from flask_app.controllers import dojos, ninjas


#for dev debug app
if __name__=="__main__":
	app.run(debug=True)