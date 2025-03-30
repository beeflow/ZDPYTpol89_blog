"""copyright (c) 2014 - 2025 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""


def get_photo_path_name(instance, filename: str) -> str:
    object_id = getattr(instance, 'id', None)

    # katalog: nazwa_modelu/id_obiektu/nazwa_pliku.jpg
    return "{}/{}/{}".format(
        instance.__class__.__name__.lower(),
        object_id,
        filename
    )
