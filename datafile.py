from google.appengine.ext import db

class remoteSettings(db.Model):
	sampleTime  = db.IntegerProperty()
	watchdogTime = db.IntegerProperty()
	noLines = db.IntegerProperty()
	startOfDay = db.IntegerProperty()
	endOfDay = db.IntegerProperty()
