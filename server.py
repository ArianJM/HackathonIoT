from flask import Flask
import weather
import requests
import Adafruit_DHT

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/home")
def home():
  h,t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
  return 'Temperatura:', t, 'Celsius. Humedad:', h

@app.route("/city/weather")
def city_weather():
  url_w = 'http://api.openweathermap.org'
  method_w = '/data/2.5/weather?q=Madrid,es'

  r = requests.get(url_w+method_w)
  data = r.json()
  celsius = data['main']['temp'] - 273.15
  ret = data['name']+' '+str(celsius)+'C ' + data['weather'][0]['description']
  return ret

@app.route("/city/events")
def city_events():
  url_art = 'http://api.artsholland.com'
  method_art = '/rest/event.json?locality=amsterdam'

  r = requests.get(url_art+method_art)
  data = r.json()
  events = ''
  for res in data['results']:
    if 'description' in res.keys():
      events += 'Evento:'+res['description']+'\n'
      events += 'Inicio:'+res['hasBeginning']+'\n'
      events += 'Fin:'+res['hasEnd']+'\n\n'
  
  return events

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=True)

