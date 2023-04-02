# auth.py
from __future__ import print_function
from googleapiclient.discovery import build 
from google.oauth2 import service_account
SCOPES = [
'https://www.googleapis.com/auth/spreadsheets'
]
credentials = service_account.Credentials.from_service_account_file('primal-quanta-380801-fecceeb2d3fa.json', scopes=SCOPES)
spreadsheet_service = build('sheets', 'v4', credentials=credentials)