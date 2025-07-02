from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_homepage():
    return render_template("index.html")

@app.route('/emotionDetector', methods=["GET"])
def emotion_detection_analysis() -> str:
    text = request.args["textToAnalyze"]
    result = emotion_detector(text)
    response = "For the given statement, the system response is "
    response += "'anger'" + ": " + str(result['anger']) + ", "
    response += " 'disgust'" + ": " + str(result['disgust']) + ", "
    response += " 'fear'"  + ": " + str(result['fear']) + ", "
    response += " 'joy'" + ": " + str(result['joy']) + ", "
    response += " and 'sadness'" + ": " + str(result['sadness']) + "."
    response += "The dominant emotion is " + result['dominant_emotion']
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)