from EmotionDetection.emotion_detection import emotion_detector
import unittest

class test_emotion_detector(unittest.TestCase):
    def test1(self):
        # Test case
        test0 = emotion_detector("I am glad this happened")
        test1 = emotion_detector("I am really mad about this")
        test2 = emotion_detector("I feel disgusted just hearing about this")
        test3 = emotion_detector("I am so sad about this")
        test4 = emotion_detector("I am really afraid that this will happen")
        
        # test assertion
        self.assertEqual(test0["dominant_emotion"], "joy")
        self.assertEqual(test1["dominant_emotion"], "anger")
        self.assertEqual(test2["dominant_emotion"], "disgust")
        self.assertEqual(test3["dominant_emotion"], "sadness")
        self.assertEqual(test4["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()
    