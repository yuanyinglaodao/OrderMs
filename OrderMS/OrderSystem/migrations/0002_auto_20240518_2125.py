# Generated by Django 3.2.17 on 2024-05-18 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrderSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'verbose_name': '菜品信息表', 'verbose_name_plural': '菜品信息表'},
        ),
        migrations.AlterModelOptions(
            name='foodtype',
            options={'verbose_name': '菜品类型表', 'verbose_name_plural': '菜品类型表'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '订单信息表', 'verbose_name_plural': '订单信息表'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': '订单状态表', 'verbose_name_plural': '订单状态表'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': '员工信息表', 'verbose_name_plural': '员工信息表'},
        ),
        migrations.AlterModelOptions(
            name='staff_table',
            options={'verbose_name': '餐桌信息表', 'verbose_name_plural': '餐桌信息表'},
        ),
        migrations.AlterField(
            model_name='food',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='剩余数量'),
        ),
        migrations.AlterField(
            model_name='food',
            name='cost_time',
            field=models.IntegerField(default=0, verbose_name='制作时间'),
        ),
        migrations.AlterField(
            model_name='food',
            name='foodType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='OrderSystem.foodtype', verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='food',
            name='price',
            field=models.FloatField(default=0, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='food',
            name='title',
            field=models.CharField(max_length=20, verbose_name='菜品名称'),
        ),
        migrations.AlterField(
            model_name='foodtype',
            name='name',
            field=models.CharField(max_length=20, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.CharField(default='', max_length=50, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='food_amount',
            field=models.IntegerField(default=0, verbose_name='菜品总数'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_pay',
            field=models.BooleanField(default=False, verbose_name='是否支付'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay_time',
            field=models.DateTimeField(null=True, verbose_name='支付时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OrderSystem.staff', verbose_name='员工'),
        ),
        migrations.AlterField(
            model_name='order',
            name='table_id',
            field=models.IntegerField(default=0, verbose_name='桌号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0, verbose_name='总价'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='comment',
            field=models.CharField(max_length=50, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='end_cook_time',
            field=models.TimeField(null=True, verbose_name='制作结束时间'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='foodID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OrderSystem.food', verbose_name='菜品'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='orderID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OrderSystem.order', verbose_name='订单'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='start_cook_time',
            field=models.TimeField(null=True, verbose_name='开始制作时间'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.IntegerField(choices=[(0, '后厨未接单'), (1, '后厨在准备'), (2, '等待上菜'), (3, '上菜完成')], default=0, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='sum_price',
            field=models.FloatField(default=0, verbose_name='总价'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address',
            field=models.CharField(default='', max_length=50, verbose_name='住址'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='born_date',
            field=models.DateField(null=True, verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='citizenID',
            field=models.CharField(max_length=20, verbose_name='证件号码'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=20, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=10, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='电话号码'),
        ),
        migrations.AlterField(
            model_name='staff_table',
            name='name',
            field=models.CharField(max_length=20, verbose_name='桌名'),
        ),
        migrations.AlterField(
            model_name='staff_table',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='OrderSystem.staff', verbose_name='负责员工'),
        ),
        migrations.CreateModel(
            name='OrderHotFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='数量')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OrderSystem.food', verbose_name='菜品')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OrderSystem.order', verbose_name='订单')),
            ],
            options={
                'verbose_name': '订单项',
                'verbose_name_plural': '订单项',
            },
        ),
    ]