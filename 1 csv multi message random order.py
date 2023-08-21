from sqlite3 import Date
import string
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import random
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from datetime import date
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
message_number= simpledialog.askstring(title="Test",
                                        prompt="total number of message ")
me=[]
for i in range(0,int(message_number)):
    me.append(simpledialog.askstring(title="Test",
                                    prompt="message(where use name there put name) "))
save_file = simpledialog.askstring(title="Test",
                                  prompt="your file save as file name:")

#today date save as run_date
run_date=str(date.today())   
rday=run_date[8:10]
rmonth=run_date[5:7]
ryear=run_date[0:4]
rd =str(ryear+"/"+rmonth+"/"+rday)
d1 = datetime.strptime(rd, "%Y/%m/%d")

# Make interface for file selection
Tk().withdraw()
filename = askopenfilename()

#random time for sleep
ts = random.randint(10,30)
dp = pd.read_csv(filename)
l = len(dp)

driver = webdriver.Chrome("C:\\Users\\Riteshkumar Parmar\\Desktop\\Solwin Infotech\\requriedment\\chromedriver_win32\\chromedriver.exe")
url = "https://web.whatsapp.com/"
driver.get(url)
print("Scan QR Code")
#scan qr code to login into whatsapp

time.sleep(30)
srchbox = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[1]/p")  # Searchbox
srchbox.click()
name=[]
number=[]
yes=[]
no=[]
day_gap=[]
message_no=[]

