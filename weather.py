import json
import requests
#import Adafruit_DHT
import time

def getInsideWeather():
  h,t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
  return 'Temperatura:', t, 'Celsius. Humedad:', h

def getOutsideWeather(city='Madrid,es'):
  url_w = 'http://api.openweathermap.org'
  method_w = '/data/2.5/weather?q='+city

  r = requests.get(url_w+method_w)
  data = r.json()
  celsius = data['main']['temp'] - 273.15
  return data['name'], celsius, 'Celsius', data['weather'][0]['description']

def getAmsterdamArt():
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

while True:
  print getInsideWeather()
  print getOutsideWeather()
  print getAmsterdamArt()
  time.sleep(60)
