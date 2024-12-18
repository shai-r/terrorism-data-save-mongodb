from app.mongodb.database_mongo import terrorism_collection, restart_mongo
from app.mongodb.repository_mongo import create_indexes
from app.services.consumer_service import save_in_mongo_consumer

if __name__ == '__main__':
    restart_mongo()
    create_indexes(terrorism_collection)
    save_in_mongo_consumer()
    print(len(list(terrorism_collection.find({}))))