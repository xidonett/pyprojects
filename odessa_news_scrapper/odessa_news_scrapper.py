from bs4 import BeautifulSoup
import pandas as pd
import requests

class OdessaNewsScrapper():
    
    def __init__( self, first_page:int = 1, last_page:int = 2, link:str = "https://on.od.ua/category/news/2-odessa/page/", csv_file:str = "odessa_news.csv" ) -> None:
        
        titles = []
        dates = []
        views = []

        for i in range(first_page, last_page+1):
            
            print(str(i)+" page of "+str(last_page))

            raw_code = requests.get(link+str(i)).content
            soup = BeautifulSoup(raw_code, "html.parser")
            
            sc_titles = soup.findAll( "h2", {"class" : "entry-title"} )
            sc_views = soup.findAll( "span", {"class" : "post-views"} )
            sc_dates = soup.findAll( "span", {"class" : "posted-on"} )
            
            sc_formatted_dates = []
            for j in range(0, len(sc_dates)):
                sep_date = sc_dates[j].get_text().split(" ")
                sc_formatted_dates.append(sep_date[0])

            for i in range(0, len(sc_titles)):
                titles.append(sc_titles[i].get_text())
                dates.append(sc_formatted_dates[i])
                views.append(sc_views[i].get_text())
        
        data = {"Название статьи": titles, "Дата": dates, "Кол-во просмотров": views}
        
        df = pd.DataFrame(data)
        df.to_csv(csv_file, encoding="utf-8-sig", )
        
        print("Done.")

odessa_news = OdessaNewsScrapper(1, 350)