for i in range(l):    
    mob = int(dp.at[i,'Mobile'])  # Mobile/Whatsapp Number # csv row and column name
    nam = str(dp.at[i,'Name'])    # Name
    
    
    messa=[]
    dd=[]
    for i in range(0,int(message_number)):
        messa.append(0)
    for i in range(0,int(message_number)):
         messa[i]= str(me[i]).replace("***",nam)
    for i in range(0,int(message_number)):
        dd.append(0)
    for i in range(0,int(message_number)):
         dd[i]= str(me[i]).replace("***",nam)
    print(dd)  
    time.sleep(1)                                # Message type Here........
    # Going to page of candidate in whatsapp
    le=int(len(messa)) 

    ln=int(len(messa))
    for i in range(le):
        if(ln!=1):
            random_int =random.randint(0,ln-1)
            print(random_int)
            mess= messa[int(random_int)]
            for i in reversed(range(ln)):
                if(str(messa[i])==str(mess)):
                    messa.remove(messa[i])
                else:
                    continue
            print(mess)  
            print(messa)  
        else:
            mess=str(messa[0])
        ln=int(len(messa))

        for i in range(0,le):
            print(str(mess),dd[i])
            if(str(mess)==dd[i]):
                message_no.append(i+1)
                print(message_no)
            else:
                print(message_no,"0")
                continue
                
        
            
        number.append(mob)
        name.append(nam)
        srchbox.send_keys(mob)
        
        time.sleep(1)
        srchbox.send_keys(Keys.ENTER)
        
        p = driver.page_source
        soup= BeautifulSoup(p,'lxml')
        try:
            lastmess1 = soup.find_all('span',{'class':"i0jNr selectable-text copyable-text"},string=True)[-1]
            recent1 = lastmess1.get_text(strip=True)
            if(lastmess1 ==soup.find_all('span',{'class':"i0jNr selectable-text copyable-text"},string=True)[0]):
                if(recent1!= mess):
                    messbox = driver.find_element(By.XPATH, "//div[@title='Type a message']")
                    messbox.send_keys(mess)
                    messbox.send_keys(Keys.ENTER)  # Message sent with ENTER Key
                    print("Message sent successfully!!!",nam)
                    yes.append("*")
                    no.append(" ")
                    day_gap.append(" ")
                    
                else:
                    lastmdate = soup.find_all('div',{'class':"copyable-text"})[-1]
                    lastmd = lastmdate['data-pre-plain-text']
                    lastmd.split(" ")
                    l =(lastmd.split(" "))
                    print(l)
                    l2 =l[2]
                    l3 =l2.split("/")
                    lmmonth=l3[0]
                    lmday=l3[1]
                    lmyear=l3[2][0:4]
                    lmd=str(lmyear+"/"+lmmonth+"/"+lmday)
                    d2 = datetime.strptime(lmd, "%Y/%m/%d")
                    #list of all messages
                    # Last Message
                    daysdiff= d1-d2
                    daysdifference =daysdiff.days
                    day_gap.append(daysdifference)
                    #if your mess send alrey last 5 message and that message send before 1 week then you will able to send again
                    if(daysdifference>7):
                        messbox = driver.find_element(By.XPATH, "//div[@title='Type a message']")
                        messbox.send_keys(mess)
                        messbox.send_keys(Keys.ENTER)  # Message sent with ENTER Key
                        print("Message sent successfully!!!",nam)
                        yes.append("*")
                        no.append(" ")
                    
                    else:
                        print("Failed to send ",nam)
                        yes.append(" ")
                        no.append("*")
            else:
                lastmess2 = soup.find_all('span',{'class':"i0jNr selectable-text copyable-text"},string=True)[-2]
                recent2 = lastmess2.get_text(strip=True)
                if(lastmess2 ==soup.find_all('span',{'class':"i0jNr selectable-text copyable-text"},string=True)[0]):
                    if(recent1!=mess and recent2!= mess):
                        messbox = driver.find_element(By.XPATH, "//div[@title='Type a message']")
                        messbox.send_keys(mess)
                        messbox.send_keys(Keys.ENTER)  # Message sent with ENTER Key
                        print("Message sent successfully!!!",nam)
                        yes.append("*")
                        no.append(" ")
                        day_gap.append(" ")
                    else:
                        if(recent2==mess):
                            lastmdate = soup.find_all('div',{'class':"copyable-text"})[-1]
                        else:
                            lastmdate = soup.find_all('div',{'class':"copyable-text"})[-2]
                        lastmd = lastmdate['data-pre-plain-text']
                        lastmd.split(" ")
                        l =(lastmd.split(" "))
                        print(l)
                        l2 =l[2]
                        l3 =l2.split("/")
                        lmmonth=l3[0]
                        lmday=l3[1]
                        lmyear=l3[2][0:4]
                        lmd=str(lmyear+"/"+lmmonth+"/"+lmday)
                        d2 = datetime.strptime(lmd, "%Y/%m/%d")
                        # list of all messages
                        # Last Message
                        daysdiff= d1-d2
                        daysdifference =daysdiff.days
                        day_gap.append(daysdifference)
                        #if your mess send alrey last 5 message and that message send before 1 week then you will able to send again
                        if(daysdifference>7):
                            messbox = driver.find_element(By.XPATH, "//div[@title='Type a message']")
                            messbox.send_keys(mess)
                            messbox.send_keys(Keys.ENTER)  # Message sent with ENTER Key
                            print("Message sent successfully!!!",nam)
                            yes.append("*")
                            no.append(" ")
                        else:
                            print("Failed to send ",nam)
                            yes.append(" ")
                            no.append("*")
                else:
                    lastmess3 = soup.find_all('span',{'class':"i0jNr selectable-text copyable-text"},string=True)[-3]
                    recent3 = lastmess3.get_text(strip=True)
                    if(lastmess3==soup.find_all('span',{'class':"i0jNr selectable-text copyable-text"},string=True)[0]):  
                        if(recent1!=mess and recent2!= mess and recent3!=mess):
                            messbox = driver.find_element(By.XPATH, "//div[@title='Type a message']")
                            messbox.send_keys(mess)
                            messbox.send_keys(Keys.ENTER)  # Message sent with ENTER Key
                            print("Message sent successfully!!!",nam)
                            yes.append("*")
                            no.append(" ")
                            day_gap.append(" ") 
                        else:
                            if(recent1==mess):
                                lastmdate = soup.find_all('div',{'class':"copyable-text"})[-1]
                            elif(recent2 == mess):
                                lastmdate = soup.find_all('div',{'class':"copyable-text"})[-2]
                            else:
                                lastmdate = soup.find_all('div',{'class':"copyable-text"})[-3]
                            lastmd = lastmdate['data-pre-plain-text']
                            lastmd.split(" ")
                            l =(lastmd.split(" "))
                            print(l)
                            l2 =l[2]
                            l3 =l2.split("/")
                            lmmonth=l3[0]
                            lmday=l3[1]
                            lmyear=l3[2][0:4]
                            lmd=str(lmyear+"/"+lmmonth+"/"+lmday)
                            d2 = datetime.strptime(lmd, "%Y/%m/%d")
                            # list of all messages
                            # Last Message
                            daysdiff= d1-d2
                            daysdifference =daysdiff.days
                            day_gap.append(daysdifference)
                            #if your mess send alrey last 5 message and that message send before 1 week then you will able to send again
                            if(daysdifference>7):
                                messbox = driver.find_element(By.XPATH, "//div[@title='Type a message']")
                                messbox.send_keys(mess)
                                messbox.send_keys(Keys.ENTER)  # Message sent with ENTER Key
                                print("Message sent successfully!!!",nam)
                                yes.append("*")
                                no.append(" ")
                            else:
                                print("Failed to send ",nam)
                                yes.append(" ")
                                no.append("*")
                    else:
                        lastmess4 = soup.find_all('span',{'class':"i0jNr selectable-text copyable-text"},string=True)[-4]
                        recent4 = lastmess4.get_text(strip=True)
                        if(lastmess4==soup.find_all('span',{'class':"i0jNr selectable-text copyable-text"},string=True)[0]):
                            if(recent1!=mess and recent2!= mess and recent3!=mess and recent4!=mess):
                                messbox = driver.find_element(By.XPATH, "//div[@title='Type a message']")
                                messbox.send_keys(mess)
                                messbox.send_keys(Keys.ENTER)  # Message sent with ENTER Key
                                print("Message sent successfully!!!",nam)
                                yes.append("*")
                                no.append(" ")
                                day_gap.append(" ") 
                            else:
                                if(recent1==mess):
                                    lastmdate = soup.find_all('div',{'class':"copyable-text"})[-1] 
                                elif(recent2==mess):
                                    lastmdate = soup.find_all('div',{'class':"copyable-text"})[-2]
                                elif(recent3==mess):
                                    lastmdate = soup.find_all('div',{'class':"copyable-text"})[-3]
                                else:
                                    lastmdate = soup.find_all('div',{'class':"copyable-text"})[-4]
                                lastmd = lastmdate['data-pre-plain-text']
                                lastmd.split(" ")
                                l =(lastmd.split(" "))
                                print(l)
                                l2 =l[2]
                                l3 =l2.split("/")
                                lmmonth=l3[0]
                                lmday=l3[1]
                                lmyear=l3[2][0:4]
                                lmd=str(lmyear+"/"+lmmonth+"/"+lmday)
                                d2 = datetime.strptime(lmd, "%Y/%m/%d")
                                # list of all messages
                                # Last Message
                                daysdiff= d1-d2
                                daysdifference =daysdiff.days
                                day_gap.append(daysdifference)
                                #if your mess send alrey last 5 message and that message send before 1 week then you will able to send again
                                if(daysdifference>7):
                                    messbox = driver.find_element(By.XPATH, "//div[@title='Type a message']")
                                    messbox.send_keys(mess)
                                    messbox.send_keys(Keys.ENTER)  # Message sent with ENTER Key
                                    print("Message sent successfully!!!",nam)
                                    yes.append("*")
                                    no.append(" ")
                    
                                else:
                                    print("Failed to send ",nam)
                                    yes.append(" ")
                                    no.append("*")
                        else:
                            lastmess5 = soup.find_all('span',{'class':"i0jNr selectable-text copyable-text"},string=True)[-5]
                            recent5 = lastmess5.get_text(strip=True)
                            if(recent1!=mess and recent2!= mess and recent3!=mess and recent4!=mess and recent5!=mess):
                                messbox = driver.find_element(By.XPATH, "//div[@title='Type a message']")
                                messbox.send_keys(mess)
                                messbox.send_keys(Keys.ENTER)  # Message sent with ENTER Key
                                print("Message sent successfully!!!",nam)
                                yes.append("*")
                                no.append(" ")
                                day_gap.append(" ")
                            else:
                                if(recent1==mess):
                                    lastmdate = soup.find_all('div',{'class':"copyable-text"})[-1] 
                                elif(recent2==mess):
                                    lastmdate = soup.find_all('div',{'class':"copyable-text"})[-2]
                                elif(recent3==mess):
                                    lastmdate = soup.find_all('div',{'class':"copyable-text"})[-3]
                                elif(recent4==mess):
                                    lastmdate = soup.find_all('div',{'class':"copyable-text"})[-4]
                                else:
                                    lastmdate = soup.find_all('div',{'class':"copyable-text"})[-5]
                                lastmd = lastmdate['data-pre-plain-text']
                                lastmd.split(" ")
                                l =(lastmd.split(" "))
                                print(l)
                                l2 =l[2]
                                l3 =l2.split("/")
                                lmmonth=l3[0]
                                lmday=l3[1]
                                lmyear=l3[2][0:4]
                                lmd=str(lmyear+"/"+lmmonth+"/"+lmday)
                                d2 = datetime.strptime(lmd, "%Y/%m/%d")
                                # list of all messages
                                # Last Message
                                daysdiff= d1-d2
                                daysdifference =daysdiff.days
                                day_gap.append(daysdifference)
                                #if your mess send alrey last 5 message and that message send before 1 week then you will able to send again
                                if(daysdifference>7):
                                    messbox = driver.find_element(By.XPATH, "//div[@title='Type a message']")
                                    messbox.send_keys(mess)
                                    messbox.send_keys(Keys.ENTER)  # Message sent with ENTER Key
                                    print("Message sent successfully!!!",nam)
                                    yes.append("*")
                                    no.append(" ")
                    
                                else:
                                    print("Failed to send ",nam)
                                    yes.append(" ")
                                    no.append("*")
        except:
            recent1=str("  ")
            messbox = driver.find_element(By.XPATH, "//div[@title='Type a message']")
            messbox.send_keys(mess)
            messbox.send_keys(Keys.ENTER)  # Message sent with ENTER Key
            print("Message sent successfully!!!",nam)
            yes.append("*")
            no.append(" ")
            day_gap.append(" ")
        time.sleep(3)
        
       
    
        dist={"number" : number ,"name" : name,"message no":message_no, "yes" : yes, "no" : no, "day_gap" :day_gap,} #,
        #print(dist)
        df=pd.DataFrame(dist)
        Date=str(run_date)
        df.to_csv(str(save_file)+".csv")                  #filename
    
    time.sleep(ts)  # Stop for random time
#for csv file 
print("work done")
#driver.close()  # Close the window   


