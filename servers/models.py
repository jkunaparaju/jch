from django.db import models

# Create your models here.

from django.core.urlresolvers import reverse
class Mem(models.Model):
    mem_id = models.IntegerField(primary_key=True)
    mem_name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    def __str__(self):
        return self.mem_name

    class Meta:
        managed = False
        db_table = 'mem'

class Server(models.Model):
    name = models.CharField(max_length=200)
    ip = models.GenericIPAddressField()
    order = models.IntegerField()
    mem = models.ForeignKey(Mem, models.DO_NOTHING, blank=True, null=True)
    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'servers_server'



    def get_absolute_url(self):
        return reverse('server_edit', kwargs={'pk': self.pk})