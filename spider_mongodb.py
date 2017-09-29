import pymongo
import pprint
import json
import datetime
from pymongo import MongoClient


def run_mongo():

    PTT_JSON = './tmp_pic/data.json'
    client = MongoClient()
    db = client.myfirstdb
    collections= db.posts

    post={"author": "Mike",
          "text": "My first blog post!",
          "tags": ["mongodb", "python", "pymongo"],
          "date": datetime.datetime.utcnow()}

    collections.insert_one(post).inserted_id
    pprint.pprint(collections.find_one())

    with open(PTT_JSON, 'r') as f:
        js = json.load(f)

    for u in js:
        title=u['tilte']
        liked=u['liked']
        href=u['href']
        result=collections.find_one({'title':title})
        if(result is not None):
            continue

        post={"title": title,
              "liked": liked,
              "href": href
        }
        collections.insert_one(post).inserted_id
