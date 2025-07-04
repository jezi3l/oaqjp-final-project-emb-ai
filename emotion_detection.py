import requests
from requests.auth import HTTPBasicAuth
import json


def emotion_detector(text_to_analyse):
    url = 'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/v1/analyze?version=2022-04-07'
    myobj = {
        "text": text_to_analyse,
        "features": {
            "emotion": {
                "document": True
            }
        }
    }
    header = {"Content-Type": "application/json"}
    response = requests.post(
        url,
        json=myobj,
        headers=header,
        auth=HTTPBasicAuth("apikey", "bpcEobre2qPvq8jk8tlaldnYDYE0lwgB70JxcVAujW4B")
    )
    formatted_response = response.json()
    print(formatted_response)

    if response.status_code == 200:
        try:
            emotions = formatted_response['emotion']['document']['emotion']
            
            # Extract the required emotions with their scores
            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)
            
            # Find the dominant emotion (emotion with highest score)
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            
            # Return in the specified format
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        except KeyError:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

    # Handle server error
    elif response.status_code == 500:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Handle other unexpected errors
    else:
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
