# Generated by Django 2.2.11 on 2020-05-11 01:35

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
                ('course_id', models.CharField(db_index=True, max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='课程号')),
                ('course_name', models.CharField(max_length=20, unique=True, verbose_name='课程名')),
                ('course_status', models.CharField(default='未开', max_length=20, verbose_name='课程状态')),
                ('course_college', models.CharField(default='信息科学与技术学院', max_length=20, verbose_name='开课学院')),
                ('course_pre_id', models.CharField(max_length=20, null=True, verbose_name='先修课程号')),
                ('course_pre_name', models.CharField(max_length=20, null=True, verbose_name='先修课程名')),
                ('course_introduction', models.CharField(max_length=1000, verbose_name='课程介绍')),
                ('course_scale', models.CharField(max_length=20, verbose_name='平时成绩比例')),
                ('course_volume', models.CharField(max_length=20, verbose_name='课程容量')),
            ],
            options={
                'verbose_name': '课程信息表',
                'verbose_name_plural': '课程信息表',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('notice_id', models.AutoField(primary_key=True, serialize=False)),
                ('notice_send_time', models.DateTimeField(auto_now_add=True, verbose_name='发送日期')),
                ('notice_content', models.CharField(max_length=1000, verbose_name='通知内容')),
                ('notice_title', models.CharField(max_length=255, verbose_name='通知标题')),
            ],
            options={
                'verbose_name': '公告表',
                'verbose_name_plural': '公告表',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(db_index=True, max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='学号')),
                ('student_name', models.CharField(max_length=20, null=True, verbose_name='姓名')),
                ('student_age', models.PositiveSmallIntegerField(null=True, verbose_name='年龄')),
                ('student_sex', models.CharField(default='男', max_length=20, null=True, verbose_name='性别')),
                ('student_nation', models.CharField(default='汉族', max_length=20, null=True, verbose_name='民族')),
                ('student_political_status', models.CharField(default='群众', max_length=20, null=True, verbose_name='政治面貌')),
                ('student_come_year', models.CharField(max_length=40, null=True, verbose_name='入学日期')),
                ('student_college', models.CharField(default='信息科学与技术学院', max_length=20, null=True, verbose_name='学院')),
                ('student_major', models.CharField(max_length=20, null=True, verbose_name='专业')),
                ('student_class', models.CharField(max_length=20, null=True, verbose_name='班级')),
                ('student_province', models.CharField(max_length=20, null=True, verbose_name='省份')),
                ('student_city', models.CharField(max_length=20, null=True, verbose_name='城市')),
                ('student_birthday', models.CharField(max_length=40, null=True, verbose_name='出生日期')),
                ('student_qq', models.CharField(max_length=20, null=True, verbose_name='QQ号码')),
                ('student_wechat', models.CharField(max_length=20, null=True, verbose_name='微信号码')),
                ('student_high_school', models.CharField(max_length=20, null=True, verbose_name='毕业高中')),
                ('student_foreign_language', models.CharField(default='英语', max_length=20, null=True, verbose_name='外语')),
                ('student_status', models.CharField(default='在读', max_length=20, null=True, verbose_name='状态')),
            ],
            options={
                'verbose_name': '学生信息表',
                'verbose_name_plural': '学生信息表',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.CharField(db_index=True, max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='工号')),
                ('teacher_name', models.CharField(max_length=20, null=True, verbose_name='姓名')),
                ('teacher_age', models.PositiveSmallIntegerField(null=True, verbose_name='年龄')),
                ('teacher_sex', models.CharField(default='男', max_length=20, null=True, verbose_name='性别')),
                ('teacher_nation', models.CharField(default='汉族', max_length=20, null=True, verbose_name='民族')),
                ('teacher_political_status', models.CharField(default='群众', max_length=20, null=True, verbose_name='政治面貌')),
                ('teacher_department', models.CharField(default='信息科学与技术学院', max_length=20, null=True, verbose_name='学院')),
                ('teacher_academic_title', models.CharField(default='教授', max_length=20, null=True, verbose_name='职称')),
                ('teacher_degree', models.CharField(default='学士', max_length=20, null=True, verbose_name='学位')),
                ('teacher_come_year', models.CharField(max_length=80, null=True, verbose_name='入职日期')),
                ('teacher_province', models.CharField(max_length=20, null=True, verbose_name='省份')),
                ('teacher_city', models.CharField(max_length=20, null=True, verbose_name='城市')),
                ('teacher_birthday', models.CharField(max_length=255, null=True, verbose_name='出生日期')),
                ('teacher_qq', models.CharField(max_length=20, null=True, verbose_name='QQ号码')),
                ('teacher_wechat', models.CharField(max_length=20, null=True, verbose_name='微信号码')),
                ('teacher_graduate_school', models.CharField(max_length=20, null=True, verbose_name='毕业院校')),
            ],
            options={
                'verbose_name': '教师信息表',
                'verbose_name_plural': '教师信息表',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=20, verbose_name='账号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('identity', models.CharField(default='学生', max_length=20, verbose_name='身份')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='手机号码')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮件地址')),
            ],
            options={
                'verbose_name': '用户登录表',
                'verbose_name_plural': '用户登录表',
                'unique_together': {('account', 'identity')},
            },
        ),
        migrations.CreateModel(
            name='SelectCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=20, verbose_name='学期')),
                ('student_usual_grade', models.CharField(max_length=20, verbose_name='平时成绩')),
                ('student_final_grade', models.CharField(max_length=20, verbose_name='期末成绩')),
                ('student_total_grade', models.CharField(max_length=20, verbose_name='总评成绩')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Course', verbose_name='课程号')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Student', verbose_name='学号')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Teacher', verbose_name='工号')),
            ],
            options={
                'verbose_name': '选课表',
                'verbose_name_plural': '选课表',
                'unique_together': {('student_id', 'term', 'course_id', 'teacher_id')},
            },
        ),
        migrations.CreateModel(
            name='CourseArrangement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=20, verbose_name='学期')),
                ('week', models.CharField(max_length=20, verbose_name='周次')),
                ('session', models.CharField(max_length=20, verbose_name='节次')),
                ('location', models.CharField(max_length=20, verbose_name='地点')),
                ('weekday', models.CharField(max_length=20, verbose_name='上课日期')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Course', verbose_name='课程号')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Teacher', verbose_name='工号')),
            ],
            options={
                'verbose_name': '课程安排表',
                'verbose_name_plural': '课程安排表',
                'unique_together': {('course_id', 'term', 'teacher_id')},
            },
        ),
    ]
