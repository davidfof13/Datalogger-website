from google.appengine.ext import db

class remoteSettings(db.Model):
	sampleTime  = db.IntegerProperty()
	watchdogTime = db.IntegerProperty()
	noLines = db.IntegerProperty()
	startOfDay = db.IntegerProperty()
	endOfDay = db.IntegerProperty()
    
class electricalValues(db.Model):
    v = db.IntegerProperty()
    i = db.IntegerProperty()
    tdate = db.DateTimeProperty(auto_now_add=False)
