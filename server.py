"""
Flask web application for emotion detection.

This module provides a web interface for analyzing emotions in text
using IBM Watson Natural Language Understanding API.
"""

from flask import Flask, request, render_template
from emotion_detection import emotion_detector  # pylint: disable=import-error

# Initialize Flask app
app = Flask(__name__)


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Flask route for emotion detection.

    Gets text from query parameter and returns formatted response.
    
    Returns:
        str: Formatted emotion analysis result or error message.
    """
    # Get the text to analyze from query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detection function (it will handle blank entries internally)
    response = emotion_detector(text_to_analyze)

    # Check if there was an error in the emotion detection (dominant_emotion is None)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Format the response according to requirements
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Create the formatted response string
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_response


if __name__ == '__main__':
    # Run the Flask app on localhost:5000
    app.run(host='0.0.0.0', port=5000, debug=True)
