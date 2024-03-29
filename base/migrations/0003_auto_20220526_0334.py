# Generated by Django 3.2.6 on 2022-05-26 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_task_complete_user_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_detail',
            name='level',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='exp',
            field=models.IntegerField(blank=True, choices=[(10, 'Easy'), (20, 'Average'), (40, 'Complex'), (50, 'BOSS')], default=10, null=True),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='difficulty',
            field=models.IntegerField(default=200),
        ),
    ]
