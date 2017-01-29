# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-29 12:41
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20170121_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsoredevent',
            name='abstract',
            field=core.models.EAWTextField(help_text="<p><a href='#' data-toggle='modal' data-target='#proposalFieldExampleModal' data-content='abstract'>Proposal Examples</a></p>The overview of what the talk is about. If the talk assume some domain knowledge please state it here. If your talk is accepted, this will be displayed on both the website and the handbook. Should be one paragraph.", max_length=1000, verbose_name='abstract'),
        ),
        migrations.AlterField(
            model_name='sponsoredevent',
            name='detailed_description',
            field=models.TextField(blank=True, help_text="<p><a href='#' data-toggle='modal' data-target='#proposalFieldExampleModal'data-content='detailed description'>Proposal Examples</a></p>Try not be too lengthy to scare away reviewers or potential audience. A comfortable length is less than 2000 characters (or about 1200 Chinese characters). Since most reviewers may not understand the topic as deep as you do, including related links to the talk topic will help reviewers understand the proposal. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='detailed description'),
        ),
    ]
