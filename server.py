from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    if request.method == 'GET':
        text_to_analyze = request.args.get("textToAnalyze")
    elif request.method == 'POST':
        text_to_analyze = request.form.get("textToAnalyze")
    else:
        return "Invalid method"

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
    app.run(debug=True)
