import threading
from O365 import Account

class OutlookCalendarAPI:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(OutlookCalendarAPI, cls).__new__(cls)
        return cls._instance

    def __init__(self, client_id, client_secret):
        self.account = Account((client_id, client_secret))
        self.schedule = self.account.schedule()

    def schedule_meeting(self, text_processing_subject, text_processing_location, attendees, start, end):
        """
        Schedules a meeting in Outlook Calendar based on the provided content.
        """
        # Check for conflicts
        if self.check_for_conflicts(start, end, attendees):
            print('WARNING: There is a conflict in the schedule.')
            # Additional logic for handling conflicts
            return

        # No conflict, create the event
        event = self.schedule.new_event(
            subject=text_processing_subject,
            location=text_processing_location,
            attendees=attendees,
            start=start,
            end=end
        )
        event.save()

    def check_for_conflicts(self, start, end, attendees):
        """
        Checks for scheduling conflicts.
        """
        events = self.schedule.get_events()  # or a more specific query based on date/time
        for event in events:
            if event.start < end and event.end > start and set(event.attendees).intersection(set(attendees)):
                print('The conflicting event is:', event)
                return True
        return False
