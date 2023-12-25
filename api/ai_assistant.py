from outlook_calendar_api import OutlookCalendarAPI
from outlook_docs_api import OutlookDocsAPI
from outlook_mail_api import OutlookMailAPI
from note_factory import NoteFactory

class AIAssistant:
    def __init__(self, voice_processing_service, text_processing_service):
        self.voice_service = voice_processing_service
        self.text_service = text_processing_service
        # Initialize Outlook Calendar API
        client_id = "<Your-Client-ID>"
        client_secret = "<Your-Client-Secret>"
        self.calendar_api = OutlookCalendarAPI(client_id, client_secret)
        self.mail_api = OutlookMailAPI(client_id, client_secret)
        self.docs_api = OutlookDocsAPI(client_id, client_secret)

    def process_voice_command(self, voice_data):
        text = self.voice_service.convert_to_text(voice_data)
        command, content = self.text_service.parse_command(text)

        if command == 'prepare_for_question':
            return content
        elif command == 'query_model':
            return content
        # ... [handle other commands] ...

        return "Unknown command"

    def process_text_command(self, text):
        command, content = self.text_service.parse_command(text)

        if command == 'schedule_meeting':
            return self.calendar_api.schedule_meeting(content)
        elif command == 'take_note':
            # Extract note type from the command
            note_type, note_content = self.extract_note_type_and_content(content)

            note_factory = NoteFactory()
            note = note_factory.get_note(note_type)
            note.create_note(note_content)
            return "Note created successfully"
        elif command == 'send_email':
            return self.mail_api.send_email(content)
        # Add more command processing as needed

        return "Command not recognized"
    
    def extract_note_type_and_content(self, content):
        """
        Extracts the note type and content from the command.
        """
        # Logic to extract note type and content from the command
        note_content = content
        
        return note_type, note_content

    # Additional methods for handling specific tasks can be added here
