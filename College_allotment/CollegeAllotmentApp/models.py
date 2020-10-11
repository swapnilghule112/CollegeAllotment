from django.db import models


class UserData(models.Model):
    CMPN = models.IntegerField(default = 0)
    INFT = models.IntegerField(default = 0)
    EXTC = models.IntegerField(default = 0)
    ETRX = models.IntegerField(default = 0)
    BIOMED = models.IntegerField(default = 0)
    student_data = models.FileField()