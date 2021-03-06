# Generated by Django 2.0.3 on 2018-07-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20180704_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natpage',
            name='Category',
            field=models.IntegerField(choices=[(0, 'Select:'), (1, 'NCC'), (2, 'NSS')], default=0),
        ),
        migrations.AlterField(
            model_name='natpage',
            name='DocType',
            field=models.IntegerField(choices=[(0, 'Select:'), (1, '(a) Certificate'), (2, '(b) Letter from Authorities'), (3, '(c) Appreciation recognition letter'), (4, '(d)Documentary evidence'), (5, '(e) Legal Proof'), (6, 'Others')], default=0),
        ),
        migrations.AlterField(
            model_name='natpage',
            name='SubCategory',
            field=models.IntegerField(choices=[(0, 'Select:'), (1, 'C certificate(os performance)'), (2, 'Best NSS Volunteer Awardee(University Level)'), (3, 'Participation in National Integration Camp'), (4, 'Participation in Pre-Republic Day Parade Camp'), (5, 'Best NSS Awardee(State Level/National Level)'), (6, 'Participation in Republic Day Parade Camp'), (7, 'International Youth Exchange Programme'), (8, 'Others')], default=0),
        ),
    ]
