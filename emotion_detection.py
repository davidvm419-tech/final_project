# Imports for the function
import requests
# Function to send the text to IBM's model
def emotion_detector(text_to_analize):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Headers for the request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # body for the request
    text = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=text, headers=headers)

    return response.text