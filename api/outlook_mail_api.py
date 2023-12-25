import threading
from O365 import Account, FileSystemTokenBackend

class OutlookMailAPI:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(OutlookMailAPI, cls).__new__(cls)
        return cls._instance

    def __init__(self, client_id, client_secret):
        token_backend = FileSystemTokenBackend(token_path='.', token_filename='o365_token.txt')
        self.account = Account((client_id, client_secret), token_backend=token_backend)
        self.mailbox = self.account.mailbox()

    def send_email(self, recipient, subject, content):
        """
        Sends an email through Outlook 365.
        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param content: The body content of the email.
        """
        new_message = self.mailbox.new_message()
        new_message.to.add(recipient)
        new_message.subject = subject
        new_message.body = content
        new_message.send()
