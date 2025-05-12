from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    if request.method == 'GET':
        # For GET request, get the query parameter
        text_to_analyze = request.args.get("textToAnalyze")
    elif request.method == 'POST':
        # For POST request, get the form data
        text_to_analyze = request.form.get("textToAnalyze")
    else:
        return "Invalid method"

    if not text_to_analyze:
        return "No text to analyze provided."

    # Call the emotion_detector function to analyze the text
    response = emotion_detector(text_to_analyze)
    
    if response is None:
        return "Invalid input or server error."
    
    result = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )
    return result

if __name__ == '__main__':
    app.run(debug=True)
