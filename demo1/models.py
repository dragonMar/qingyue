from django.db import models

# Create your models here.


class count(models.Model):
    database_name = models.CharField(max_length=20)
    table_name = models.CharField(max_length=20)
    tag_name = models.CharField(max_length=20)
    num = models.IntegerField(default=0)
    pub_time = models.DateTimeField()
    create_time = models.DateTimeField()


    def __unicode__(self):
        return self.table_name
