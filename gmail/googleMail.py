import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
from email.mime.text import MIMEText
import time

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def main():
    """Shows basic usage of the Gmail API.
    Prints the sender, subject, and snippet of the last 25 emails.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)
        result = service.users().getProfile(userId='me').execute()
        messages = service.users().messages().list(
            userId='me',
            maxResults=10, 
            labelIds=['INBOX']
        ).execute()
        if not messages.get('messages'):
            print("No messages found.")
            return
        
        for message in messages['messages']:
            # Add delay between requests to avoid rate limits
            time.sleep(1)
            
            msg = service.users().messages().get(
                id=message['id'],
                userId='me'
            ).execute()

            headers = msg.get('payload', {}).get('headers', [])
            subject = None
            for header in headers:
                if header['name'] == 'Subject':
                    subject = header['value']
                    break

            parts = msg.get('payload', {}).get('parts', [])
            body_text = ''
            
            for part in parts:
                if part.get('mimeType') == 'text/plain':
                    data = part.get('body', {}).get('data')
                    try:
                        decoded_data = base64.urlsafe_b64decode(data)
                        text = decoded_data.decode('utf-8')
                        body_text += text
                    except (TypeError, UnicodeDecodeError):
                        continue

            if subject and body_text.strip():
                print(f"Subject: {subject}")
                print(f"Body: {body_text}\n{'-'*50}")


    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()