# Generated by Django 5.1.7 on 2025-03-25 05:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('phone_no', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=255)),
                ('linkedln', models.URLField(max_length=255, verbose_name='LinkedIn URL')),
                ('facebook_id', models.URLField(max_length=255, verbose_name='Facebook URL')),
                ('twitter', models.URLField(max_length=255, verbose_name='Twitter URL')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('won', 'Won'), ('hot', 'Hot'), ('warm', 'Warm'), ('cold', 'Cold'), ('lost', 'Lost')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('leads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.leads')),
            ],
        ),
    ]
