from outlook_docs_api import OutlookDocsAPI 

class TranscriptionNote():
    def create_note(self, content):
        # Logic to transcribe and save content to Google Doc
        doc_title = "Transcription Note"
        google_docs_api = OutlookDocsAPI()
        google_docs_api.create_document(doc_title, content)