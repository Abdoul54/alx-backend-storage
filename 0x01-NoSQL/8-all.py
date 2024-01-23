#!/usr/bin/env python3
def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list containing all documents in the collection.
    """
    documents = list(mongo_collection.find())
    return documents


if __name__ == "__main__":
    # Example usage
    from pymongo import MongoClient

    # Connect to MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the desired database and collection
    db = client.my_db
    school_collection = db.school

    # Call the list_all function
    schools = list_all(school_collection)

    # Print the results
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
