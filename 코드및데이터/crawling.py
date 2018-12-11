# -*- coding: utf-8 -*-
  
from bs4 import BeautifulSoup
import requests
import re
import csv

month=[9]
date=[0,0,0,32,31,32,31,32,32,31,32]

oldStadium=['잠실','목동','문학','수원','대전','대구','포항','광주','마산','사직','울산']
newStadium=["잠실","고척돔","인천문학","케이티위즈파크","대전한밭","청주","라이온즈파크","포항","챔피언스필드","마산","부산사직","울산"]

#url = 'http://www.statiz.co.kr/boxscore.php?opt=4&date=2014-03-30&stadium=문학&hour=14'

url='http://www.statiz.co.kr/boxscore.php?opt=4&date=2018-'
url2='http://www.statiz.co.kr/boxscore.php?opt=2&date=2018-'
url3 = 'http://www.statiz.co.kr/league.php?opt=2018'
r = requests.get(url3)

soup = BeautifulSoup(r.text, "html.parser")
mr = soup.find_all("tr")
mr=mr[5:15]
count =1
while(mr):
    string=str(mr[0])
                        
    string = re.sub('<.*?>', '\t', string)

    string=string.replace("<tr>","")
    string=string.replace("</tr>","")
    string=string.replace("<th>","")
    string=string.replace("</th>","\t")
    string=string.replace("\n","\t")
    while "\t\t" in string:
        string=string.replace("\t\t","\t")
    string=string.replace("\t ","\t")
    string=string.replace("  "," ")
    string =  string.split("\t")
    if count is 1:
        dusanID = string[4]
    elif count is 2:
        skID = string[4]
    elif count is 3:
        hanhwaID = string[4]
    elif count is 4:
        nexenID=string[4]
    elif count is 5:
        lgID = string[4]
    elif count is 6:
        kiaID = string[4]
    elif count is 7:
        samsungID = string[4]
    elif count is 8:
        lotteID = string[4]
    elif count is 9:
        ncID=string[4]
    elif count is 10:
        ktID=string[4]
    count=count+1
    print (string)
    
    mr=mr[1:]

    
