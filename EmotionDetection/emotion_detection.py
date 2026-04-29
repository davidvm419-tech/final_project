# Imports for the function
import json
import requests

# Function to send the text to IBM's model
def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Headers for the request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # body for the request
    text = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=text, headers=headers)

    # Check for invalid status code
    if response.status_code == 400:

        emotions = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

        return emotions
    
    # If not get data

    # Get anger, disgust, fear, joy and sadness values
    formatted_text = json.loads(response.text)

    emotions = {
        "anger": formatted_text["emotionPredictions"][0]["emotion"]["anger"],
        "disgust": formatted_text["emotionPredictions"][0]["emotion"]["disgust"],
        "fear": formatted_text["emotionPredictions"][0]["emotion"]["fear"],
        "joy": formatted_text["emotionPredictions"][0]["emotion"]["joy"],
        "sadness": formatted_text["emotionPredictions"][0]["emotion"]["sadness"],
    }
    
    # get the dominant emotion key or name
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Save the key on the emotions dictionary
    emotions["dominant_emotion"] = dominant_emotion

    return emotions
    