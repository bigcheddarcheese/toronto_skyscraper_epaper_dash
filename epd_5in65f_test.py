from __future__ import print_function
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
imagedir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'images')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd5in65f
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from auth import spreadsheet_service

logging.basicConfig(level=logging.DEBUG)

try:
    # FETCH GOOGLE SPREADSHEET DATA
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
    # GOOGLE SPREADSHEET DATA FETCHED


    logging.info("epd5in65f Demo")
    
    epd = epd5in65f.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font30 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 40)
    
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Vimage = Image.new('RGB', (epd.width, epd.height), 0xffffff)  # 255: clear the frame
    Vimage = Vimage.transpose(Image.ROTATE_270)
    draw = ImageDraw.Draw(Vimage)
    draw.text((10, 160), formatted_data[0][0], font = font30, fill = epd.BLACK)
    draw.text((10, 200), formatted_data[0][1], font = font30, fill = epd.ORANGE)
    draw.text((10, 240), "Height: " + formatted_data[0][2], font = font30, fill = epd.GREEN)
    draw.text((10, 280), "Storeys: " + formatted_data[0][3], font = font30, fill = epd.BLUE)
    draw.text((10, 320), "Completion date: " + formatted_data[0][4], font = font30, fill = epd.RED)
    epd.display(epd.getbuffer(Vimage))
    time.sleep(3)
    
    Vimage = Image.open(os.path.join(imagedir, formatted_data[0][5]))
    epd.display(epd.getbuffer(Vimage))
    time.sleep(3)
    
    epd.Clear()
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd5in65f.epdconfig.module_exit()
    exit()
