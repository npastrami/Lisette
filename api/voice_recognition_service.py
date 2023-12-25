import torch
from transformers import WhisperForConditionalGeneration, WhisperProcessor

class VoiceRecognitionService:
    def __init__(self):
        self.model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v3")
        self.processor = WhisperProcessor.from_pretrained("openai/whisper-large-v3")

    def convert_to_text(self, audio_path):
        """
        Converts voice data to text using OpenAI's Whisper model.
        :param audio_path: Path to the audio file for voice recognition.
        :return: Transcribed text.
        """
        # Load audio and perform inference
        audio_input = self.processor(audio_path, return_tensors="pt")
        with torch.no_grad():
            logits = self.model.generate(**audio_input)

        # Decode the model output into text
        transcription = self.processor.batch_decode(logits, skip_special_tokens=True)
        return transcription[0]