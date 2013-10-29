import webapp2
import cgi
from datafile import remoteSettings
 
MAIN_PAGE_HTML = """\
<html>
  <body style=background-color:#6495ed;>
    <h1> Datalogger 2013 </h1>
 
  <form name="input" action="/Parameters" method="post">
    <fieldset>
      <legend>Remote Variables:</legend>
      Sample Time: <input type="text" name="SampleTime" size="30"><br>
      Watchdog Time: <input type="text" name="WatchdogTime" size="30"><br>
      Number of lines: <input type="text" name="nolines" size="30"><br>
      Start of day (hours): <input type="text"  name="startDay" size="30"><br>
      End of day: <input type="text" name="endDay" size="10">
    </fieldset>
    <input type="submit" value="Submit">
  </form>
 
  <body>
</html>
"""
 
MAIN_PAGE_CSS = """\
 
<!DOCTYPE html>
<html>
 <head>
  <style>
  div
  {
   background-color:#ffffff;
  }
 
  p
  {
   background-color:#e0ffff;
  }
  </style>
 </head>
 
 <body>
 
   <div>
    <p > This is a paragraph</p>
   </div>
   
 
 </body>
</html>
"""
 
 
class MainPage(webapp2.RequestHandler):
 
  def get(self):
    self.response.write(MAIN_PAGE_CSS)
 
 
 
class sensorParameters(webapp2.RequestHandler):
 
  def get(self):
    self.response.write(MAIN_PAGE_HTML)
 
  def post(self):
    self.response.write('<html><body>You wrote:<pre>')
    self.response.write('Remote Variables are:<br>')
    sampleTime = cgi.escape(self.request.get('SampleTime', '0'))
    watchdogTime = cgi.escape(self.request.get('WatchdogTime', '0'))
    noLines = cgi.escape(self.request.get('nolines', '0'))
    startOfDay = cgi.escape(self.request.get('startDay', '0'))
    self.response.write( sampleTime + '<br>')
    self.response.write( watchdogTime + '<br>')
    self.response.write( noLines + '<br>')
    self.response.write( startOfDay + '<br>')
    self.response.write( '<br>')
    self.response.write('</pre></body></html>')
 
 
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/Parameters', sensorParameters),
], debug=True)
 
def main():
    run_wsgi_app(application)
  
if __name__ == '__main__':
  main()
