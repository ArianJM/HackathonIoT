from flask import Flask
import requests
import picamera
import Adafruit_DHT

app = Flask(__name__, static_url_path = 'tmp', static_folder='tmp')

@app.route("/")
def hello():
  index = '<a href=/home>Home</a><br><a href="/city">City</a>'
  return index

@app.route("/home")
def home():
  h,t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
  return 'Temperatura:'+str(round(t))+' Celsius.\nHumedad:'+str(round(h))

@app.route("/home/pic")
def pic():
  with picamera.PiCamera() as camera:
    camera.capture('tmp/image.png')
  return 'tmp/image.png'
  

@app.route("/city")
def city():
  city = '<a href=/city/weather>Weather</a></br><a href="/city/events">Events</a>'
  return city

@app.route("/city/weather")
def city_weather():
  url_w = 'http://api.openweathermap.org'
  method_w = '/data/2.5/weather?q=Madrid,es'

  r = requests.get(url_w+method_w)
  data = r.json()
  celsius = data['main']['temp'] - 273.15
  ret = '<h3>'+data['name']+'</h3>'
  ret+= '<b>Temperatura: </b>'+str(celsius)+'C'
  ret+= 'Minimo: '+data['main']['temp_min']
  ret+= 'Maximo: '+data['main']['temp_max']+'<br>'
  ret+= '<b>Temporal: </b>'+data['weather'][0]['description']+'<br>'
  ret+= '<b>Humedad: </b>'+data['main']['humidity']+'<br>'
  ret+= '<b>Viento: </b>'+data['wind']['speed']+'Km/h'
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
      events += '<h3>Evento</h3>'+res['description']+'<br>'
      events += '<b>Inicio:</b>'+res['hasBeginning']+'<br>'
      events += '<b>Fin:</b>'+res['hasEnd']+'<br><br>'
  
  return events

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=True)

