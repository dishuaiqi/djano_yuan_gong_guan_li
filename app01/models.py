from django.db import models

# Create your models here.
'''创建登录表'''
class Admin(models.Model):
    Username=models.CharField(verbose_name='用户名',max_length=32)
    password=models.CharField(verbose_name='密码',max_length=64)



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


class Task(models.Model):
    '''任务管理'''
    leavel_choice=(
        (1,'紧急'),
        (2,'重要'),
        (3,'临时'),
    )
    lavel=models.SmallIntegerField(verbose_name='级别',choices=leavel_choice,default=1)
    title=models.CharField(verbose_name='标题',max_length=64)
    detail=models.TextField(verbose_name='内容详情')
    user=models.ForeignKey(verbose_name='负责人',to='Admin',on_delete=models.CASCADE)


class Order(models.Model):
    '''订单管理'''

    order_number=models.CharField(verbose_name='订单号',max_length=64)
    title=models.CharField(verbose_name='商品名称',max_length=64)
    price=models.IntegerField(verbose_name='价格')
    status_choices=(
        (1,'待支付'),
        (2,'已支付'),
    )
    status=models.SmallIntegerField(verbose_name='状态',choices=status_choices,default=1)
    admin=models.ForeignKey(verbose_name='管理员',to='Admin',on_delete=models.CASCADE)

class City(models.Model):
    '''城市'''
    name=models.CharField(verbose_name='名称',max_length=64)
    count=models.IntegerField(verbose_name='人口')
    img=models.FileField(verbose_name='logo',max_length=128,upload_to='city')# 存放的还是路劲，可以把文件上传到media问价夹中国通某个文件


