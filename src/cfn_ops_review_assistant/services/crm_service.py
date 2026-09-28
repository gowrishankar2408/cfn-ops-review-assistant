import os
import requests

class CRMService:
    def __init__(self):
        self.host_name = os.getenv("hostName")
        self.entry_point = os.getenv("entryPoint")
        self.endpoint = os.getenv("endpoint")
        self.clientID = os.getenv("clientid")
        self.clientSecret = os.getenv("clientsecret")

    def get_case_notes(self, case_number: str, token: str):

        '''Fetch case notes for a given case number using the provided token.'''

        if not case_number or not token:
            raise ValueError("Both case_number and token are required.")
        notesURL = self.host_name + self.entry_point + self.endpoint.format(caseNumber=case_number) + 'notes'
        response = requests.get(notesURL, headers={"client_id": self.clientID, "client_secret": self.clientSecret })
        return (response.content)

    def close_case(self, case_number: str, token: str):
        '''Close the case for the given case number using the provided token.'''
        if not case_number or not token:
            raise ValueError("Both case_number and token are required.")
        closeURL = self.host_name + self.entry_point + self.endpoint.format(caseNumber=case_number) + 'close'
        response = requests.post(closeURL, headers={"client_id": self.clientID, "client_secret": self.clientSecret })
        return response.content