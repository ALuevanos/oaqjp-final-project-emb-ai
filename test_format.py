import json

# Mock Watson API response
mock_response = '''{
  "emotionPredictions": [
    {
      "emotion": {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.85,
        "sadness": 0.0
      }
    }
  ]
}'''

# Test the formatting logic
response_dict = json.loads(mock_response)
emotions = response_dict.get('emotionPredictions', [{}])[0].get('emotion', {})

anger_score = emotions.get('anger', 0)
disgust_score = emotions.get('disgust', 0)
fear_score = emotions.get('fear', 0)
joy_score = emotions.get('joy', 0)
sadness_score = emotions.get('sadness', 0)

emotion_scores = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score
}

dominant_emotion = max(emotion_scores, key=emotion_scores.get)

result = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
}

print(result)