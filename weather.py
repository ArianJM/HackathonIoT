import httplib, json, urllib
import requests

def getWheather(city='Madrid,es'):
  url_w = 'api.openweathermap.org'
  method_w = '/data/2.5/weather?q='+city

  conn_w = httplib.HTTPConnection(url_w)
  conn_w.request('GET', method_w)

  response_w = conn_w.getresponse()
  print 'Weather status:', response_w.status, response_w.reason

  data_JSON = response_w.read()

  data_w = json.loads(data_JSON)
  #print data_JSON
  celsius = data_w['main']['temp'] - 273.15

def getHollandArt():
  url_art = 'api.artsholland.com'
  method_art = '/rest/event.json?locality=amsterdam'

  conn_art = httplib.HTTPConnection(url_art)
  conn_art.request('GET', method_art)

  resp_art = conn_art.getresponse()
  print 'Art status:', resp_art.status, resp_art.reason

  print data_w['name'], celsius, 'Celsius', data_w['weather'][0]['description']


def emt():
  headers = {'content-type': 'application/json',
            'idClient': 'WEB.SERV.arianjm@gmail.com',
            'passKey': 'E5978EEB-67BA-4FEB-9532-B866DBB4F579'}
  url = 'https://openbus.emtmadrid.es:9443/emt-proxy-server/last/'
  method = '/bus/GetListLines.php'
  params = {#'idClient': 'WEB.SERV.arianjm@gmail.com',
            #'passKey': 'E5978EEB-67BA-4FEB-9532-B866DBB4F579',
            'SelectDate': '28/11/2014'}
#  data = {'idClient': 'WEB.SERV.arianjm@gmail.com', 'passKey': 'E5978EEB-67BA-4FEB-9532-B866DBB4F579'}
#  params = urllib.urlencode(

  r = requests.post(url+method, params=params, headers=headers, verify=False)

  print r.text

emt()
