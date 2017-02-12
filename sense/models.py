from django.db import models
#from django.contrib.auth.models import User

#--- All measurements 
class Measurement(models.Model):
    #user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    node       = models.IntegerField(default=0)
    packettime = models.DateTimeField("Packet time", default='2016-01-01 00:00:00.000Z')
    #sensor_count = models.TextField(default="")
    sensor_name  = models.TextField(default="")
    sensor_value = models.FloatField(default=0.0)
    def __str__(self):
        return "Data [node-"+str(node)+": "+str(self.packettime)+"]"

