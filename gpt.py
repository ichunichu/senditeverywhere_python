from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

import os
from dotenv import load_dotenv
load_dotenv()

client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")


creds = Credentials(
            token="ya29.a0AeTM1ie3Fm3LZnjlE7FExPz6_lB-BmjRgUXHTkBSw94RLPqE-2Y058vmMKMjZ7iqvSBw6FzGhBVXs0XH9Gg2DhJeuP6HIAjvZBNtjabUKQ94MLjUyYNvGnzH3qMOq1JJdrVCYuV32GePZj4OpY8p0Xt9yr46JAaCgYKAcISARASFQHWtWOmcyNpirisCQYT2Ny44CU02A0165",
            refresh_token="1//0371hKAgOHRM4CgYIARAAGAMSNwF-L9IrsXomcTeLJJrOqTRNXf5_AM6qM9v3BiDxDK3vrMv0NUoTeokvm6GDXq2MMfNf9NwcmSU",
            token_uri= "https://accounts.google.com/o/oauth2/token",
            client_id=client_id,
            client_secret=client_secret)

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
