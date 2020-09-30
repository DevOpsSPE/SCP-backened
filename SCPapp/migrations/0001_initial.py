# Generated by Django 3.1 on 2020-09-30 05:35

import SCPapp.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='emailVerify',
            fields=[
                ('rollNumber', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100)),
                ('otp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('author', models.CharField(default='Admin', max_length=141)),
                ('subject', models.CharField(max_length=101)),
                ('year', models.IntegerField()),
                ('resourceType', models.CharField(blank=True, max_length=20, null=True)),
                ('semester', models.IntegerField()),
                ('numberofUpvotes', models.IntegerField(default=0)),
                ('numberofDownvotes', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=141)),
                ('title', models.CharField(max_length=101)),
                ('yearPlaced', models.IntegerField()),
                ('experience', models.CharField(blank=True, max_length=2000, null=True)),
                ('yearPassout', models.IntegerField()),
                ('company', models.CharField(default='', max_length=20)),
                ('numberofUpvotes', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(default='Student', max_length=15)),
                ('rollNumber', models.CharField(max_length=15, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', SCPapp.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CommentsPYQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('commentBody', models.CharField(default='', max_length=1000)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('pyq', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='SCPapp.file')),
            ],
        ),
        migrations.CreateModel(
            name='CommentsExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('commentBody', models.CharField(default='', max_length=1000)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('exp', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='SCPapp.interview')),
            ],
        ),
    ]
