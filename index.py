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
  .set_endpoint('https://appwrite.senditeverywhere.com/v1') # Your API Endpoint
  .set_project('638e3cb0dea2968f1afa') # Your project ID
  .set_key('5a0f11cb675717984e00cda60f975ea1f24bb37a0b3831bb19af973a5947305645789398ffc3fee76aa19ec28086d890e2527dd67aea252859b7feda1e318016f2da15bd63fc4219b584f1598d2c9cb2d40e1e1fa98a1c42397d5dbbf554303ac3f8acffcb526daddaf721418ee217b4bbc7e341fd418f4f7b026b93bd54fc26') # Your secret API key
)

storage = Storage(client)

with open("test.mp4",mode="rb") as file:
    result = file.read()

print(result.__sizeof__())

#result = storage.get_file_download('638efd926527d6cbf083', '638eff2461938913eae7')



