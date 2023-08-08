from django.apps import apps as global_apps
from django.db import migrations


def move_data_from_old_profiles_to_new_profiles(apps, schema_editor):
    try:
        OldProfiles = apps.get_model("oc_lettings_site", "Profile")
    except LookupError:
        return
    NewProfile = apps.get_model("profiles", "Profile")

    try:
        return NewProfile.objects.bulk_create(
            NewProfile(user=old_object.user,
                       favorite_city=old_object.favorite_city)
            for old_object in OldProfiles.objects.all())
    except LookupError:
        return


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]
    if global_apps.is_installed("oc_lettings_site"):
        dependencies.append(("oc_lettings_site", "0001_initial"))

    operations = [
        migrations.RunPython(move_data_from_old_profiles_to_new_profiles,
                             migrations.RunPython.noop)
    ]
    if global_apps.is_installed("oc_lettings_site"):
        operations.append(
            migrations.RunSQL("DROP TABLE oc_lettings_site_profile;"),
        )
