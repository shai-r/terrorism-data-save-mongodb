import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(verbose=True)

client = MongoClient(os.environ['MONGODB_URL'])
db = client[os.environ['TERRORISM_DATA']]
collection_name = "terrorism_events"

terrorism_collection = db.get_collection('terrorism_events')
def restart_mongo():
    db.drop_collection(collection_name)
    db.create_collection(
            collection_name,
            validator={
                "$jsonSchema": {
                    "bsonType": "object",
                    "required": ["event_id", "date", "location", "weapons", "casualties", "targets", "attack_type",
                                 "perpetrators"],
                    "properties": {
                        "event_id": {"bsonType": "string"},
                        "date": {
                            "bsonType": "object",
                            "required": ["year", "month", "day"],
                            "properties": {
                                "year": {"bsonType": "int"},
                                "month": {"bsonType": "int"},
                                "day": {"bsonType": "int"}
                            }
                        },
                        "location": {
                            "bsonType": "object",
                            "required": ["country", "region", "city", "latitude", "longitude"],
                            "properties": {
                                "country": {
                                    "bsonType": "object",
                                    "required": ["code", "text"],
                                    "properties": {
                                        "code": {"bsonType": "int"},
                                        "text": {"bsonType": "string"}
                                    }
                                },
                                "region": {
                                    "bsonType": "object",
                                    "required": ["code", "text"],
                                    "properties": {
                                        "code": {"bsonType": "int"},
                                        "text": {"bsonType": "string"}
                                    }
                                },
                                "state": {"bsonType": "string"},
                                "city": {"bsonType": "string"},
                                "latitude": {"bsonType": "double"},
                                "longitude": {"bsonType": "double"}
                            }
                        },
                        "weapons": {
                            "bsonType": "array",
                            "items": {
                                "bsonType": "object",
                                "required": ["type", "subtype"],
                                "properties": {
                                    "type": {
                                        "bsonType": "object",
                                        "required": ["code", "text"],
                                        "properties": {
                                            "code": {"bsonType": "int"},
                                            "text": {"bsonType": "string"}
                                        }
                                    },
                                    "subtype": {
                                        "bsonType": "object",
                                        "required": ["code", "text"],
                                        "properties": {
                                            "code": {"bsonType": "int"},
                                            "text": {"bsonType": "string"}
                                        }
                                    }
                                }
                            }
                        },
                        "casualties": {
                            "bsonType": "object",
                            "required": ["killed", "wounded", "details"],
                            "properties": {
                                "killed": {"bsonType": "int"},
                                "wounded": {"bsonType": "int"},
                                "details": {
                                    "bsonType": "object",
                                    "properties": {
                                        "us_killed": {"bsonType": "int"},
                                        "terrorists_killed": {"bsonType": "int"},
                                        "us_wounded": {"bsonType": "int"},
                                        "terrorists_wounded": {"bsonType": "int"}
                                    }
                                }
                            }
                        },
                        "groups": {
                            "bsonType": "array",
                            "items": {
                                "bsonType": "object",
                                "properties": {
                                    "name": {"bsonType": "string"},
                                    "subname": {"bsonType": "string"}
                                }
                            }
                        },
                        "targets": {
                            "bsonType": "array",
                            "items": {
                                "bsonType": "object",
                                "required": ["type", "subtype", "details", "nationality"],
                                "properties": {
                                    "type": {
                                        "bsonType": "object",
                                        "required": ["code", "text"],
                                        "properties": {
                                            "code": {"bsonType": "int"},
                                            "text": {"bsonType": "string"}
                                        }
                                    },
                                    "subtype": {
                                        "bsonType": "object",
                                        "required": ["code", "text"],
                                        "properties": {
                                            "code": {"bsonType": "int"},
                                            "text": {"bsonType": "string"}
                                        }
                                    },
                                    "details": {"bsonType": "string"},
                                    "nationality": {
                                        "bsonType": "object",
                                        "required": ["code", "text"],
                                        "properties": {
                                            "code": {"bsonType": "int"},
                                            "text": {"bsonType": "string"}
                                        }
                                    }
                                }
                            }
                        },
                        "attack_type": {
                            "bsonType": "object",
                            "required": ["primary", "secondary", "tertiary"],
                            "properties": {
                                "primary": {
                                    "bsonType": "object",
                                    "required": ["code", "text"],
                                    "properties": {
                                        "code": {"bsonType": "int"},
                                        "text": {"bsonType": "string"}
                                    }
                                },
                                "secondary": {
                                    "bsonType": "object",
                                    "required": ["code", "text"],
                                    "properties": {
                                        "code": {"bsonType": "int"},
                                        "text": {"bsonType": "string"}
                                    }
                                },
                                "tertiary": {
                                    "bsonType": "object",
                                    "required": ["code", "text"],
                                    "properties": {
                                        "code": {"bsonType": "int"},
                                        "text": {"bsonType": "string"}
                                    }
                                }
                            }
                        },
                        "perpetrators": {
                            "bsonType": "object",
                            "required": ["count", "captured"],
                            "properties": {
                                "count": {"bsonType": "int"},
                                "captured": {"bsonType": "int"}
                            }
                        }
                    }
                }
            }
        )