lotte=[]
nexen=[]
kia=[]
samsung=[]
sk=[]
nc=[]
hanhwa=[]
dusan=[]
lg=[]
kt=[]
match=[]
for i in month:
    for j in range(date[i]):
        matchurl=url+'0'+str(i)+"-"+str(j+1)
        Matchurl=url2+'0'+str(i)+"-"+str(j+1)
        print (i,"/",(j+1))
        for k in oldStadium:
            matchurl1=matchurl+'&stadium='+k
            Matchurl1=Matchurl+'&stadium='+k
            r = requests.get(matchurl1)
            R = requests.get(Matchurl1)
            soup = BeautifulSoup(r.text, "html.parser")
            Soup = BeautifulSoup(R.text, "html.parser")
            mr=soup.find_all("tr")
            Mrr=Soup.find_all("tr")
            if len(mr)>26:
                if "일일일정"in str(mr[6]):
                    count =4
                    hr=soup.find_all("h3")
                    team1= re.sub('<.*?>', '\t', str(hr[-3]))
                    team2= re.sub('<.*?>', '\t', str(hr[-2]))

                    team1=str(team1[8:-3])
                    team2=str(team2[8:-3])
                    #print matchurl1
                    #print Matchurl1
                    #print team1,team2
                    match=[team1]+[team2]
                    

                    Mr=Mrr[19]
                    home=Mrr[10]
                    away=Mrr[11]
                    

                    string=str(Mr)
                    
                    string = re.sub('<.*?>', '\t', string)
                    string=string.replace("<tr>","")
                    string=string.replace("</tr>","")
                    string=string.replace("<th>","")
                    string=string.replace("</th>","\t")
                    string=string.replace("\n","\t")
                    while "\t\t" in string:
                        string=string.replace("\t\t","\t")
                    string=string.replace("\t ","\t")
                    string=string.replace("  "," ")
                    string = string.split(" ")
                    team1era= string[-4]
                    team1era=team1era.split("\t")[0]
                    team2era= string[-1]
                    #print team1era,team2era



                    
                    string =str(home)
                    string = re.sub('<.*?>', '\t', string)
                    string=string.replace("<tr>","")
                    string=string.replace("</tr>","")
                    string=string.replace("<th>","")
                    string=string.replace("</th>","\t")
                    string=string.replace("\n","\t")
                    while "\t\t" in string:
                        string=string.replace("\t\t","\t")
                    string=string.replace("\t ","\t")
                    string=string.replace("  "," ")
                    string = string.split(" ")
 
                    home=string[-1].split("\t")[2]

                    
                    if home is "--":
                        home = 0.5

                    else:
                        home = home.split("-")
                        home =round(float(home[0])/(float(home[0])+float(home[1])),3)

                    string = str(away)
                    string = re.sub('<.*?>', '\t', string)
                    string=string.replace("<tr>","")
                    string=string.replace("</tr>","")
                    string=string.replace("<th>","")
                    string=string.replace("</th>","\t")
                    string=string.replace("\n","\t")
                    while "\t\t" in string:
                        string=string.replace("\t\t","\t")
                    string=string.replace("\t ","\t")
                    string=string.replace("  "," ")
                    string = string.split(" ")
                    away = string[-1].split("\t")[1]
                    
                    
                    if away is "--":
                        away = 0.5

                    else:
                        away=away.split("-")
                        away =round(float(away[0])/(float(away[0])+float(away[1])),3)

                    #print away,home
                    
                    mr=mr[7:]
                    record=4
                    team1ops=0
                    team2ops=0
                    newteam1=[]
                    newteam2=[]

                    while(mr):
                        string=str(mr[0])
                        
                        string = re.sub('<.*?>', '\t', string)
                        string=string.replace("<tr>","")
                        string=string.replace("</tr>","")
                        string=string.replace("<th>","")
                        string=string.replace("</th>","\t")
                        string=string.replace("\n","\t")
                        while "\t\t" in string:
                            string=string.replace("\t\t","\t")
                        string=string.replace("\t ","\t")
                        string=string.replace("  "," ")
                        if "POS" in string:
                            break
                        if record>0:
                            if string.split("\t")[1].isdigit() is True:
                                string = string.split("\t")
                                count=0
                                if record==3:
                                    team1ops= team1ops+ float(string[19])
                                elif record ==2:
                                    team2ops= team2ops+float(string[19])
                        if "합계"in string:
                            string = string.split("\t")
                            if record is 3:
                                newteam1=newteam1+[string[-4],string[-3],string[-2]]
                                team1score=int(string[4])
                            elif record is 2:
                                newteam2=newteam2+[string[-4],string[-3],string[-2]]
                                team2score=int(string[4])
                            elif record is 1:
                                newteam1=newteam1+[string[-5]]
                            elif record is 0:
                                newteam2=newteam2+[string[-5]]
                        
                        if "이름"in string:
                            record=record-1
                        mr=mr[1:]
                    if team1score<team2score:
                        match=match+[1]
                    else:
                        match = match+[0]
                        
                    newteam1=newteam1+[round(team1ops/9,3)]
                    newteam2=newteam2+[round(team2ops/9,3)]
                    #print round(team1ops/9,3),round(team2ops/9,3)
                    #print newteam1,newteam2
                    #print newteam1 ,newteam2

                    match=match+[team1era,team2era]+[away,home]
                    if team1 == lotteID :

                        match=match+lotte
                        lotte=newteam1
                    elif team1 == nexenID:

                        match=match+nexen
                        nexen=newteam1
                    elif team1 == kiaID:

                        team1=match+kia
                        kia=newteam1
                    elif team1 == samsungID:

                        match=match+samsung
                        samsung=newteam1
                    elif team1 == skID:

                        match =match + sk
                        sk=newteam1
                    elif team1 == ncID:

                        match = match+nc
                        nc=newteam1
                    elif team1 == hanhwaID:

                        match = match +hanhwa
                        hanhwa=newteam1
                    elif team1 == dusanID:
 
                        match = match + dusan
                        dusan=newteam1
                    elif team1 == lgID:

                        match = match+lg
                        lg=newteam1
                    elif team1 == ktID:

                        match = match +kt
                        kt=newteam1

                    if team2  == lotteID :
                        match=match+lotte
                        lotte=newteam2
                    elif team2 == nexenID:
                        match=match+nexen
                        nexen=newteam2
                    elif team2 == kiaID:
                        team1=match+kia
                        kia=newteam2
                    elif team2  == samsungID:
                        match=match+samsung
                        samsung=newteam2
                    elif team2 == skID:
                        match =match + sk
                        sk=newteam2
                    elif team2 == ncID:
                        match = match+nc
                        nc=newteam2
                    elif team2 == hanhwaID:
                        match = match +hanhwa
                        hanhwa=newteam2
                    elif team2 == dusanID:
                        match = match + dusan
                        dusan=newteam2
                    elif team2  == lgID:
                        match = match+lg
                        lg=newteam2
                    elif team2 == ktID:
                        match = match +kt
                        kt=newteam2

                    if len(match)>13:
                        print (match)
