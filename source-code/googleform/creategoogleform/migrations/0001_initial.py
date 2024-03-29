# Generated by Django 2.1.7 on 2019-10-08 07:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkillModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='creategoogleform.BaseModel')),
                ('skill', models.TextField(blank=True, max_length=100)),
            ],
            bases=('creategoogleform.basemodel',),
        ),
        migrations.CreateModel(
            name='UserDetailModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='creategoogleform.BaseModel')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=20, null=True, unique=True)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creategoogleform.SkillModel')),
            ],
            bases=('creategoogleform.basemodel',),
        ),
    ]
