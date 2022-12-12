from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import Flow

#flow = Flow.from_client_secrets_file(
#    'bureau.json',
#    scopes=['https://www.googleapis.com/auth/youtube.upload'],
#    redirect_uri='urn:ietf:wg:oauth:2.0:oob')
#code = '4/0AfgeXvu75aw5U_1mXW3RBgxd-Ix6HGjOO26BIeAXLGpMbif2XuMI9QbKtqpMQT4NywZJqQ'
#flow.fetch_token(code=code)
#
## Create a credentials object by passing the API key to the `Credentials` class
#creds = flow.credentials


#{
#	"access_token": "ya29.a0AeTM1icZ5iiF2pwE-uBhFeK63qXfVXwoY8D-gg_og1LBV11JY9ia9geDcubSWePVZxr8rzt48yigkdpd5Jt0PgjWFf5a48h2iYeM52_6nEAKbt7YxNjPHYUJXUtDzGbAX2n2p-XdgySgrY5bWGzcW87eIIi6aCgYKAVASARASFQHWtWOmnU9tQWnuA3fIIhiSFD63uA0163",
#	"expires_in": 3599,
#	"refresh_token": "1//09eSzaNO7YAnkCgYIARAAGAkSNwF-L9IrK5qGD5_ONPO4jq5EhQPuL7fxt60sknpKyklPbCezjX08RbR5Vi957xlnO_K6qy9hS7Q",
#	"scope": "https://www.googleapis.com/auth/youtube.upload",
#	"token_type": "Bearer"
#}

creds = Credentials(
            token="ya29.a0AeTM1icZ5iiF2pwE-uBhFeK63qXfVXwoY8D-gg_og1LBV11JY9ia9geDcubSWePVZxr8rzt48yigkdpd5Jt0PgjWFf5a48h2iYeM52_6nEAKbt7YxNjPHYUJXUtDzGbAX2n2p-XdgySgrY5bWGzcW87eIIi6aCgYKAVASARASFQHWtWOmnU9tQWnuA3fIIhiSFD63uA0163",
            refresh_token="1//09eSzaNO7YAnkCgYIARAAGAkSNwF-L9IrK5qGD5_ONPO4jq5EhQPuL7fxt60sknpKyklPbCezjX08RbR5Vi957xlnO_K6qy9hS7Q",
            #id_token=token_dict.get('_id_token'),

    token_uri= "https://accounts.google.com/o/oauth2/token"
,
client_id="785621539450-af6ja0ahpmuj7te7a4t3o5pbquehhmtj.apps.googleusercontent.com",
            client_secret="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")

# Build the YouTube API client
youtube = build("youtube", "v3", credentials=creds)

# Use the YouTube API to upload the video
with open("test.mp4", "rb") as file:
    media = MediaFileUpload('test.mp4',
                            mimetype='video/mp4')

    youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": "YOUR_VIDEO_TITLE",
                "description": "YOUR_VIDEO_DESCRIPTION"
            },
            "status": {
                "privacyStatus": "private"
            }
        },

        media_body=media
    ).execute()
#Quotat du jour atteint. La ligne media_body doit etre tester (je l'avais retirer pour essayer de debug le code, mais
# ducoup le quotat as était atteint avant que je pense a la remettre)