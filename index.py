import json
import threading

from appwrite.client import Client
from appwrite.id import ID
from appwrite.services.storage import Storage
from appwrite.services.databases import Databases
from appwrite.query import Query

client = Client()
database = Databases(client)
(client
.set_endpoint('https://appwrite.senditeverywhere.com/v1')  # Your API Endpoint
.set_project('638e3cb0dea2968f1afa')  # Your project ID
.set_key(
    '5a0f11cb675717984e00cda60f975ea1f24bb37a0b3831bb19af973a5947305645789398ffc3fee76aa19ec28086d890e2527dd67aea252859b7feda1e318016f2da15bd63fc4219b584f1598d2c9cb2d40e1e1fa98a1c42397d5dbbf554303ac3f8acffcb526daddaf721418ee217b4bbc7e341fd418f4f7b026b93bd54fc26')
)

from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
from datetime import timedelta, datetime

import os
from dotenv import load_dotenv
load_dotenv()

client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'




def doStuff(*args):
    print("I DID STUFF")
    print(args)





@app.route('/webhook', methods=['POST'])
def respond():
    res = request.json
    if res["$collectionId"] == "638e47c1f24248bbcda6":
        now = datetime.now()
        print(type(request.json["vidId"]));
        run_at = now + timedelta(seconds=3)
        delay = (run_at - now).total_seconds()
        threading.Timer(delay, doStuff, [{"vidId": res["vidId"]}]).start()
    return Response(status=200)


# app.run()


storage = Storage(client)

# print(result.__sizeof__())

# get all schedules
toUpload = database.list_documents("63910075cc7582964627", "6391a27459ba27f94278",
                                   [Query.equal("uploaded", False), Query.orderAsc(attribute="dateTime")])

if toUpload["documents"]:
    print(toUpload["documents"])

