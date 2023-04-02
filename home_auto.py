from __future__ import print_function
from auth import spreadsheet_service

def create():
    spreadsheet_details = {
    'properties': {
        'title': 'Python-google-sheets-demo'
        }
    }
    request = spreadsheet_service.spreadsheets().get(spreadsheetId='1lURurUl-nk0BKDgru6DRrLZiqwfYNzAkl6fWR4duy7Q', ranges=[], includeGridData=True)
    response = request.execute()
    rows = response["sheets"][0]["data"][0]["rowData"]
    #print('req:', response["sheets"][0]["data"][0]["rowData"])

    formatted_data = []

    for row in rows:
        formatted_row = []
        for item in row["values"]:
            formatted_row.append(item["userEnteredValue"]["stringValue"])
        formatted_data.append(formatted_row)

    print('end output:', formatted_data)

    




create()