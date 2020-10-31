import numpy as np
import pandas as pd
import yfinance as yf
import os 

def pull():
    try:
        company_list = pd.read_csv("constituents.csv")
    except:
        print("Missing constituents.csv.")
        x = input("EXIT")
        if x != "awpdopoijd":
            return 1

    sector_list = []
    for sector in company_list["Sector"]:
        sector_list.append(sector)

    sector_list = list(set(sector_list))

    for i in range(0, len(sector_list)):
        sector_list[i] = sector_list[i].replace(" ", "_")

    for sector in sector_list:
        exec(sector+" = pd.DataFrame()")

    for i in range(0, len(company_list)):  
        ticker = company_list["Symbol"].iloc[i]
        sector = company_list["Sector"].iloc[i].replace(" ", "_")
        try:
            exec(sector+'["'+ticker+'"] = yf.Ticker(ticker).history(period="10y")["Close"]')
            print(ticker + " added to " + sector+".")
        except:
            print(ticker + " failed!")

    for sector in sector_list:
        exec(sector+" = "+sector+".pct_change().fillna(0)")

    #!mkdir pulled-data
    folder_name = str(input("Write to: "))
    os.mkdir(folder_name)

    for sector in sector_list:
        print(sector+" is writing.")
        #exec(sector+".to_csv('"+directory+"pulled-data/"+sector+".csv')")
        exec(sector+".to_csv('"+folder_name+"/"+sector+".csv')")

    x = input("EXIT")

    if x != 0:
        return 0

pull()
