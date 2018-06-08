# Generated by Django 2.0.6 on 2018-06-08 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('applicationid', models.CharField(db_column='ApplicationID', max_length=16, primary_key=True, serialize=False)),
                ('first_name', models.CharField(db_column='FirstName', max_length=45)),
                ('last_name', models.CharField(db_column='LastName', max_length=45)),
                ('email', models.CharField(db_column='Email', max_length=254)),
                ('status', models.CharField(db_column='Status', max_length=30)),
                ('created_dtm', models.DateTimeField(auto_now_add=True, db_column='CreatedDateTime')),
                ('updated_dtm', models.DateTimeField(db_column='UpdatedDateTime', default=None, null=True)),
            ],
            options={
                'get_latest_by': ['-created_dtm', '-updated_dtm'],
                'db_table': 'applications',
            },
        ),
    ]