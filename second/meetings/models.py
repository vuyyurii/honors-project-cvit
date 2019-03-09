from django.db import models

class Meeting(models.Model):
    
    name = models.CharField(max_length = 30)
    tim = models.CharField(max_length = 10, default = 'time')
    transcript = models.CharField(max_length = 1000, default = 'transcript')
    words = models.CharField(max_length = 1000, default = 'words')
