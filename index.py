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
from appwrite.services.databases import Databases
from appwrite.query import Query

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload


client = Client()
database = Databases(client)
(client
  .set_endpoint('https://appwrite.senditeverywhere.com/v1') # Your API Endpoint
  .set_project('638e3cb0dea2968f1afa') # Your project ID
  .set_key('5a0f11cb675717984e00cda60f975ea1f24bb37a0b3831bb19af973a5947305645789398ffc3fee76aa19ec28086d890e2527dd67aea252859b7feda1e318016f2da15bd63fc4219b584f1598d2c9cb2d40e1e1fa98a1c42397d5dbbf554303ac3f8acffcb526daddaf721418ee217b4bbc7e341fd418f4f7b026b93bd54fc26') # Your secret API key
)

storage = Storage(client)



#print(result.__sizeof__())

#get all schedules
toUpload = database.list_documents("63910075cc7582964627","6391a27459ba27f94278",[Query.equal("uploaded", False), Query.orderAsc(attribute="dateTime")])

if toUpload["documents"]:
    print(toUpload["documents"])



credentials = Credentials("ya29.a0AeTM1icCU5P3PhlbCjlUFBqn6n0R5--0CXn9zh7xo5-0-wS4G94cjJrxhs_Uey6o6DhD9HHul_DnJN-lsi1DAmL9ArAZvnxe15VdJtFIa4L5sOAEc390sI_9zzhNtxyGUgGHbq0I2vgDcpyglcbjUxf9aWwLaCgYKAUESARASFQHWtWOmTQtPuMKMwsOonQb7sDX30g0163")

client = build('youtube', 'v3', credentials)

body = {
            'snippet': {
                'title': 'My Django Youtube Video',
                'description': 'My Django Youtube Video Description',
                'tags': 'django,howto,video,api',
                'categoryId': '27'
            },
            'status': {
                'privacyStatus': 'unlisted'
            }
        }
#https://developers.google.com/identity/protocols/oauth2/web-server#httprest_3
with open("test.mp4",mode="rb") as file:
    result = file.read()
    insert_request = client.videos().insert(
                part=','.join(body.keys()),
                body=body,
                media_body=MediaFileUpload(
                    file.name, chunksize=-1, resumable=True)
            )
    insert_request.execute()








#result = storage.get_file_download('638efd926527d6cbf083', '638eff2461938913eae7')



