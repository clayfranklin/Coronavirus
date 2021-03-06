import numpy as np
import pandas as pd
from flask import Flask, jsonify, Response, render_template
import datetime
from datetime import timedelta
import time

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


@app.route("/")
def index():
    """Return the homepage."""

    return render_template("index.html")


@app.route("/TNDeptHealth_overtime")
def viz_overtime():
    
    #Scrape tn.gov for coronavirus data, remove uncessecary info 
    daily = "https://www.tn.gov/health/cedep/ncov.html"
    viral = pd.read_html(daily)
    df2 = viral[5]
    TN_county = df2[:-3]
    TN_county=TN_county.rename(columns={'positives':'Positive','negatives':'Negative','Unnamed: 0': 'County', 'deaths':'Death'})
    TN_county["County"]=TN_county["County"].str.split(" County", expand = True)

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
    
    #Merge daily data with populationa and perform calculations
    TN_data = TN_county_populations.merge(TN_county,left_on='County',right_on='County', how='left')
    TN_data["Percentage of County Population"] = round((TN_data["Positive"]/TN_data["Population"])*100,3)
    TN_data=TN_data.sort_values("Positive", ascending=False).reset_index(drop=True)
    TN_data["Percent_Tested"] = round(((TN_data["Positive"]+TN_data["Negative"])/TN_data["Population"])*100,1)
    TN_data.sort_values("Percent_Tested", ascending=False)

    #Merge daily data to historical data
    to_update=pd.read_csv("C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/Synched/TN_cases_yesterday.csv")
    synched=TN_data.append(to_update, sort=True)
    TN_cases=synched.sort_values(["County", "Date"],ascending=[0,1])
    TN_cases["Duplicates"]=TN_cases["County"]+TN_cases['Date']
    TN_cases = TN_cases.drop_duplicates(subset="Duplicates", keep="last")
    TN_up_to_date=TN_cases.drop('Duplicates', axis=1)
    TN_up_to_date.reset_index(drop=True, inplace=True)
    time.sleep(5)
    TN_up_to_date.to_csv("C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/Synched/TN_cases_yesterday.csv")
    
    #export daily data for storage
    TN_up_to_date.to_csv('C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/up_to_this_day_' + date_to_add +'.csv',index=False)
    
    #send data to flask route as json for data visulization
    time_counties = TN_up_to_date.to_json(orient='columns')

    return time_counties


@app.route("/TNDeptHealth_overall")
def viz_overall():
    daily = "https://www.tn.gov/health/cedep/ncov.html"
    viral = pd.read_html(daily)
    df = viral[0]
    testing = df.drop([3])
    date = datetime.datetime.today()
    date_modify = str(date)
    date_for_export = date_modify[0:10]
    testing["Date"] = date_for_export
    testing.to_csv('C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/' + date_for_export +'_overall.csv',index=False)
    viral_overall = testing.to_json(orient='columns')

    return viral_overall


@app.route("/TNDeptHealth_age")
def viz_age():
    daily = "https://www.tn.gov/health/cedep/ncov.html"
    viral = pd.read_html(daily)
    df3 = viral[3]
    group_cleaned = df3.drop([10])
    age_groups = group_cleaned.rename(columns={'Age Ranges of Confirmed Cases.1': 'Number_Cases'})
    date = datetime.datetime.today()
    date_modify = str(date)
    date_for_export = date_modify[0:10]
    age_groups["Date"] = date_for_export
    age_groups.to_csv('C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/' + date_for_export +'_age.csv',index=False)
    viral_age = age_groups.to_json(orient='columns')

    return viral_age

@app.route("/TNDeptHealth_counties")
def viz_counties():
    
    #Scrape tn.gov for coronavirus data, remove uncessecary info 
    daily = "https://www.tn.gov/health/cedep/ncov.html"
    viral = pd.read_html(daily)
    df2 = viral[5]
    TN_county = df2[:-3]
    TN_county=TN_county.rename(columns={'positives':'Positive','negatives':'Negative','Unnamed: 0': 'County', 'deaths':'Death'})
    TN_county["County"]=TN_county["County"].str.split(" County", expand = True)

    
    #Read in and clean Population by County data
    TNpop = pd.read_csv("Coronavirus/Covid_predictions/TN/Resources/Population Estimates by County.csv")
    TNpop= TNpop.drop([96])
    TNpop = TNpop.drop([0])
    TNpop["Population Estimates by County"]= TNpop["Population Estimates by County"].str.split(" County", n = 1, expand = True)
    TNpop = TNpop.rename(columns={'Population Estimates by County': 'County'})
    TN_county_populations = TNpop.rename(columns={'Unnamed: 1': 'Population'})
    TN_county_populations["Population"] = TN_county_populations["Population"].str.replace(",","").astype(int)
    
    #Merge two dataframes and perform calculations, and add a date column
    TN_data = TN_county_populations.merge(TN_county,left_on='County',right_on='County', how='left')
    TN_data["Percentage of County Population"] = round((TN_data["Positive"]/TN_data["Population"])*100,3)
    TN_data=TN_data.sort_values("Positive", ascending=False).reset_index(drop=True)
    TN_data["Percent_Tested"] = round(((TN_data["Positive"]+TN_data["Negative"])/TN_data["Population"])*100,1)
    TN_data.sort_values("Percent_Tested", ascending=False)
    date = datetime.datetime.today()
    date_modify = str(date)
    date_for_export = date_modify[0:10]
    TN_data["Date"] = date_for_export
    
    

    #export data for storage
    TN_data.to_csv('C:/Users/clayf/Documents/Coronavirus/Covid_predictions/TN/Resources/' + date_for_export +'_counties.csv',index=False)
    
    #send data to flask route as json for data visulization
    viral_counties = TN_data.to_json(orient='columns')

    return viral_counties


if __name__ == '__main__':
    app.run(debug=True)
