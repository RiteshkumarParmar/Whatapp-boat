#message line 52
# filename  line 316
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
save_file = simpledialog.askstring(title="Test",
                                  prompt="your file save as file name:")
message_for_all=simpledialog.askstring(title="Test",
                                  prompt="Your message put here(where use name there put ***) :")
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

driver = webdriver.Chrome("C:\\Users\\Hardik\\Downloads\\chromedriver_win32\\chromedriver.exe")
url = "https://web.whatsapp.com/"
driver.get(url)
print("Scan QR Code")
#scan qr code to login into whatsapp

time.sleep(30)
srchbox = driver.find_element(By.XPATH, "//div[@class='_13NKt copyable-text selectable-text']")  # Searchbox
srchbox.click()
name=[]
number=[]
yes=[]
no=[]
day_gap=[]

for i in range(l):    
    mob = int(dp.at[i,'Mobile'])  # Mobile/Whatsapp Number # csv row and column name
    nam = str(dp.at[i,'Name'])    # Name
    mess = message_for_all.replace("***",nam)                                # Message type Here........
    # Going to page of candidate in whatsapp
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
    
    #difference between days
    dist={"number" : number ,"name" : name, "yes" : yes, "no" : no, "day_gap" :day_gap} #
    #print(dist)
    df=pd.DataFrame(dist)
    Date=str(run_date)
    df.to_csv(str(save_file)+".csv")                  #filename
    
    time.sleep(ts)  # Stop for random time
#for csv file 
print("work done")
#driver.close()  # Close the window   



