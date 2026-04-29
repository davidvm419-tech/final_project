''' Executing this function initiates the application of emotion detector
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request

# Import the emotion_detector function from the package
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def em_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detector()
        function. The output returned a dict with the score  
        of each emotion for the provided text.
    '''
    # Get text from url
    text_to_analyze = request.args.get("textToAnalyze").strip()

    # Send text to the function
    text_analysis = emotion_detector(text_to_analyze)

    if text_analysis["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    # Store results in variables
    anger = f"'anger': {text_analysis['anger']}"
    disgust = f"'disgust': {text_analysis['disgust']}"
    fear = f"'fear': {text_analysis['fear']}"
    joy = f"'joy': {text_analysis['joy']}"
    sadness = f"'sadness': {text_analysis['sadness']}"
    dominant_emotion = f"The dominant emotion is {text_analysis['dominant_emotion']}"

    # Added to avoid the static analysis characters
    text = "For the given statement, the system response is"

    # Return response
    return f"{text} {anger}, {disgust}, {fear}, {joy} and {sadness}. {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    # This function initiates the rendering of the main application
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
