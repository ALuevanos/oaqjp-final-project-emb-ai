import json
from EmotionDetection import emotion_detector

# Mock the requests.post to simulate Watson API response
import unittest.mock as mock

mock_response_text = '''{
  "emotionPredictions": [
    {
      "emotion": {
        "anger": 0.87,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.0,
        "sadness": 0.13
      }
    }
  ]
}'''

with mock.patch('requests.post') as mock_post:
    mock_post.return_value.text = mock_response_text
    result = emotion_detector("I hate working long hours")
    print("Package import successful!")
    print(result)
    print(f"Dominant emotion: {result['dominant_emotion']}")