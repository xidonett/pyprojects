import requests
from bs4 import BeautifulSoup
import pandas

def crawl(max_page = 0, url = 'google.com'):

    p_labels = []
    p_prices = []
    p_links = []

    products = []

    page = 1
    while page < max_page:

        print("Page nr.",page)

        source_code = requests.get(url+str(page))
        raw_text = source_code.content
        soup = BeautifulSoup(raw_text, "html.parser")

        for offer in soup.findAll('td', {'class':'offer promoted'}):

            p_label = offer.find('a', {'class':'marginright5 link linkWithHash detailsLink'}).strong.get_text()
            p_price = offer.find('p', {'class': 'price'}).strong.get_text()
            p_link = offer.find('a', {'class':'marginright5 link linkWithHash detailsLink'})['href']

            p_labels.append(p_label)
            p_prices.append(p_price)
            p_links.append(p_link)

        page+=1
    products.append([p_labels, p_prices, p_links])
    print("Done.")
    return products
res = crawl(url="https://www.olx.ua/list/q-shoes/?page=", max_page = 43)

def csv_export(results_arr = [], csv_file_path=r"generated.csv"):
    print("Exporting to .csv file ("+csv_file_path+")")
    pandas_dict = {
        'Product name': results_arr[0][0], 
        'Price': results_arr[0][1],
        'Link': results_arr[0][2]
    }

    df = pandas.DataFrame(pandas_dict)
    df.to_csv(csv_file_path, encoding = "utf-8-sig")
    print("Successfully exported.")