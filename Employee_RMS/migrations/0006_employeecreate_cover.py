# Generated by Django 4.0.1 on 2022-03-05 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_RMS', '0005_employeeeducation1_delete_employeeeducation'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeecreate',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to='books/covers'),
        ),
    ]
