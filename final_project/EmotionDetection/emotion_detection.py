import requests
import json

def emotion_detector(text_to_analyze):
    """
    This function sends a request to Watson NLP EmotionPredict
    and returns the response text.
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"}

    payload = {"raw_document": {"text": text_to_analyze }}

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Error handling for blank or invalid input
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Convert response text into dictionary
    response_dict = json.loads(response.text)

    emotions = response_dict["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    # Find dominant emotion
    dominant_emotion = max(
        {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness
        },
        key=lambda x: {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness
        }[x]
    )

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }
