#! /bin/bash
IP_app1="$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' app1)"
IP_app2="$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' app2)"
IP_app3="$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' app3)"
GATEWAY="$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.Gateway}}{{end}}' con-server-ui-1)"

PORT_app1=8001
PORT_app2=8002
PORT_app3=8003


sed  "s/\$GATEWWAY/$GATEWAY/g" template/flask.json > template/flask.json.temp
sed  "s/\$IP_app1/$IP_app1/g"  template/flask.json.temp > agent1/flask.json
sed  "s/\$IP_app2/$IP_app2/g"  template/flask.json.temp > agent2/flask.json
sed  "s/\$IP_app3/$IP_app3/g"  template/flask.json.temp > agent3/flask.json
sed  "s/\$PORT/$PORT_app1/g"   agent1/flask.json > agent1/flask.json
sed  "s/\$PORT/$PORT_app2/g"   agent2/flask.json > agent2/flask.json
sed  "s/\$PORT/$PORT_app3/g"   agent3/flask.json > agent3/flask.json
rm template/flask.json.temp
