"""
Flask web application for emotion detection.

This module provides a web interface to analyze emotions
from user-provided text using the Watson NLP Emotion API.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the home page of the emotion detection application.

    Returns:
        HTML template for index page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    """
    Handle emotion detection requests from the web interface.

    Retrieves user input text, processes emotion detection,
    and returns a formatted response string.

    Returns:
        str: Emotion analysis result or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
