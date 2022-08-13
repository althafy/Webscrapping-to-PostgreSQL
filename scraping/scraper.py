import pandas as pd

def Scraper(link):
    data = pd.read_html(link)

    return data

