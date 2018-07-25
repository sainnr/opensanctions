# from memorious.operations import store
# from memorious.operations import db

import os
import json
import shutil
import random


def store_entity(context, data):
    context.params["unique"] = ["id", "name", "program"]
    context.params["children"] = [
        {
            "key": "aliases",
            "inherit": {"entity_id": "id"},
            "unique": ["entity_id", "name"],
        },
        {
            "key": "addresses",
            "inherit": {"entity_id": "id"},
            "unique": [
                "entity_id", "city", "country_code", "country_name",
                "postal_code", "region", "street", "street_2", "text"
            ],
        },
        {
            "key": "identifiers",
            "inherit": {"entity_id": "id"},
            "unique": ["entity_id", "type", "number"],
        },
        {
            "key": "nationalities",
            "inherit": {"entity_id": "id"},
            "unique": ["entity_id", "country_code"],
        },
        {
            "key": "birth_dates",
            "inherit": {"entity_id": "id"},
            "unique": ["entity_id", "date"],
        },
        {
            "key": "birth_places",
            "inherit": {"entity_id": "id"},
            "unique": ["entity_id", "place"],
        },
    ]
    # db(context, data)
    directory(context, data)


def directory(context, data):
    """Store the collected files to a given directory."""
    with context.http.rehash(data) as result:
        # VS: Original code fails at this point, for an unknown reason
        #
        # if not result.ok:
        #     context.log.info("WARN: result not ok")
        #     return

        # VS: this branch fails as well (if uncommented)
        #
        # content_hash = data.get('content_hash')
        # if content_hash is None:
        #     context.log.info("WARN: no hash")
        #     context.emit_warning("No content hash in data.")
        #     return

        context.log.info(result)
        context.log.info(result.ok)
        context.log.info(result.file_path)
        context.log.info(result.file_name)
        context.log.info(result.raw)

        path = "/data/json"
        # file_name = random.randint(100000, 1000000)
        file_name = "master"

        # VS: Skipped all tricky namings for resulting files, using just hash of the data entry
        #
        # file_name = data.get('file_name', result.file_name)
        # file_name = '%s.%s' % ("sddata", file_name)
        # data['_file_name'] = file_name
        # file_path = os.path.join(path, file_name)
        # if not os.path.exists(file_path):
        #     shutil.copyfile(result.file_path, file_path)

        context.log.info("Store in a file:")
        # context.log.info(file_name)

        meta_path = os.path.join(path, '%s.json' % file_name)
        context.log.info(meta_path)

        # with open(meta_path, 'w') as fh:
        with open(meta_path, 'a+') as fh:
            json.dump(data, fh)
            context.log.info(fh.name)


def remove_namespace(doc, namespace):
    """Remove namespace in the passed document in place."""
    ns = u'{%s}' % namespace
    nsl = len(ns)
    for elem in doc.getiterator():
        if elem.tag.startswith(ns):
            elem.tag = elem.tag[nsl:]
