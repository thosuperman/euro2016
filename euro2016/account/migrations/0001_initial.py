# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', error_messages={'unique': 'A user with that username already exists.'}, unique=True, verbose_name='username', max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=254)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('fav_team', models.CharField(choices=[('NS', 'None'), ('Albania', 'Alb'), ('Austria', 'Aus'), ('Belgium', 'Bel'), ('Croatia', 'Cro'), ('Czech Republic', 'Czech'), ('England', 'Eng'), ('France', 'Fra'), ('Germany', 'Ger'), ('Hungary', 'Hun'), ('Iceland', 'Ice'), ('Italy', 'Ita'), ('Northern Ireland', 'NIre'), ('Poland', 'Pol'), ('Portugal', 'Por'), ('Republic of Ireland', 'RIre'), ('Romania', 'Rom'), ('Russia', 'Russ'), ('Slovakia', 'Slov'), ('Spain', 'Spa'), ('Sweden', 'Swe'), ('Switzerland', 'Swi'), ('Turkey', 'Tur'), ('Ukraine', 'Ukr'), ('Wales', 'Wal')], default='NS', max_length=100)),
                ('groups', models.ManyToManyField(related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', verbose_name='groups', blank=True, to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', help_text='Specific permissions for this user.', related_query_name='user', verbose_name='user permissions', blank=True, to='auth.Permission')),
            ],
            options={
                'verbose_name': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='customuser',
            unique_together=set([('email',)]),
        ),
    ]
