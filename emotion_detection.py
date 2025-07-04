import requests
from requests.auth import HTTPBasicAuth
import json


def emotion_detector(text_to_analyse):
    url = 'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/v1/analyze?version=2022-04-07'
    payload = {
        "text": text_to_analyse,
        "features": {
            "emotion": {
                "document": True
            }
        }
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        auth=HTTPBasicAuth("apikey", "bpcEobre2qPvq8jk8tlaldnYDYE0lwgB70JxcVAujW4B")
    )

    try:
        response_dict = json.loads(response.text)  # Step 1: Convert response to dictionary
    except json.JSONDecodeError:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    if response.status_code == 200:
        try:
            # Step 2: Extract emotions
            emotions = response_dict['emotion']['document']['emotion']

            anger = emotions.get('anger', 0)
            disgust = emotions.get('disgust', 0)
            fear = emotions.get('fear', 0)
            joy = emotions.get('joy', 0)
            sadness = emotions.get('sadness', 0)

            # Step 3: Find dominant emotion
            emotion_scores = {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness
            }
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Step 4: Return formatted result
            return {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': dominant_emotion
            }

        except KeyError:
            pass  # Fall through to error response below

    # Handle any error or malformed response
    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }


if __name__ == "__main__":
    text = input("Enter text to analyze: ")
    result = emotion_detector(text)
    print(result)
