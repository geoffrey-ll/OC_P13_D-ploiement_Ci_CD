"""Migration des données des anciennes tables, vers les nouvelles."""
from django.apps import apps as global_apps
from django.db import migrations


def move_data_from_old_lettings_to_new_lettings(apps, schema_editor):
    """Transfert des data de lettings vers leurs nouvelles tables."""
    try:
        OldLetting = apps.get_model("oc_lettings_site", "Letting")
    except LookupError:
        return
    attributes = ["number", "street", "city",
                  "state", "zip_code", "country_iso_code"]
    NewAddress = apps.get_model("lettings", "Address")
    NewLetting = apps.get_model("lettings", "Letting")

    for old_letting in OldLetting.objects.all():
        old_title = old_letting.title
        old_address = old_letting.address
        dict_old_address = {
            attribute: getattr(old_address, attribute)
            for attribute in attributes
        }
        new_address, bool_status = \
            NewAddress.objects.get_or_create(**dict_old_address)
        try:
            NewLetting.objects.create(title=old_title, address=new_address)
        except LookupError:
            continue


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]
    if global_apps.is_installed("oc_lettings_site"):
        dependencies.append(("oc_lettings_site", "0001_initial"))

    operations = [
        migrations.RunPython(move_data_from_old_lettings_to_new_lettings,
                             migrations.RunPython.noop),
    ]
    if global_apps.is_installed("oc_lettings_site"):
        operations.append(
            migrations.RunSQL([("DROP TABLE oc_lettings_site_address;"),
                               ("DROP TABLE oc_lettings_site_letting;")]),
        )
