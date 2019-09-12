"""Run `!pip install --upgrade google-api-python-client` in your console under this directory to install gcp ml api lib"""

APIKEY="XXXXXXXXXX"

# Running Vision API
from googleapiclient.discovery import build
import base64
import pprint
IMAGE="gs://cloud-training-demos/vision/sign2.jpg"

# below four images are face detection samples
# IMAGE="gs://cloud-training-demos/images/met/APS6880.jpg"
# IMAGE="gs://cloud-training-demos/images/met/DP205018.jpg"
# IMAGE="gs://cloud-training-demos/images/met/DP290402.jpg"
# IMAGE="gs://cloud-training-demos/images/met/DP700302.jpg"

vservice = build('vision', 'v1', developerKey=APIKEY)
service = build('translate', 'v2', developerKey=APIKEY)

request = vservice.images().annotate(body={
        'requests': [{
                'image': {
                    'source': {
                        'gcs_image_uri': IMAGE
                    }
                },
                'features': [{
                    'type': 'TEXT_DETECTION',
                    # 'type': 'FACE_DETECTION',
                    'maxResults': 3,
                }]
            }],
        })
responses = request.execute(num_retries=3)
# print the response of vision service
#pprint.pprint(responses)

""" for face detection, comment out all below"""
foreigntext = responses['responses'][0]['textAnnotations'][0]['description']
foreignlang = responses['responses'][0]['textAnnotations'][0]['locale']
# Print the text of OCR
print(foreignlang, foreigntext)

inputs=[foreigntext]
outputs = service.translations().list(source=foreignlang, target='en', q=inputs).execute()
# print(outputs)
for input, output in zip(inputs, outputs['translations']):
  print("{0} -> {1}".format(input, output['translatedText']))