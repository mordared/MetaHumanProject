from flask import Flask, render_template
import openai
import os




OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/transcribe", methods=['POST'])
def transcribe():
  #Transcribe the given audio to text using Whisper.
  return null

@app.route("/ask", methods=['POST'])
def ask():
  #Generate a ChatGPT response from the given conversation
  return null

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
