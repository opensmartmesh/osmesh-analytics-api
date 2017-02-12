#R=[ \
#	"{node:4;packettime:1485652290;sensors{}",\
#	"{node:4;packettime:1485652290;sensors{}"\
#]

#curl -sS -D - -X OPTIONS -d @/tmp/wwwfff http://127.0.0.1:8000/api/login --header "Content-Type:application/json"
#curl -X POST --data 

curl -sS -D - -X POST --data \
 '{"node":4,"packettime":1486904016,"sensors":[{"name":"temperature", "value":24.3}]}'\
 http://127.0.0.1:8000/sense/\
 --header "Content-Type:application/json"

###curl -sS -D - -X POST --data \
### '{node:4;packettime:1485652290;sensors:[{"name":"temperature", "value":24.3}]}'\
### http://127.0.0.1:8000/sense/\
### --header "Content-Type:application/json"
#
echo "-------------------"
