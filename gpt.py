from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import Flow

flow = Flow.from_client_secrets_file(
    'bureau.json',
    scopes=['https://www.googleapis.com/auth/youtube.upload'],
    redirect_uri='urn:ietf:wg:oauth:2.0:oob')
code = '4/0AfgeXvu75aw5U_1mXW3RBgxd-Ix6HGjOO26BIeAXLGpMbif2XuMI9QbKtqpMQT4NywZJqQ'
flow.fetch_token(code=code)

# Create a credentials object by passing the API key to the `Credentials` class
creds = flow.credentials
# creds = Credentials(
#            token="ya29.a0AeTM1icCU5P3PhlbCjlUFBqn6n0R5--0CXn9zh7xo5-0-wS4G94cjJrxhs_Uey6o6DhD9HHul_DnJN-lsi1DAmL9ArAZvnxe15VdJtFIa4L5sOAEc390sI_9zzhNtxyGUgGHbq0I2vgDcpyglcbjUxf9aWwLaCgYKAUESARASFQHWtWOmTQtPuMKMwsOonQb7sDX30g0163",
#            #refresh_token=token_dict.get('_refresh_token'),
#            #id_token=token_dict.get('_id_token'),
#            #token_uri=token_dict.get('_token_uri'),
#            client_id="785621539450-af6ja0ahpmuj7te7a4t3o5pbquehhmtj.apps.googleusercontent.com",
#            client_secret="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")

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
                "privacyStatus": "PUBLIC"
            }
        },
    ).execute()
