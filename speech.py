"""Run `!pip install --upgrade google-api-python-client` in your console under this directory to install gcp ml api lib"""

APIKEY="XXXXXX"

# running Translate API
from googleapiclient.discovery import build

sservice = build('speech', 'v1', developerKey=APIKEY)
response = sservice.speech().recognize(
    body={
        'config': {
            'languageCode' : 'en-US',
            'encoding': 'LINEAR16',
            'sampleRateHertz': 16000
        },
        'audio': {
            'uri': 'gs://cloud-training-demos/vision/audio.raw'
            }
        }).execute()
print(response)