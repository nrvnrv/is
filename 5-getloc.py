import http.client
import geocoder

conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
myIP = conn.getresponse().read()
g = geocoder.ip(myIP.decode())
print(g.latlng)