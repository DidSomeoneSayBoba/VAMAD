#!/usr/bin/python

"""Google Drive Quickstart in Python.
This script uploads a single file to Google Drive.
"""

from __future__ import print_function
import os
import pprint
import six
import httplib2
from googleapiclient.discovery import build
import googleapiclient.http
import oauth2client.client

# OAuth 2.0 scope that will be authorized.
# Check https://developers.google.com/drive/scopes for all available scopes.
OAUTH2_SCOPE = 'https://www.googleapis.com/auth/drive'

# Location of the client secrets.
CLIENT_SECRETS = 'client_id.json'

# Path to the file to upload.

flow = oauth2client.client.flow_from_clientsecrets(CLIENT_SECRETS, OAUTH2_SCOPE)
flow.redirect_uri = oauth2client.client.OOB_CALLBACK_URN
authorize_url = flow.step1_get_authorize_url()
print('Go to the following link in your browser: ' + authorize_url)
        # `six` library supports Python2 and Python3 without redefining builtin input()
code = six.moves.input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)

# Create an authorized Drive API client.
http = httplib2.Http()
credentials.authorize(http)
drive_service = build('drive', 'v2', http=http)
# Metadata about the file.
MIMETYPE = 'video/mp4'
DESCRIPTION = 'event video'
while True:
    for file in os.listdir("./yolov4-deepsort-master"):
        if file.endswith(".mp4") and not file == "upload.mp4":
            FILENAME = os.path.join("./yolov4-deepsort-master", file)
            TITLE = file

            print(os.path.join("./yolov4-deepsort-master", file))
            file_metadata = {'name': os.path.join("./yolov4-deepsort-master", file)}
# Perform OAuth2.0 authorization flow.


# Insert a file. Files are comprised of contents and metadata.
# MediaFileUpload abstracts uploading file contents from a file on disk.
            media_body = googleapiclient.http.MediaFileUpload(
                FILENAME,
                mimetype=MIMETYPE,
                resumable=True
            )
# The body contains the metadata for the file.
            body = {
              'title': TITLE,
              'description': DESCRIPTION,
            }

# Perform the request and print the result.
            new_file = drive_service.files().insert(
              body=body, media_body=media_body).execute()
            pprint.pprint(new_file)
            print(file.replace('\'',''))
            os.system("sudo rm ./yolov4-deepsort-master/"+file)