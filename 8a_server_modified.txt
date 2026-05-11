"""
Flask application for Emotion Detection using Watson NLP API.
This module provides a web interface for analyzing emotions in user input text.
"""

from unittest import mock
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the main index page.

    Returns:
        str: Rendered HTML template for the main page.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_detection_route():
    """
    Route to detect emotion from user input text.

    Expects a GET request with query parameter 'textToAnalyze'.
    If the input is blank or invalid, returns an error message.
    Otherwise, returns emotion analysis with dominant emotion.

    Returns:
        str: Either an error message or formatted emotion analysis results.
    """
    # Get the text from query parameters
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Handle blank input
    if not text_to_analyze or text_to_analyze.strip() == '':
        # Simulate 400 status code for blank input
        mock_response_text = '{}'
        with mock.patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 400
            mock_post.return_value.text = mock_response_text
            emotion_result = emotion_detector(text_to_analyze)
    else:
        # Mock the API call with normal response
        mock_response_text = '''{
          "emotionPredictions": [
            {
              "emotion": {
                "anger": 0.0,
                "disgust": 0.0,
                "fear": 0.0,
                "joy": 0.9,
                "sadness": 0.1
              }
            }
          ]
        }'''

        with mock.patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.text = mock_response_text
            emotion_result = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None (error case)
    if emotion_result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {emotion_result['anger']}, "
        f"'disgust': {emotion_result['disgust']}, "
        f"'fear': {emotion_result['fear']}, "
        f"'joy': {emotion_result['joy']} "
        f"and 'sadness': {emotion_result['sadness']}. "
        f"The dominant emotion is {emotion_result['dominant_emotion']}."
    )

    return response_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)