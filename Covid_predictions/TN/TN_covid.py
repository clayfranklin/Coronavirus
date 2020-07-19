import numpy as np
import pandas as pd
from flask import Flask, jsonify, Response, render_template
import datetime
from datetime import timedelta
import time
from splinter import Browser
from bs4 import BeautifulSoup
import shutil
import os


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': "C:/Users/clayf/Documents/web-scraping-challenge/Mission_to_Mars/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

@app.route("/")
def index():
    """Return the homepage."""
   
    return render_template("index.html")

#get latest data and store to right path
@app.route("/scrape")
def get_the_stuff():

    browser = init_browser()
    url = 'https://www.tn.gov/health/cedep/ncov/data/downloadable-datasets.html'
    browser.visit(url)
    browser.click_link_by_partial_text('County New')
    return render_template("index.html")

  

# @app.route("/scrape2")
# def get_more_stuff():

#     browser = init_browser()
#     url = 'https://www.tn.gov/health/cedep/ncov/data/downloadable-datasets.html'
#     browser.visit(url)
#     browser.click_link_by_partial_text('Daily')
#     print("data downloading, please wait")
#     return render_template("index.html")

# @app.route("/TNDeptHealth_totals_overtime")
# def viz_overall_overtime():
#     #move file to correct place
#     shutil.move("C:/Users/clayf/Downloads/Public-Dataset-Daily-Case-Info.xlsx", "C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/TN_DH/daily_total.xlsx")
#     time.sleep(5)
#     totals = pd.read_excel("Coronavirus/Covid_predictions/TN/Resources/TN_DH/daily_total.xlsx")
#     totals["DATE"]=totals["DATE"].astype(str)
#     total_TN = totals.to_json(orient = 'columns')
#     render_template("index.html")
#     return total_TN

@app.route("/TNDeptHealth_overtime")
def viz_overtime():
    #move file to correct place
    # time.sleep(5)
    # shutil.move("C:/Users/clayf/Downloads/Public-Dataset-County-New.xlsx", "C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/TN_DH/daily.xlsx")
    #add today's date 
    # date = datetime.datetime.today()
    # date_modify=str(date)
    # date_to_add = date_modify[0:10]
    

    #add this date if your slacking and did it after midnight, SLACKER!!!! 
    # d = datetime.datetime.today() - timedelta(days=1)
    # date_modify=str(d)
    # date_to_add2 = date_modify[0:10]
    # TN_county["Date"]=date_to_add2


    #Read in and clean Population by County data
    # TNpop = pd.read_csv("C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/Population Estimates by County.csv")
    # TNpop= TNpop.drop([96])
    # TNpop = TNpop.drop([0])
    # TNpop["Population Estimates by County"]= TNpop["Population Estimates by County"].str.split(" County", n = 1, expand = True)
    # TNpop = TNpop.rename(columns={'Population Estimates by County': 'County'})
    # TN_county_populations = TNpop.rename(columns={'Unnamed: 1': 'Population'})
    # TN_county_populations["Population"] = TN_county_populations["Population"].str.replace(",","").astype(int)
    
    # Read in daily info
    # time.sleep(5)
    TN=pd.read_excel("C:/Users/clayf/Downloads/Public-Dataset-County-New.xlsx")
    TN["DATE"]=TN["DATE"].astype(str)
    
    #Merge daily with population
    # withPop=TN.merge(TN_county_populations,left_on='COUNTY',right_on='County', how='left')
    
    # #create new columns with data
    # withPop["Percentage of County with Coronavirus"] = round((withPop["TOTAL_ACTIVE"]/withPop["Population"])*100,3)
    # withPop["Percent of County Tested"] = round(((withPop["TOTAL_TESTS"]+withPop["NEG_TESTS"])/withPop["Population"])*100,1)
    davidson=TN[TN["COUNTY"] == "Davidson"]
    davidson.to_csv("C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/TN_DH/forGDS.csv", index=False, encoding ="UTF-8")
    #send data to flask route as json for data visulization
    time_counties = davidson.to_json(orient = 'columns')

    
    return time_counties


@app.route("/Davidson")
def viz_davidson():
    TN=pd.read_excel("C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/TN_DH/daily.xlsx")
    TN["DATE"]=TN["DATE"].astype(str)
    davidson=TN[TN["COUNTY"] == 'Davidson']
    davidsonTN=davidson.to_json(orient = 'columns')
    return davidsonTN

@app.route("/shelby")
def shelby():
    TN=pd.read_excel("C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/TN_DH/daily.xlsx")
    TN["DATE"]=TN["DATE"].astype(str)
    shelby=TN[TN["COUNTY"] == 'Shelby']
    shelbyTN=shelby.to_json(orient = 'columns')
    return shelbyTN

@app.route("/Knox")
def knox():
    TN=pd.read_excel("C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/TN_DH/daily.xlsx")
    TN["DATE"]=TN["DATE"].astype(str)
    knox=TN[TN["COUNTY"] == 'Knox']
    knoxTN=knox.to_json(orient = 'columns')
    return knoxTN

@app.route("/Hamilton")
def hamilton():
    TN=pd.read_excel("C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/TN_DH/daily.xlsx")
    TN["DATE"]=TN["DATE"].astype(str)
    hamilton=TN[TN["COUNTY"] == 'Hamilton']
    hamiltonTN=hamilton.to_json(orient = 'columns')
    return hamiltonTN

@app.route("/Rutherford")
def rutherford():
    TN=pd.read_excel("C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/TN_DH/daily.xlsx")
    TN["DATE"]=TN["DATE"].astype(str)
    rutherford=TN[TN["COUNTY"] == 'Rutherford']
    rutherfordTN=rutherford.to_json(orient = 'columns')
    return rutherfordTN

@app.route("/sumner")
def sumner():
    TN=pd.read_excel("C:/Users/clayf/Downloads/Public-Dataset-County-New.xlsx")
    TN["DATE"]=TN["DATE"].astype(str)
    sumner=TN[TN["COUNTY"] == 'Sumner']
    sumnerTN=sumner.to_json(orient = 'columns')
    return sumnerTN


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

@app.route("/TNDeptHealth_counties")
def viz_counties():
    
    date = datetime.datetime.today()
    date_modify=str(date)
    date_to_add = date_modify[0:10]
    

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
    
    TN=pd.read_excel("C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/TN_DH/daily.xlsx")
    TN["DATE"]=TN["DATE"].astype(str)
    
    #Merge daily with population
    withPop=TN.merge(TN_county_populations,left_on='COUNTY',right_on='County', how='left')
    
    #create new columns with data
    withPop["Percentage of County with Coronavirus"] = round((withPop["TOTAL_ACTIVE"]/withPop["Population"])*100,3)
    withPop["Percent of County Tested"] = round(((withPop["TOTAL_TESTS"]+withPop["NEG_TESTS"])/withPop["Population"])*100,1)

    all_counties = withPop.to_json(orient = 'columns')

    return all_counties

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

if __name__ == '__main__':
    app.run(debug=True)
