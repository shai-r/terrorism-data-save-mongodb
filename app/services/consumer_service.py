import os

from dotenv import load_dotenv

from app.mongodb.database_mongo import terrorism_collection
from app.mongodb.repository_mongo import insert_terrorism_events
from app.services.mongo_service import transform_data_to_record
from app.settings.kafka_settings.consumer import create_consumer

load_dotenv(verbose=True)
topic = os.environ['SAVE_IN_MONGO_TOPIC']
bootstrap_servers = os.environ['BOOTSTRAP_SERVERS']

def save_in_mongo_consumer():
    consume = create_consumer(topic, bootstrap_servers)
    for message in consume:
        try:
            inserted = insert_terrorism_events(
                collection=terrorism_collection,
                data=transform_data_to_record(message.value)
            )
            print(f'Received- {message.key}, :{inserted}')
        except Exception as e:
            print(f"Failed to insert message: {e}")
            continue

