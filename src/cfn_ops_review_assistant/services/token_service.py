import os
import requests
import time
import json
import uuid
from http.cookies import SimpleCookie
import sys, time, datetime
from dotenv import load_dotenv
from cfn_ops_review_assistant.utils.path_utils import get_project_root
load_dotenv(get_project_root() / ".env")

class Commlinksession():
    """
    A class to create a CFN session ID and cookie jar in order to login to Comm Ave using API
    
    Argument : Environment - qa or dev or prod
    
    Returns : CFN session ID
    """
    def __init__(self,environment):
        """
        Initialize the required configurations based on the environment
        """

        self.grant_type = os.getenv("prod_grant_type")
        self.client_id = os.getenv("prod_client_id")
        self.client_secret = os.getenv("prod_client_secret")
        self.scope = os.getenv("prod_scope")
        self.session_payload = json.loads(os.getenv("prod_payload"))
        self.session_uri = os.getenv("prod_session_api")
        self.session_url = os.getenv("prod_session_url")        
        self.auth_token_headers = json.loads(os.getenv("auth_token_headers"))
        self.session_id_headers = json.loads(os.getenv("session_id_headers"))
        self.auth_token_uri = os.getenv("auth_token_uri")
        self.cookie_dict = json.loads(os.getenv("cookie_dict"))
        self.cookie_path = os.getenv("cookie_path")
        self.cookie_domain = os.getenv("cookie_domain")
        self.cookie_expires = os.getenv("cookie_expires")
        
    def session_creator(self):
        """
        core function to generate a CFN session ID and cookie jar to test the browser is launching without any issues
        """
        bot_output = {"flag":False, "sessionid":""}
        auth_payload = {
                        "grant_type": self.grant_type,
                        "client_id": self.client_id ,
                        "client_secret": self.client_secret,
                        "scope": self.scope
                    }
        auth_token_uri = requests.post(self.auth_token_uri,data = auth_payload,headers=self.auth_token_headers)
        auth_token_response = auth_token_uri.json()
        auth_token = auth_token_response["access_token"]
        #print(auth_token)
        #Add auth token to headers for creatng a session id
        self.session_id_headers["Authorization"] = 'Bearer ' + auth_token
        new_guid = uuid.uuid4()
        new_guid_str = str(new_guid)
        session_id = new_guid_str
        self.session_payload["sessionId"] = session_id
        self.session_payload = json.dumps(self.session_payload)
        #print(self.session_payload)
        #print(self.session_id_headers)
        #print(self.session_uri)
        session_uri_request = requests.post(self.session_uri,data = self.session_payload,headers = self.session_id_headers)
        #print(session_uri_request.status_code)
        session_uri_reponse = session_uri_request.json()
        #print(session_uri_reponse)
        session_id = session_uri_reponse["sessionId"]
        #print(session_id)
        # Create a requests session object
        session = requests.Session()
        # Define your session ID
        #session_id = "70608163-b48c-4624-ad02-52ddb815e12e"
        #session_id = session_id
        #print(session_id)
        # This allows for easy manipulation of cookie attributes
        cookie = SimpleCookie()
        cookie["CFNSession"] = session_id
        cookie["CFNSession"]["path"] = self.cookie_path
        cookie["CFNSession"]["domain"] = self.cookie_domain
        cookie["CFNSession"]["expires"] = self.cookie_expires
        # Convert the SimpleCookie to a format compatible with requests' cookies
        cookie_dict = {name: morsel.value for name, morsel in cookie.items()}
        
        # Add the cookie to the session's cookie jar
        session.cookies.update(cookie_dict)
        #print(session.cookies)
        response = session.get(self.session_url)
        stats_code = response.status_code
        stats_content = response.text
        #print(stats_content)
        if (stats_code == 200 or stats_code == 201) and "You've been logged out" not in stats_content:
            bot_output["flag"] = True
            bot_output["sessionid"] = session_id
        return  bot_output["sessionid"]
   
    def __del__(self):
        pass