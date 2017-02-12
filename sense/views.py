import json
from time import strftime
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Measurement

################################################## POST sensor data
@csrf_exempt 
@require_http_methods(["POST"])
def measure(request):
    print(request.POST)
    print(request.body)
    # With JSON version
    R = ""
    if type(request.body) == type(b""):
        R = json.loads(request.body.decode("utf-8"), encoding="utf-8")
    else:
        R = json.loads(request.body)

    print("DEBUG --- Received measure POST request: "+str(R))
    #M = Measurement(uid = uid, packettime = A.packettime, node = A.node, sensors=A.sensors)

    # --- Converting the date
    packettime = datetime.fromtimestamp(float(R["packettime"])/1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
    print("DEBUG ---- packettime "+packettime)

    # --- Saving in database 
    M = Measurement(packettime = packettime, node = R["node"], sensor_name=R["sensors"][0]["name"], sensor_value=R["sensors"][0]["value"])
    b = M.save()

    print("DEBUG --- saved in DB: "+str(b))
    return HttpResponse("Every thing is alright")

##################################################
def test(request):
    A = {"key":[2.3,2.4,1.0,{"status":"test not yet ready"}]}
    return HttpResponse(json.dumps(A, sort_keys=True, indent=4))

################################################## GET sensor data
@csrf_exempt 
@require_http_methods(["GET"])
def node_period(request, node_id):

    #M = Measurement.objects.filter(packettime__gt=d1, packettime__lt=d2)
    #data = serializers.serialize('json', M, fields=())
    #return HttpResponse(json.dumps(A, sort_keys=True, indent=4))
    return HttpResponse("Nothing here yet")
