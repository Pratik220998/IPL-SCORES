from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

sauce = "https://www.cricbuzz.com/cricket-series/2810/indian-premier-league-2019/points-table"
page = requests.get(sauce, headers=headers)

soup = BeautifulSoup(page.text,features="html.parser")
#print(soup.prettify())

tbl = soup.find("table",class_="table cb-srs-pnts")
#print(tbl.prettify())

col_names = [x.get_text() for x in tbl.find_all('td',class_="cb-srs-pnts-th")]
col_names[5]='pts'
#print(col_names)

team_names = [x.get_text() for x in tbl.find_all('td',class_="cb-srs-pnts-name")]
#print(team_names)

pnt_tbl = [x.get_text() for x in tbl.find_all('td',class_="cb-srs-pnts-td")]
#print(pnt_tbl)

np_pnt_tbl = (np.array(pnt_tbl)).reshape(len(team_names),7)
np_pnt_tbl = np.delete(np_pnt_tbl,6,1)
np_pnt_tbl = np_pnt_tbl.astype(int)
#print(np_pnt_tbl)

t=1
while(t==1):
    print("1.Show current team standings/points table")
    print("2.Show the win/loss vs matches played graph of each team")
    print("3.Last match results")
    print("4.Next match schedule")
    x = int(input("Select your option: "))

    if(x==1):
        consol_tbl = pd.DataFrame(np_pnt_tbl,index=team_names,columns=col_names)
        consol_tbl.columns.name = "Teams"
        print(consol_tbl)

    elif(x==2):
        team_abr = []

        for team in team_names:
            short_form = ''
            for initial in team.split(' '):
               short_form = short_form + initial[0]
            team_abr.append(short_form)


        title = 'IPL 2019 Number of match won by teams'
        val_ticks = [1,2,3,4,5,6,7,8]
        lost_ticks=[1.4,2.4,3.4,4.4,5.4,6.4,7.4,8.4]


        plt.bar(val_ticks,np_pnt_tbl[:,1],width=0.4,color='g',alpha=0.6,label='Won')
        plt.bar(lost_ticks,np_pnt_tbl[:,2],width=0.4,color='r',alpha=0.6,label='Lost')
        plt.yticks(val_ticks)
        plt.ylabel("Matches")
        plt.xticks(val_ticks,team_abr,rotation='vertical')
        plt.grid(True)
        plt.legend()
        plt.title(title)

        plt.show()

    elif(x==3):
        q=1
        while(q==1):
            print("1.Chennai Super Kings")
            print("2.Royal Challengers Bangalore")
            print("3.Kolkata Knight Riders")
            print("4.Mumbai Indians")
            print("5.Delhi Capitals")
            print("6.Rajasthan Royals")
            print("7.Sunrisers Hyderabad")
            print("8.Kings XI Punjab")
            z = int(input("Enter your team: "))
            
            if(z==1):
                page1 = "https://www.cricbuzz.com/cricket-team/chennai-super-kings/58/results"
                pagetree = requests.get(page1, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                lastmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                lstmtch = soup1.find_all("a", {"class": "cb-text-complete"})
                print(lastmatch[0].text)
                print(lstmtch[0].text)

            if(z==2):
                page1 = "https://www.cricbuzz.com/cricket-team/royal-challengers-bangalore/59/results"
                pagetree = requests.get(page1, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                lastmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                lstmtch = soup1.find_all("a", {"class": "cb-text-complete"})
                print(lastmatch[0].text)
                print(lstmtch[0].text)

            if(z==3):
                page1 = "https://www.cricbuzz.com/cricket-team/kolkata-knight-riders/63/results"
                pagetree = requests.get(page1, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                lastmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                lstmtch = soup1.find_all("a", {"class": "cb-text-complete"})
                print(lastmatch[0].text)
                print(lstmtch[0].text)
                
            if(z==4):
                page1 = "https://www.cricbuzz.com/cricket-team/mumbai-indians/62/results"
                pagetree = requests.get(page1, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                lastmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                lstmtch = soup1.find_all("a", {"class": "cb-text-complete"})
                print(lastmatch[0].text)
                print(lstmtch[0].text)

            if(z==5):
                page1 = "https://www.cricbuzz.com/cricket-team/delhi-capitals/61/results"
                pagetree = requests.get(page1, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                lastmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                lstmtch = soup1.find_all("a", {"class": "cb-text-complete"})
                print(lastmatch[0].text)
                print(lstmtch[0].text)

            if(z==6):
                page1 = "https://www.cricbuzz.com/cricket-team/rajasthan-royals/64/results"
                pagetree = requests.get(page1, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                lastmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                lstmtch = soup1.find_all("a", {"class": "cb-text-complete"})
                print(lastmatch[0].text)
                print(lstmtch[0].text)

            if(z==7):
                page1 = "https://www.cricbuzz.com/cricket-team/sunrisers-hyderabad/255/results"
                pagetree = requests.get(page1, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                lastmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                lstmtch = soup1.find_all("a", {"class": "cb-text-complete"})
                print(lastmatch[0].text)
                print(lstmtch[0].text)

            if(z==8):
                page1 = "https://www.cricbuzz.com/cricket-team/kings-xi-punjab/65/results"
                pagetree = requests.get(page1, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                lastmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                lstmtch = soup1.find_all("a", {"class": "cb-text-complete"})
                print(lastmatch[0].text)
                print(lstmtch[0].text)

            else:
                q=0
            
    elif(x==4):
        p=1
        while(p==1):
            print("1.Chennai Super Kings")
            print("2.Royal Challengers Bangalore")
            print("3.Kolkata Knight Riders")
            print("4.Mumbai Indians")
            print("5.Delhi Capitals")
            print("6.Rajasthan Royals")
            print("7.Sunrisers Hyderabad")
            print("8.Kings XI Punjab")
            y = int(input("Enter your team: "))

            if(y==1):
                page1 = "https://www.cricbuzz.com/cricket-team/chennai-super-kings/58/schedule"
                page2 = "https://sports.ndtv.com/cricket/teams/2141-chennai-super-kings-teamprofile/schedules-fixtures"
                pagetree = requests.get(page1, headers=headers)
                pagetree2 = requests.get(page2, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                soup2 = BeautifulSoup(pagetree2.text,features="html.parser")
                nextmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                nxtmtch = soup1.find_all("div", {"class": "cb-font-12 text-gray"})
                tt = soup2.find_all("div", {"class": "team_head_date"})
                print(nextmatch[0].text)
                print(tt[0].text)
                print(nxtmtch[0].text)
                
            elif(y==2):
                page1 = "https://www.cricbuzz.com/cricket-team/royal-challengers-bangalore/59/schedule"
                page2 = "https://sports.ndtv.com/cricket/teams/2138-royal-challengers-bangalore-teamprofile/schedules-fixtures"
                pagetree = requests.get(page1, headers=headers)
                pagetree2 = requests.get(page2, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                soup2 = BeautifulSoup(pagetree2.text,features="html.parser")
                nextmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                nxtmtch = soup1.find_all("div", {"class": "cb-font-12 text-gray"})
                tt = soup2.find_all("div", {"class": "team_head_date"})
                print(nextmatch[0].text)
                print(tt[0].text)
                print(nxtmtch[0].text)
                
            elif(y==3):
                page1 = "https://www.cricbuzz.com/cricket-team/kolkata-knight-riders/63/schedule"
                page2 = "https://sports.ndtv.com/cricket/teams/2139-kolkata-knight-riders-teamprofile/schedules-fixtures"
                pagetree = requests.get(page1, headers=headers)
                pagetree2 = requests.get(page2, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                soup2 = BeautifulSoup(pagetree2.text,features="html.parser")
                nextmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                nxtmtch = soup1.find_all("div", {"class": "cb-font-12 text-gray"})
                tt = soup2.find_all("div", {"class": "team_head_date"})
                print(nextmatch[0].text)
                print(tt[0].text)
                print(nxtmtch[0].text)
                
            elif(y==4):
                page1 = "https://www.cricbuzz.com/cricket-team/mumbai-indians/62/schedule"
                page2 = "https://sports.ndtv.com/cricket/teams/2144-mumbai-indians-teamprofile/schedules-fixtures"
                pagetree = requests.get(page1, headers=headers)
                pagetree2 = requests.get(page2, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                soup2 = BeautifulSoup(pagetree2.text,features="html.parser")
                nextmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                nxtmtch = soup1.find_all("div", {"class": "cb-font-12 text-gray"})
                tt = soup2.find_all("div", {"class": "team_head_date"})
                print(nextmatch[0].text)
                print(tt[0].text)
                print(nxtmtch[0].text)
                
            elif(y==5):
                page1 = "https://www.cricbuzz.com/cricket-team/delhi-capitals/61/schedule"
                page2 = "https://sports.ndtv.com/cricket/teams/2142-delhi-capitals-teamprofile/schedules-fixtures"
                pagetree = requests.get(page1, headers=headers)
                pagetree2 = requests.get(page2, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                soup2 = BeautifulSoup(pagetree2.text,features="html.parser")
                nextmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                nxtmtch = soup1.find_all("div", {"class": "cb-font-12 text-gray"})
                tt = soup2.find_all("div", {"class": "team_head_date"})
                print(nextmatch[0].text)
                print(tt[0].text)
                print(nxtmtch[0].text)
                
            elif(y==6):
                page1 = "https://www.cricbuzz.com/cricket-team/rajasthan-royals/64/schedule"
                page2 = "https://sports.ndtv.com/cricket/teams/2143-rajasthan-royals-teamprofile/schedules-fixtures"
                pagetree = requests.get(page1, headers=headers)
                pagetree2 = requests.get(page2, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                soup2 = BeautifulSoup(pagetree2.text,features="html.parser")
                nextmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                nxtmtch = soup1.find_all("div", {"class": "cb-font-12 text-gray"})
                tt = soup2.find_all("div", {"class": "team_head_date"})
                print(nextmatch[0].text)
                print(tt[0].text)
                print(nxtmtch[0].text)
                
            elif(y==7):
                page1 = "https://www.cricbuzz.com/cricket-team/sunrisers-hyderabad/255/schedule"
                page2 = "https://sports.ndtv.com/cricket/teams/2165-sunrisers-hyderabad-teamprofile/schedules-fixtures"
                pagetree = requests.get(page1, headers=headers)
                pagetree2 = requests.get(page2, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                soup2 = BeautifulSoup(pagetree2.text,features="html.parser")
                nextmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                nxtmtch = soup1.find_all("div", {"class": "cb-font-12 text-gray"})
                tt = soup2.find_all("div", {"class": "team_head_date"})
                print(nextmatch[0].text)
                print(tt[0].text)
                print(nxtmtch[0].text)
                
            elif(y==8):
                page1 = "https://www.cricbuzz.com/cricket-team/kings-xi-punjab/65/schedule"
                page2 = "https://sports.ndtv.com/cricket/teams/2140-kings-xi-punjab-teamprofile/schedules-fixtures"
                pagetree = requests.get(page1, headers=headers)
                pagetree2 = requests.get(page2, headers=headers)
                soup1 = BeautifulSoup(pagetree.text,features="html.parser")
                soup2 = BeautifulSoup(pagetree2.text,features="html.parser")
                nextmatch = soup1.find_all("a", {"class": "text-hvr-underline"})
                nxtmtch = soup1.find_all("div", {"class": "cb-font-12 text-gray"})
                tt = soup2.find_all("div", {"class": "team_head_date"})
                print(nextmatch[0].text)
                print(tt[0].text)
                print(nxtmtch[0].text)
                
            else:
                p=0
            
    else:
        t=0

