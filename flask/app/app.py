from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
global_counter = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
my_counter = Redis(host="redis", db=1, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

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
    app.run(host='0.0.0.0', port=80)
