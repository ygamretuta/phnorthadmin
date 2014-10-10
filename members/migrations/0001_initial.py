# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('photo', sorl.thumbnail.fields.ImageField(upload_to='')),
                ('testimonial', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
