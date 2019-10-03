from flask import Flask
from redis import Redis, RedisError
import consul
import os
import socket

# Connect to Redis
global_counter = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
my_counter = Redis(host="redis", db=1, socket_connect_timeout=2, socket_timeout=2)

# Prepare for consul
c = consul.Consul(host='172.27.0.1', port='8500')

app = Flask(__name__)

@app.route("/offline/")
def offline():
    hostname=socket.gethostname()
    html = c.kv.put(hostname, 'maintenance')
    return html.format()

@app.route("/online/")
def online():
    hostname=socket.gethostname()
    html = c.kv.put( hostname, 'ok')
    return html.format()

@app.route("/health/")
def health():
    index = None
    hostname=socket.gethostname()
    index, data = c.kv.get(hostname, index=index)
    if hostname == str(data['Value'])[2:-1]:
        html = "maintenance"
        code = 503
    else:
        html = "ok"
        code = 200
    return html.format(), code

@app.route("/")
def hello():
    hostname=socket.gethostname()
    try:
        visits = global_counter.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    try:
        my_visits = my_counter.incr(hostname)
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Host visits: </b> {my_visits} <br/>" \
           "<b>Global visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=hostname, visits=visits, my_visits=my_visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
