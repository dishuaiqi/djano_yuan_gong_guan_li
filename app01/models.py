from django.db import models

# Create your models here.
class DepartMent(models.Model):
    '''部门表'''
    title=models.CharField(verbose_name='部门',max_length=32)

    def __str__(self):
        return self.title

class Staff(models.Model):
    '''员工表'''
    name=models.CharField(verbose_name='姓名',max_length=32)
    password=models.CharField(verbose_name='密码',max_length=64)
    age=models.IntegerField(verbose_name='年龄')

    salary=models.DecimalField(verbose_name='工资',max_digits=8,decimal_places=2,default=10)
    work_time = models.DateField(verbose_name='入职时间')    #根据需求不同，可以设置不同的时间格式，此格式不显示时、分、秒


    '''关联表'''
    # 无约束
    # depart_id=models.BigIntegerField(verbose_name='部门ID')
    # 1.有约束
    #  to 表示与哪张表关联
    #  to_field 表示与哪一列关联
    # 2.django自动
    #     写的depart
    #       生成数据列 depart_id
    # 3.部门列表被删除
    #   3.1级联删除
    depart=models.ForeignKey(verbose_name='部门',to='DepartMent',to_field='id',on_delete=models.CASCADE)
    #   3.2置空
    # depart = models.ForeignKey(to='DepartMent', to_field='id', null=True,blank=True,on_delete=models.SET_NULL)


class Preetyphone(models.Model):
    telephone=models.CharField(max_length=32,verbose_name='手机号')
    price=models.IntegerField(verbose_name='价格',default=888)

    level_choice=(
        (1,'1级'),
        (2,'2级'),
        (3,'3级'),
        (4,'4级'),
    )


    level=models.SmallIntegerField(verbose_name='级别',choices=level_choice,default=1)

    status_choice=(
        (1,'未占用'),
        (2,'已占用'),
    )
    status=models.SmallIntegerField(verbose_name='状态',choices=status_choice,default=1)
