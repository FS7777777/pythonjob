from django.db import models

# Create your models here.
#public user detail
class T_User_Detail(models.Model):
    f_id = models.AutoField(primary_key=True)
    #用户积分
    f_score = models.IntegerField()
    #昵称
    f_nickname = models.CharField(max_length=20)
    #sex
    f_sex = models.SmallIntegerField()
    #phone
    f_phone = models.CharField(max_length=11)
    #role 普通客户
    f_role = models.IntegerField()
    #备注
    f_description = models.CharField(max_length=200)

# user lesson
class T_User_Lesson(models.Model):
    #id
    f_id = models.AutoField(primary_key=True)
    #用户id
    f_user_id = models.IntegerField()
    #课程id
    f_lesson_id = models.IntegerField()
    #实际缴纳金额
    f_payment = models.DecimalField()
    #课程完成情况
    f_finish_result = models.FloatField()