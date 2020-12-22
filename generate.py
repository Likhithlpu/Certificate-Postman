from PIL import Image , ImageDraw , ImageFont
import pandas as pd
import os
import getpass
import smtplib
import imghdr
from email.message import EmailMessage

Email_Address = input(str("Enter Your Email Adress:"))
Email_Password = getpass.getpass("Enter Password:")


df = pd.read_csv('example.csv')

font = ImageFont.truetype("arialbd.ttf",80)
for index,j in df.iterrows():
    print(j)
    msg = EmailMessage()
    msg['Subject'] = 'Subject '
    msg['From'] = Email_Address
    msg.set_content('Content')
    msg['To'] = (j['Email'])

    img = Image.open("certificate.jpg")
    draw = ImageDraw.Draw(img)
    draw.text(xy=(835,750),text= '{}'.format(j['Name'].upper()),fill=(0,0,0),font = font)
    saveimg = img.save('{}.jpg'.format(j['Name']))


    files = ['{}.jpg'.format(j['Name'])]
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
        
        msg.add_attachment(file_data, maintype ='image', subtype = file_type , filename = file_name)

 
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(Email_Address, Email_Password)
        smtp.send_message(msg)


