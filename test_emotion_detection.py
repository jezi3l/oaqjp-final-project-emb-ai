import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    def test_joy_emotion(self):
        """Test if joy is detected as dominant emotion"""
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'joy')
        
    def test_anger_emotion(self):
        """Test if anger is detected as dominant emotion"""
        statement = "I am really mad about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'anger')
        
    def test_disgust_emotion(self):
        """Test if disgust is detected as dominant emotion"""
        statement = "I feel disgusted just hearing about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'disgust')
        
    def test_sadness_emotion(self):
        """Test if sadness is detected as dominant emotion"""
        statement = "I am so sad about this"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'sadness')
        
    def test_fear_emotion(self):
        """Test if fear is detected as dominant emotion"""
        statement = "I am really afraid that this will happen"
        result = emotion_detector(statement)
        self.assertEqual(result['dominant_emotion'], 'fear')
        
    def test_all_emotion_keys_present(self):
        """Test if all required emotion keys are present in response"""
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        expected_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
        for key in expected_keys:
            self.assertIn(key, result)
            
    def test_emotion_scores_are_numbers(self):
        """Test if emotion scores are numeric values"""
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        emotion_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        for key in emotion_keys:
            if result[key] is not None:
                self.assertIsInstance(result[key], (int, float))

if __name__ == '__main__':
    # Run the tests
    unittest.main()