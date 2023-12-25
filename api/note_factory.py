from notes_types.transcription import TranscriptionNote
from notes_types.summary import SummaryNote
from notes_types.outline import OutlineNote

class NoteFactory:
    note_class_map = {
        'transcription': TranscriptionNote,
        'summary': SummaryNote,
        'outline': OutlineNote
    }

    def get_note(self, note_type):
        note_class = self.note_class_map.get(note_type)
        if note_class:
            return note_class()
        raise ValueError(f"Unknown Note Type: {note_type}")