# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 02:01
from __future__ import unicode_literals

from django.db import migrations, models
import shadowsocks.tools


class Migration(migrations.Migration):

    dependencies = [
        ('shadowsocks', '0003_auto_20170716_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='InviteCode',
            fields=[
                ('code', models.CharField(blank=True, default=shadowsocks.tools.get_long_random_string, max_length=40, primary_key=True, serialize=False, verbose_name='邀请码')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '邀请码',
                'ordering': ('-time_created',),
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('name', models.CharField(max_length=32, verbose_name='名字')),
                ('server', models.CharField(max_length=128, verbose_name='服务器IP')),
                ('menthod', models.CharField(choices=[('aes-256-cfb', 'aes-256-cfb'), ('rc4-md5', 'rc4-md5'), ('salsa20', 'salsa20'), ('aes-128-ctr', 'aes-128-ctr')], default='aes-256-cfb', max_length=32, verbose_name='加密类型')),
                ('info', models.CharField(blank=True, max_length=1024, null=True, verbose_name='节点说明')),
                ('status', models.CharField(choices=[('ok', '好用'), ('slow', '不好用'), ('fail', '坏了')], default='ok', max_length=32, verbose_name='状态')),
                ('node_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='节点id')),
            ],
            options={
                'verbose_name_plural': '节点',
                'ordering': ['node_id'],
            },
        ),
    ]