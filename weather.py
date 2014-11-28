import json
import requests
import Adafruit_DHT

def getInsideWeather():
  return Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)

def getOutsideWeather(city='Madrid,es'):
  url_w = 'http://api.openweathermap.org'
  method_w = '/data/2.5/weather?q='+city

  r = requests.get(url_w+method_w)
  data = r.json()
  celsius = data['main']['temp'] - 273.15
  print data['name'], celsius, 'Celsius', data['weather'][0]['description']

def getHollandArt():
  url_art = 'http://api.artsholland.com'
  method_art = '/rest/event.json?locality=amsterdam'

  r = requests.get(url_art+method_art)
  data = r.json()
  for res in data['results']:
    if 'description' in res.keys():
      print 'Evento:', res['description']
      print 'Inicio:', res['hasBeginning']
      print 'Fin:', res['hasEnd']



def emt():
  headers = {'content-type': 'application/json'}
            #'idClient': 'WEB.SERV.arianjm@gmail.com',
            #'passKey': 'E5978EEB-67BA-4FEB-9532-B866DBB4F579'}
  url = 'https://openbus.emtmadrid.es:9443/emt-proxy-server/last/'
  method = 'bus/GetListLines.php'
  params = {#'idClient': 'WEB.SERV.arianjm@gmail.com',
            #'passKey': 'E5978EEB-67BA-4FEB-9532-B866DBB4F579',
            'SelectDate': '28/11/2014'}
  data = {'idClient': 'WEB.SERV.arianjm@gmail.com', 'passKey': 'E5978EEB-67BA-4FEB-9532-B866DBB4F579'}
#  params = urllib.urlencode(

  r = requests.post(url+method, data=data, params=params, headers=headers, verify=False)

  print r.text


while True:
  getInsideWeather()
  getOutsideWeather()
  getHollandArt()
  time.sleep(15)
