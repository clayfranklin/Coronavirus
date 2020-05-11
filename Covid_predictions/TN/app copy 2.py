import numpy as np
import pandas as pd
from flask import Flask, jsonify, Response, render_template
import datetime
from datetime import timedelta
import time
from splinter import Browser
from bs4 import BeautifulSoup

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


@app.route("/")
def index():
    """Return the homepage."""

    return render_template("index.html")

#get latest data and store to right path
@app.route("/scrape")
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': "C:/Users/clayf/Documents/web-scraping-challenge/Mission_to_Mars/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)
    
browser = init_browser()
url = 'https://www.tn.gov/health/cedep/ncov/data/downloadable-datasets.html'
browser.visit(url)
browser.click_link_by_partial_text('County')

import shutil
shutil.move("C:/Users/clayf/Downloads/Public-Dataset-County-New.xlsx", "C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/daily.csv")



@app.route("/TNDeptHealth_overtime")
def viz_overtime():
    
    #add today's date 
    date = datetime.datetime.today()
    date_modify=str(date)
    date_to_add = date_modify[0:10]
    TN_county["Date"]=date_to_add

    #add this date if your slacking and did it after midnight, SLACKER!!!! 
    # d = datetime.datetime.today() - timedelta(days=1)
    # date_modify=str(d)
    # date_to_add2 = date_modify[0:10]
    # TN_county["Date"]=date_to_add2


    #Read in and clean Population by County data
    TNpop = pd.read_csv("Coronavirus/Covid_predictions/TN/Resources/Population Estimates by County.csv")
    TNpop= TNpop.drop([96])
    TNpop = TNpop.drop([0])
    TNpop["Population Estimates by County"]= TNpop["Population Estimates by County"].str.split(" County", n = 1, expand = True)
    TNpop = TNpop.rename(columns={'Population Estimates by County': 'County'})
    TN_county_populations = TNpop.rename(columns={'Unnamed: 1': 'Population'})
    TN_county_populations["Population"] = TN_county_populations["Population"].str.replace(",","").astype(int)
    
    # Read in daily info
    TN=pd.read_excel("C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/Public-Dataset-County-New (5).xlsx")
    
    #Merge daily with population
    withPop=TN.merge(TN_county_populations,left_on='COUNTY',right_on='County', how='left')
    
    #create new columns with data
    TN_data["Percentage of County with Coronavirus"] = round((TN_data["Positive"]/TN_data["Population"])*100,3)
    TN_data=TN_data.sort_values("Positive", ascending=False).reset_index(drop=True)
    TN_data["Percent of County Tested"] = round(((TN_data["Positive"]+TN_data["Negative"])/TN_data["Population"])*100,1)
    
    #Export daily data combined with past
    TN_data.to_csv("C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/Synched/TN_cases_yesterday.csv", index=False)
    
    #export daily data for storage
    TN_data.to_csv('C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/up_to_this_day_' + date_to_add +'.csv',index=False)
    
    #send data to flask route as json for data visulization
    time_counties = TN_data.to_json(orient = 'columns')

    return time_counties


# @app.route("/TNDeptHealth_overall")
# def viz_overall():
#     daily = "https://www.tn.gov/health/cedep/ncov.html"
#     viral = pd.read_html(daily)
#     df = viral[0]
#     testing = df.drop([3])
#     date = datetime.datetime.today()
#     date_modify = str(date)
#     date_for_export = date_modify[0:10]
#     testing["Date"] = date_for_export
#     testing.to_csv('C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/' + date_for_export +'_overall.csv',index=False)
#     viral_overall = testing.to_json(orient='columns')

#     return viral_overall


# @app.route("/TNDeptHealth_age")
# def viz_age():
#     daily = "https://www.tn.gov/health/cedep/ncov.html"
#     viral = pd.read_html(daily)
#     df2 = viral[2]
#     group_cleaned = df2.drop([9])
#     group_cleaned.columns = ['Age Ranges of Confirmed Cases', 'Number_Cases', 'Number of Deaths']
#     date = datetime.datetime.today()
#     date_modify = str(date)
#     date_for_export = date_modify[0:10]
#     group_cleaned["Date"] = date_for_export
#     group_cleaned.to_csv('C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/' + date_for_export +'_age.csv',index=False)
#     viral_age = group_cleaned.to_json(orient='columns')

#     return viral_age

# @app.route("/TNDeptHealth_counties")
# def viz_counties():
    
#     #Scrape tn.gov for coronavirus data, remove uncessecary info 
#     daily = "https://www.tn.gov/health/cedep/ncov.html"
#     viral = pd.read_html(daily)
#     df2 = viral[8]
#     TN_county = df2[:-3]
#     TN_county.columns = ['County', 'Positive', 'Negative', 'Death']
#     TN_county["County"]=TN_county["County"].str.split(" County", expand = True)

    
#     #Read in and clean Population by County data
#     TNpop = pd.read_csv("Coronavirus/Covid_predictions/TN/Resources/Population Estimates by County.csv")
#     TNpop= TNpop.drop([96])
#     TNpop = TNpop.drop([0])
#     TNpop["Population Estimates by County"]= TNpop["Population Estimates by County"].str.split(" County", n = 1, expand = True)
#     TNpop = TNpop.rename(columns={'Population Estimates by County': 'County'})
#     TN_county_populations = TNpop.rename(columns={'Unnamed: 1': 'Population'})
#     TN_county_populations["Population"] = TN_county_populations["Population"].str.replace(",","").astype(int)
    
#     #Merge two dataframes and perform calculations, and add a date column
#     TN_data = TN_county_populations.merge(TN_county,left_on='County',right_on='County', how='left')
#     TN_data["Percentage of County Population"] = round((TN_data["Positive"]/TN_data["Population"])*100,3)
#     TN_data=TN_data.sort_values("Positive", ascending=False).reset_index(drop=True)
#     TN_data["Percent_Tested"] = round(((TN_data["Positive"]+TN_data["Negative"])/TN_data["Population"])*100,1)
#     TN_data.sort_values("Percent_Tested", ascending=False)
#     date = datetime.datetime.today()
#     date_modify = str(date)
#     date_for_export = date_modify[0:10]
#     TN_data["Date"] = date_for_export
#     TN_data.reset_index(drop=True)
    

#     #export data for storage
#     TN_data.to_csv('C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/' + date_for_export +'_counties.csv',index=False)
    
#     #send data to flask route as json for data visulization
#     viral_counties = TN_data.to_json(orient='columns')

#     return viral_counties

# @app.route("/TNDeptHealth_gender")
# def gender():
#     daily = "https://www.tn.gov/health/cedep/ncov.html"
#     viral = pd.read_html(daily)
#     df3=viral[7]
#     date = datetime.datetime.today()
#     date_modify = str(date)
#     date_for_export = date_modify[0:10]
#     df3["Date"] = date_for_export
#     df3.to_json(orient='columns')
#     df3.to_csv('C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/' + date_for_export +'_gender.csv',index=False)

#     return df3

# @app.route("/TNDeptHealth_ethnicity")
# def ethnicity():
#     daily = "https://www.tn.gov/health/cedep/ncov.html"
#     viral = pd.read_html(daily)
#     df=viral[4]
#     df.iloc[2,0]='Hispanic'
#     date = datetime.datetime.today()
#     date_modify = str(date)
#     date_for_export = date_modify[0:10]
#     df["Date"] = date_for_export
#     df.to_csv('C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/' + date_for_export +'_ethnicity.csv',index=False)

#     df.to_json(orient='columns')

#     return df

# if __name__ == '__main__':
#     app.run(debug=True)
