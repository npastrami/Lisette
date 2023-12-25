from flask import Flask, request, jsonify
from ai_assistant import AIAssistant
from text_processing_service import TextProcessingService
from voice_recognition_service import VoiceRecognitionService
from outlook_calendar_api import OutlookCalendarAPI
from outlook_docs_api import OutlookDocsAPI
from outlook_mail_api import OutlookMailAPI

# Initialize Flask app
app = Flask(__name__)

voice_processing_service = VoiceRecognitionService()
text_service = TextProcessingService()
ai_assistant = AIAssistant(voice_processing_service, text_service)

@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.json
    audio_path = data.get('audio_path')  # Expecting a file path to the audio file
    text = voice_processing_service.convert_to_text(audio_path)
    response = ai_assistant.process_text_command(text)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)