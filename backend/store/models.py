from django.db import models

# Create your models here.
class T_Stores(models.Model):
    f_id = models.AutoField(primary_key=True)
    #门店名称id
    f_name = models.CharField(max_length=100)
    #坐标
    f_coordinate = models.CharField(max_length=100)
    #位置说明
    f_local = models.CharField(max_length=100)
    #拥有者
    f_owner = models.CharField(max_length=32)
    #联系方式
    f_phone = models.CharField(max_length=11)
    #门店简介
    f_description = models.TextField()

class T_Teacher(models.Model):
    f_id = models.AutoField(primary_key=True)
    #老师名称
    f_name = models.CharField(max_length=100)
    #老师评分
    f_score = models.IntegerField()
    #入职时间
    f_create_time = models.DateTimeField()
    #个人说明
    f_description = models.CharField(max_length=200)

class T_Lesson(object):
    f_id = models.AutoField(primary_key=True)
    #所属场馆
    f_store_id =models.IntegerField()
    #所属老师
    f_teacher_id =models.IntegerField()
    #课程名称
    f_name = models.CharField(max_length=100)
    #开始时间
    f_start_time = models.DateTimeField()
    #结束时间
    f_end_time = models.DateTimeField()
    #课程容纳人数
    
    #报名人数

    #是否过期

    #课程简介
    f_description = models.CharField(max_length=200)