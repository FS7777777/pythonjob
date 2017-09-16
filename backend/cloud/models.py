from django.db import models

# Create your models here.
class T_Cloud_Stores(models.Model):
    f_id = models.AutoField(primary_key=True)
    #门店名称id
    f_store_id = models.IntegerField()
    #是否停用
    f_if_enable = models.BooleanField(default=False)
    #签约时间
    f_create_time = models.DateTimeField()
    #签约人
    f_contractor = models.CharField(max_length=20)
    #说明
    f_description = models.CharField(max_length=200)