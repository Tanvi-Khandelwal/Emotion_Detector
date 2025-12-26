import requests
import json

def emotion_detector(text_to_analyze):
    """
    This function sends a request to Watson NLP EmotionPredict
    and returns the response text.
    """

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(payload)
    )

    return response.text