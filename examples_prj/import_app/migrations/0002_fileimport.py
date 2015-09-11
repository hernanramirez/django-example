# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileImport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reference', models.CharField(default=b'none', max_length=100)),
                ('name_file', models.FileField(upload_to=b'files')),
                ('proccesed', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
