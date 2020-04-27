# Generated by Django 2.2.11 on 2020-04-24 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='课程号')),
                ('course_name', models.CharField(max_length=20, verbose_name='课程名')),
                ('course_status', models.CharField(max_length=20, verbose_name='课程状态')),
                ('course_college', models.CharField(max_length=20, verbose_name='开课学院')),
                ('course_pre_id', models.CharField(max_length=20, verbose_name='先修课程号')),
                ('course_pre_name', models.CharField(max_length=20, verbose_name='先修课程名')),
                ('course_introduction', models.CharField(max_length=1000, verbose_name='课程介绍')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('notice_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='通知号')),
                ('notice_send_time', models.DateTimeField(verbose_name='发送日期')),
                ('notice_content', models.CharField(max_length=1000, verbose_name='通知内容')),
                ('notice_title', models.CharField(max_length=255, verbose_name='通知标题')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='学号')),
                ('student_name', models.CharField(max_length=20, verbose_name='姓名')),
                ('student_age', models.CharField(max_length=20, verbose_name='年龄')),
                ('student_sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=20, verbose_name='性别')),
                ('student_nation', models.CharField(default='汉', max_length=20, verbose_name='民族')),
                ('student_political_status', models.CharField(max_length=20, verbose_name='政治面貌')),
                ('student_come_year', models.DateTimeField(verbose_name='入学日期')),
                ('student_college', models.CharField(max_length=20, verbose_name='学院')),
                ('student_major', models.CharField(max_length=20, verbose_name='专业')),
                ('student_class', models.CharField(max_length=20, verbose_name='班级')),
                ('student_province', models.CharField(max_length=20, verbose_name='省份')),
                ('student_city', models.CharField(max_length=20, verbose_name='城市')),
                ('student_birthday', models.DateTimeField(verbose_name='出生日期')),
                ('student_phone', models.CharField(max_length=20, verbose_name='手机号码')),
                ('student_qq', models.CharField(max_length=20, verbose_name='QQ号码')),
                ('student_wechat', models.CharField(max_length=20, verbose_name='微信号码')),
                ('student_email', models.EmailField(max_length=254, verbose_name='邮件地址')),
                ('student_high_school', models.CharField(max_length=20, verbose_name='毕业高中')),
                ('student_foreign_language', models.CharField(max_length=20, verbose_name='外语')),
                ('student_status', models.CharField(max_length=20, verbose_name='状态')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='工号')),
                ('teacher_name', models.CharField(max_length=20, verbose_name='姓名')),
                ('teacher_age', models.CharField(max_length=20, verbose_name='年龄')),
                ('teacher_sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=20, verbose_name='性别')),
                ('teacher_nation', models.CharField(max_length=20, verbose_name='民族')),
                ('teacher_political_status', models.CharField(max_length=20, verbose_name='政治面貌')),
                ('teacher_department', models.CharField(max_length=20, verbose_name='部门')),
                ('teacher_academic_title', models.CharField(max_length=20, verbose_name='职称')),
                ('teacher_degree', models.CharField(max_length=20, verbose_name='学位')),
                ('teacher_come_year', models.DateTimeField(verbose_name='入职日期')),
                ('teacher_province', models.CharField(max_length=20, verbose_name='省份')),
                ('teacher_city', models.CharField(max_length=20, verbose_name='城市')),
                ('teacher_birthday', models.DateTimeField(verbose_name='出生日期')),
                ('teacher_phone', models.CharField(max_length=20, verbose_name='手机号码')),
                ('teacher_qq', models.CharField(max_length=20, verbose_name='QQ号码')),
                ('teacher_wechat', models.CharField(max_length=20, verbose_name='微信号码')),
                ('teacher_email', models.EmailField(max_length=254, verbose_name='邮件地址')),
                ('student_graduate_school', models.CharField(max_length=20, verbose_name='毕业院校')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=20, verbose_name='账号')),
                ('identity', models.CharField(choices=[('student', '学生'), ('teacher', '教师')], default='学生', max_length=20, verbose_name='身份')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
            options={
                'unique_together': {('account', 'identity')},
            },
        ),
        migrations.CreateModel(
            name='SchoolTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_year', models.CharField(max_length=20, verbose_name='开始年份')),
                ('end_year', models.CharField(max_length=20, verbose_name='结束年份')),
                ('number', models.IntegerField(verbose_name='学期号')),
            ],
            options={
                'unique_together': {('begin_year', 'end_year', 'number')},
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='消息号')),
                ('message_content', models.CharField(max_length=1000, verbose_name='消息内容')),
                ('message_send_time', models.DateTimeField(verbose_name='发送日期')),
                ('message_status', models.CharField(max_length=20, verbose_name='消息状态')),
                ('message_title', models.CharField(max_length=255, verbose_name='消息标题')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student', verbose_name='学号')),
            ],
        ),
        migrations.CreateModel(
            name='SelectList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=20, verbose_name='专业')),
                ('term', models.CharField(max_length=20, verbose_name='学期')),
                ('status', models.CharField(max_length=20, verbose_name='状态')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Course', verbose_name='课程号')),
            ],
            options={
                'unique_together': {('major', 'term')},
            },
        ),
        migrations.CreateModel(
            name='SelectCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=20, verbose_name='学期')),
                ('student_grade', models.CharField(max_length=20, verbose_name='成绩')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Course', verbose_name='课程号')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student', verbose_name='学号')),
            ],
            options={
                'unique_together': {('student_id', 'term', 'course_id')},
            },
        ),
        migrations.CreateModel(
            name='CourseArrangement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=20, verbose_name='学期')),
                ('week_begin', models.IntegerField(verbose_name='开课周')),
                ('week_end', models.IntegerField(verbose_name='结课周')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Course', verbose_name='课程号')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Teacher', verbose_name='工号')),
            ],
            options={
                'unique_together': {('course_id', 'term', 'teacher_id')},
            },
        ),
    ]
