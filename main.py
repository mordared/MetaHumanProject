from flask import Flask, render_template, request, jsonify
import openai
import os
import requests

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/transcribe", methods=['POST'])
def transcribe():
  if 'file' not in request.files:
    return jsonify({'error': 'No file part'})

  audio_file = request.files['file']
  if audio_file.filename == '':
    return jsonify({'error': 'No selected file'})

  try:
    transcript = openai.Audio.transcribe("Whisper-1", audio_file)
    print("hello, world")
    print(transcript)
    return jsonify({'transcript': transcript})
  except Exception as e:
    return jsonify({'error': str(e)})  
  #Transcribe the given audio to text using Whisper.

@app.route("/ask", methods=['POST'])
def ask():
  user_input = request.get_json()

  try:
    response = openai.Completion.create(
      engine="davinci",
      prompt=user_input,
      max_tokens=50
    )
    chatgpt_response = response.choices[0].text
    print (jsonify({'response': chatgpt_response}))
    return jsonify({'response': chatgpt_response})
  except Exception as e:
    return jsonify({'error': str(e)})
  #Generate a ChatGPT response from the given conversation

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
