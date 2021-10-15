import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon') #download lexicon

file="mypost.xlsx"
xl=pd.ExcelFile(file) #Read the excel file
dfs=xl.parse(xl.sheet_names[0]) #Prsing data sheet to excel frame
dfs=list(dfs['Facebook'])
print(dfs)
sid=SentimentIntensityAnalyzer()
str1="Updated"
for data in dfs:
    data=str(data)
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])