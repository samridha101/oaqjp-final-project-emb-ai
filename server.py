from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the home page (index.html) when the user accesses the root URL.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Processes the input text, detects emotions, and returns the result.
    
    Handles both GET and POST requests to process the provided text and 
    return the emotion analysis result.
    """
    if request.method == 'GET':
        text_to_analyze = request.args.get("textToAnalyze")
    elif request.method == 'POST':
        text_to_analyze = request.form.get("textToAnalyze")
    else:
        return "Invalid method"  # If neither GET nor POST is used.

    if not text_to_analyze:
        return "Invalid text! Please try again."  # Handle blank input

    response = emotion_detector(text_to_analyze)

    if response is None or response['dominant_emotion'] is None:
        return "Invalid text! Please try again."  # Handle invalid or error responses

    result = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )
    return result

if __name__ == '__main__':
    """
    Starts the Flask web application on localhost:5000.
    """
    app.run(debug=True)
