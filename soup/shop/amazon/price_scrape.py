"""Amazon price tracker"""
from icecream import ic
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

def main():

    # check if target is hit
    url = 'https://www.amazon.com/Metroid-Dread-Nintendo-Switch/dp/B097B1149G/ref=sr_1_2?crid=EJDQI713IFUI&keywords=nintendo+switch+metroid+dread&qid=1637567884&sprefix=nintendo+switch+metroi%2Caps%2C219&sr=8-2'
    # url = input('URL:')
    target_price = 60
    msg_dict = AmazonScrape(url).price_scraper(target_price)

    # send email if target is hit
    if msg_dict['status'] == 1 :
        load_dotenv()
        email1 = os.environ.get('EMAIL_ID_1')
        ic(email1)
        email2 = os.environ.get('EMAIL_ID_2')
        pwd = os.environ.get('PASSWORD')

        SE = SendEmail(email1,email2,pwd)
        SE.email_smtp(msg_dict)
        

@dataclass
class AmazonScrape:
    url : str

    def price_scraper(self, target):
        """scrape price for listed url
        Args:
            :param target : "Target price
            :type target : int"""
        # get url
        url = self.url

        # get response
        header = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language":"en-US,en;q=0.9"
        }
        response = requests.get(url, headers=header)
        webpage = response.text
        # parsed soup
        soup = BeautifulSoup(webpage,'lxml')
        
        # get price if listed
        listed = 1 ; not_listed = -1
        try:
            price = float(soup.find(id='priceblock_ourprice').get_text().split('$')[1])
            if price <= target :
                msg_dict ={
                    'url' : url,
                    'price' : price,
                    'target' : target,
                    'status' : listed
                }
        except AttributeError:
            # print('Price not listed')
            msg_dict = {'status' : not_listed}

        return msg_dict            

@dataclass
class SendEmail:
    """Email connector class
    Args : 
        :param email_from : sender email
        :param email_to : receiver email
        :param password : sender email password"""
    email_from : str
    email_to : str
    password : str
    

    def email_smtp(self, msg_string):
        """send email when price hits target"""
        port = 587
        smtp_server = "smtp.gmail.com"
        sender_email = self.email_from
        receiver_email = self.email_to
        password = self.password
        
        message = MIMEMultipart("alternative")
        message['Subject'] = "Price target hit"
        message['From'] = sender_email
        message['To'] = receiver_email

        text = f"""
            Price target has been reached\n
                url : {msg_string['url']}
                current_price : ${msg_string['price']}
                target_price : ${msg_string['target']}"""
        
        message.attach(MIMEText(text))
        ic(sender_email,password)
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email,password)
            server.sendmail(sender_email, receiver_email, message.as_string())


if __name__ == "__main__":
    main()