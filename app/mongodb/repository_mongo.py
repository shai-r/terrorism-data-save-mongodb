import pymongo
from pymongo import ASCENDING, DESCENDING, TEXT, UpdateOne
from pymongo.collection import Collection


def insert_terrorism_events(collection, data):
    return collection.insert_many(data)



def create_indexes(collection: Collection):
    try:
        collection.drop_indexes()
        collection.create_index(
            [("event_id", ASCENDING)],
            # unique=True,
            name="event_id_index"
        )

        collection.create_index(
            [("attack_type.primary.code", ASCENDING)],
            name="attack_type_primary_index"
        )
        collection.create_index(
            [("attack_type.secondary.code", ASCENDING)],
            name="attack_type_secondary_index"
        )

        collection.create_index(
            [("location.region.code", ASCENDING),
            ("location.country.code", ASCENDING)],
            name="compound_location_index"
        )

        collection.create_index([("groups.name", ASCENDING)], name="groups_index")

        collection.create_index([("targets.type.code", ASCENDING)], name="targets_code_index")

        collection.create_index([
            ("date.year", ASCENDING),
            ("date.month", ASCENDING),
        ], name="datetime_index")

    except Exception as e:
        print(f"Error creating indexes: {e}")
