# Generated by Django 4.2.7 on 2023-12-01 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collegeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('mail_id', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('purpose', models.CharField(choices=[('enquiry', 'Enquiry'), ('order', 'Place Order'), ('return', 'Return')], max_length=20)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='collegeApp.course')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='collegeApp.department')),
            ],
        ),
    ]
