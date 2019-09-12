"""Run `!pip install --upgrade google-api-python-client` in your console under this directory to install gcp ml api lib"""

APIKEY="AIzaSyByrfnjgBrNbUwwtQa6go361SFQ6y82NVM"

# running Translate API
from googleapiclient.discovery import build
service = build('translate', 'v2', developerKey=APIKEY)

# use the service
inputs = ['How come you grow taller than me?', 'Do not get comfortable', 'wow']
outputs = service.translations().list(source='en', target='zh', q=inputs).execute()
# print outputs
for input, output in zip(inputs, outputs['translations']):
  print("{0} -> {1}".format(input, output['translatedText']))