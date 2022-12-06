import threading

from flask import Flask, request, Response
from datetime import timedelta, datetime

app = Flask(__name__)

def doStuff(*args):
    print("I DID STUFF")
    print(args)

@app.route('/webhook', methods=['POST'])
def respond():
    res = request.json;
    if res["$collectionId"] == "638e47c1f24248bbcda6":
        now = datetime.now()
        print(type(request.json["vidId"]));
        run_at = now + timedelta(seconds=3)
        delay = (run_at - now).total_seconds()
        threading.Timer(delay, doStuff, [{"vidId":res["vidId"]}]).start()
    return Response(status=200)

#app.run()

from appwrite.client import Client
from appwrite.services.storage import Storage

client = Client()

(client
  .set_endpoint('http://45.140.164.127/v1') # Your API Endpoint
  .set_project('638e3cb0dea2968f1afa') # Your project ID
  .set_key('84cc4810c6b3e545190b46c5d1c58aab51cf497be5c71d386de82db6a5bfdafb0638cbde819eb58bd532a0570b45e61b6b168265b1a79fbecc236c589b83b078017d056731ca584055eb923108b5c5999efa332c09457e2c9df6b425a9f5514ac7aab1b7f73556211d9bbc4f8d1b24c03707c0adce1ffbab8d686eb29a1c01e4') # Your secret API key
)

storage = Storage(client)

result = storage.get_file_download('638e3cbb9709b0fdce1e', '638e5c2d93101fa2f253')

print(result.__sizeof__())

