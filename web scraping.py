# code for scraping html code
import requests

head = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'}
for sector in range(102,118):
    for bhk in range(1,5):
        url = (f"https://www.99acres.com/{bhk}-bhk-flats-in-sector-{sector}-gurgaon-ffid")
        r = requests.get(url, headers=head)   
        # save html file 
        with open(f'D:\power Bi project\gurugram property\scrape html\{bhk}in{sector}.html', 'w') as file:
            file.write(r.text)


    