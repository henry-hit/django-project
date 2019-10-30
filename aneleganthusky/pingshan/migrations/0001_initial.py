# Generated by Django 2.2.5 on 2019-10-30 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('REC_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('REPORT_NUM', models.IntegerField(blank=True, null=True)),
                ('CREATE_TIME', models.DateTimeField(blank=True, null=True)),
                ('DISTRICT_NAME', models.CharField(blank=True, max_length=20)),
                ('DISTRICT_ID', models.IntegerField(blank=True, null=True)),
                ('STREET_NAME', models.CharField(blank=True, max_length=20)),
                ('STREET_ID', models.IntegerField(blank=True, null=True)),
                ('COMMUNITY_NAME', models.CharField(blank=True, max_length=20)),
                ('COMMUNITY_ID', models.IntegerField(blank=True, null=True)),
                ('EVENT_TYPE_NAME', models.CharField(blank=True, max_length=20)),
                ('EVENT_TYPE_ID', models.IntegerField(blank=True, null=True)),
                ('MAIN_TYPE_NAME', models.CharField(blank=True, max_length=20)),
                ('MAIN_TYPE_ID', models.IntegerField(blank=True, null=True)),
                ('SUB_TYPE_NAME', models.CharField(blank=True, max_length=40)),
                ('SUB_TYPE_ID', models.IntegerField(blank=True, null=True)),
                ('DISPOSE_UNIT_NAME', models.CharField(blank=True, max_length=40)),
                ('DISPOSE_UNIT_ID', models.IntegerField(blank=True, null=True)),
                ('EVENT_SRC_NAME', models.CharField(blank=True, max_length=20)),
                ('EVENT_SRC_ID', models.IntegerField(blank=True, null=True)),
                ('OPERATE_NUM', models.BooleanField(blank=True, null=True)),
                ('OVERTIME_ARCHIVE_NUM', models.BooleanField(blank=True, null=True)),
                ('INTIME_TO_ARCHIVE_NUM', models.BooleanField(blank=True, null=True)),
                ('INTIME_ARCHIVE_NUM', models.BooleanField(blank=True, null=True)),
                ('EVENT_PROPERTY_ID', models.IntegerField(blank=True, null=True)),
                ('EVENT_PROPERTY_NAME', models.CharField(blank=True, max_length=20)),
                ('OCCUR_PLACE', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]