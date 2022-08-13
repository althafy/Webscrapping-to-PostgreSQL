import pandas as pd
import os

from scraping import scraper
from scraping import transformer
from sqlalchemy import create_engine

if __name__ == '__main__':

    #ETL - Extract
    link = 'https://id.wikipedia.org/wiki/Daftar_miliarder_Forbes'
    data = scraper.Scraper(link)

    #ETL- Transform
    df = transformer.Transformer(data)
    
    #ETL - Load
    path_config = os.getcwd()
    with open (path_config + '\config\config.conf', 'r') as file:
        conf = file.readlines()

    db = {}
    for line in conf:
        line = line.replace('\n','').split('=')
        if len(line) == 2:
            db[line[0]] = line[1]

    #Connection DB
    
    conn_string = conn_string = f"postgresql+psycopg2://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"
    engine = create_engine(conn_string)
    
    df.to_sql(name = 'webscrapping', con = engine, if_exists = 'replace', index = False)
    



    