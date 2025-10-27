from django.db import models

# Create your models here.

class Donator(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    did = models.CharField(db_column='did',max_length=11)
    fname = models.TextField(db_column='fname')
    lname = models.TextField(db_column='lname')
    bloodtype = models.TextField(db_column='bloodtype')
    donation_date = models.DateTimeField("date published")
    
class BloodStock(models.Model):
    bid = models.IntegerField(db_column='bid',primary_key=True)
    op = models.IntegerField(db_column='op', default=0)
    ap = models.IntegerField(db_column='ap', default=0)
    bp = models.IntegerField(db_column='bp', default=0)
    abp = models.IntegerField(db_column='abp', default=0)
    om = models.IntegerField(db_column='om', default=0)
    am = models.IntegerField(db_column='am', default=0)
    bm = models.IntegerField(db_column='bm', default=0)
    abm = models.IntegerField(db_column='abm', default=0)
    def __str__(self):
        return "bid = " + str(self.bid)
    
class AuditTrail(models.Model):
    aid = models.IntegerField(db_column='aid',primary_key=True)
    type = models.TextField(db_column='type')
    btype = models.TextField(db_column='btype')
    qtts = models.IntegerField(db_column='qtts')
    dt = models.DateTimeField(db_column='dt')