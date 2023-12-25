import threading
from O365 import Account

class OutlookDocsAPI:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(OutlookDocsAPI, cls).__new__(cls)
        return cls._instance

    def __init__(self, client_id, client_secret):
        self.account = Account((client_id, client_secret))
        self.storage = self.account.storage()  # Access OneDrive
        self.drive = self.storage.get_default_drive()  # Get default drive
        self.folder = self.drive.get_special_folder('documents')  # Get Documents folder

    def create_document(self, content, doc_name='New Document'):
        """
        Creates a new Word document in OneDrive with the specified content.
        :param content: Text content to be written in the document.
        :param doc_name: Name of the new document.
        """
        new_file = self.folder.upload_file(doc_name + '.docx')
        document = new_file.open_word_online()  # Open in Word Online for editing

        # Logic to add content to the document
        # This might require interacting with Word Online's specific APIs or SDKs

        pass

    # Additional methods for other document functionalities
