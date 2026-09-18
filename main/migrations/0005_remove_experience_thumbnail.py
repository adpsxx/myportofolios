from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_project_project_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='thumbnail',
        ),
    ]
