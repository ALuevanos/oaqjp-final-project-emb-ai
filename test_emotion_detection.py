import unittest
from EmotionDetection import emotion_detector
import unittest.mock as mock

class TestEmotionDetector(unittest.TestCase):
    
    def test_emotion_detector_joy(self):
        """Test that 'I am glad this happened' returns joy as dominant emotion"""
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
            mock_post.return_value.text = mock_response_text
            result = emotion_detector("I am glad this happened")
            self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_emotion_detector_anger(self):
        """Test that 'I am really mad about this' returns anger as dominant emotion"""
        mock_response_text = '''{
          "emotionPredictions": [
            {
              "emotion": {
                "anger": 0.9,
                "disgust": 0.0,
                "fear": 0.0,
                "joy": 0.0,
                "sadness": 0.1
              }
            }
          ]
        }'''
        with mock.patch('requests.post') as mock_post:
            mock_post.return_value.text = mock_response_text
            result = emotion_detector("I am really mad about this")
            self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_emotion_detector_disgust(self):
        """Test that 'I feel disgusted just hearing about this' returns disgust as dominant emotion"""
        mock_response_text = '''{
          "emotionPredictions": [
            {
              "emotion": {
                "anger": 0.0,
                "disgust": 0.9,
                "fear": 0.0,
                "joy": 0.0,
                "sadness": 0.1
              }
            }
          ]
        }'''
        with mock.patch('requests.post') as mock_post:
            mock_post.return_value.text = mock_response_text
            result = emotion_detector("I feel disgusted just hearing about this")
            self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_emotion_detector_sadness(self):
        """Test that 'I am so sad about this' returns sadness as dominant emotion"""
        mock_response_text = '''{
          "emotionPredictions": [
            {
              "emotion": {
                "anger": 0.0,
                "disgust": 0.0,
                "fear": 0.0,
                "joy": 0.1,
                "sadness": 0.9
              }
            }
          ]
        }'''
        with mock.patch('requests.post') as mock_post:
            mock_post.return_value.text = mock_response_text
            result = emotion_detector("I am so sad about this")
            self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_emotion_detector_fear(self):
        """Test that 'I am really afraid that this will happen' returns fear as dominant emotion"""
        mock_response_text = '''{
          "emotionPredictions": [
            {
              "emotion": {
                "anger": 0.0,
                "disgust": 0.0,
                "fear": 0.9,
                "joy": 0.0,
                "sadness": 0.1
              }
            }
          ]
        }'''
        with mock.patch('requests.post') as mock_post:
            mock_post.return_value.text = mock_response_text
            result = emotion_detector("I am really afraid that this will happen")
            self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()