# Generated by Django 3.2.6 on 2021-08-15 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.SmallIntegerField(choices=[('EXECUTIVE', '임원'), ('MANAGEMENT_SUPPORT', '경영지원'), ('SALES_SUPPORT', '영업지원'), ('TECHNICAL_SUPPORT', '개발'), ('MARKETING', '마케팅')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='job_title',
            field=models.SmallIntegerField(choices=[('CEO', '대표이사'), ('DIRECTOR', '이사'), ('DEPUTY_MANAGER', '부장'), ('DEPUTY_GENERAL_MANAGER', '차장'), ('MANAGE', '과장'), ('ASSISTANT_MANAGER', '대리'), ('SENIOR_STAFF', '주임'), ('STAFF', '사원')]),
        ),
    ]