'''PSR Review Process'''
import os
import requests

class PSRReview:
    def __init__(self):
        self.host_name = os.getenv("hostName")
        self.entry_point = os.getenv("entryPoint")
        self.notes_url_template = os.getenv("notesUrl")
        self.clientID = os.getenv("clientid")
        self.clientSecret = os.getenv("clientsecret")

    def get_case_notes(self, case_number: str, token: str):

        '''Fetch case notes for a given case number using the provided token.'''

        if not case_number or not token:
            raise ValueError("Both case_number and token are required.")
        notesURL = self.host_name + self.entry_point + self.notes_url_template.format(caseNumber=case_number)
        response = requests.get(notesURL, headers={"client_id": self.clientID, "client_secret": self.clientSecret })
        return (response.content)