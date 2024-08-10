from connection import get_database
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time



dbname = get_database()

chromeoptions = Options()
chromeoptions.add_argument("--headless")
driver = webdriver.Chrome(options=chromeoptions)

driver.get("https://wonder.cdc.gov/vaers.html")

driver.implicitly_wait(0.1)

button1F = driver.find_element(by=By.XPATH, value="//*[@id='closeBtn']")
driver.execute_script("arguments[0].click();", button1F)

test = driver.find_element(by=By.XPATH, value="//*[@id='vaers-buttons2']/input")
driver.execute_script("arguments[0].click();", test)
              
vaccine = driver.find_element(by=By.NAME, value="F_D8.V14")
vaccine2 = vaccine.find_elements(by=By.TAG_NAME, value="option")
select = Select(driver.find_element(by=By.XPATH, value="//*[@id='codes-D8.V14']"))

state = driver.find_element(by=By.NAME, value="V_D8.V12")
state2 = state.find_elements(by=By.TAG_NAME, value="option")
select1 = Select(driver.find_element(by=By.XPATH, value="//*[@id='SD8.V12']"))

date = driver.find_element(by=By.NAME, value="F_D8.V3")
date2 = date.find_elements(by=By.TAG_NAME, value="option")
select2 = Select(driver.find_element(by=By.XPATH, value="//*[@id='codes-D8.V3']"))


count=True
indxcount=2
indxcount1=1
indxcount2=1
run1=True
started=False
while(indxcount<len(vaccine2)):
    nameorig = vaccine2[indxcount].text
    name = dbname[nameorig]
    if indxcount==2:
        select.deselect_by_index(0)
    select.deselect_by_index(indxcount-1)
    select.select_by_index(indxcount)
    indxcount+=1
    inxcount1=1
    while(indxcount1<len(state2)):
        state3 = state2[indxcount1].text
        select2.deselect_by_index(indxcount1-1)
        select2.select_by_index(indxcount1)
        indxcount1+=1
        indxcount2=1
        while(indxcount2<len(date2)):
            date=date2[indxcount2].text
            select1.deselect_by_index(indxcount2-1)
            select1.select_by_index(indxcount2)
            indxcount2+=1
            count=False

            send = driver.find_element(by=By.XPATH, value="//*[@id='wonderform']/table/tbody/tr/td/div[3]/input[1]")
            driver.execute_script("arguments[0].click();", send)


            results2 = driver.find_element(by=By.XPATH, value="//*[@id='wonderform']/table/tbody/tr/td/div[3]/div/table[3]/tbody")
            results3 = results2.find_elements(by=By.TAG_NAME, value="tr")


            if len(results3)==0:
                driver.back()
                print("Nothing found in", date, "and", state3, "for", nameorig)
                print('\n')
            else:
                for k in results3:
                    name2= k.find_element(by=By.TAG_NAME, value="th")
                    elements = k.find_elements(by=By.TAG_NAME, value="td")
                    for p in range(len(elements)):
                        if p%2==0:
                            events = elements[p]
                            final = {"Date": date , "State": state3 , "Symptom": name2.text, "Occurences":events.text}
                            name.insert_one(final)
                            print(nameorig, "in date",date, "in state", state3, "completed")
                            print('\n')

                driver.back()
            vaccine = driver.find_element(by=By.NAME, value="F_D8.V14")
            vaccine2 = vaccine.find_elements(by=By.TAG_NAME, value="option")
            select = Select(driver.find_element(by=By.XPATH, value="//*[@id='codes-D8.V14']"))

            date = driver.find_element(by=By.NAME, value="F_D8.V3")
            date2 = date.find_elements(by=By.TAG_NAME, value="option")
            select1 = Select(driver.find_element(by=By.XPATH, value="//*[@id='codes-D8.V3']"))

            state = driver.find_element(by=By.NAME, value="V_D8.V12")
            state2 = state.find_elements(by=By.TAG_NAME, value="option")
            select2 = Select(driver.find_element(by=By.XPATH, value="//*[@id='SD8.V12']"))
            
               
            
        

exit()



count = True
indxcount = 1
for i in vaccine2:
    name = i.text
    name = dbname[i.text]
    if count==True:
        select.deselect_by_index(0)
    select.select_by_index(indxcount)
    for j in date2:
        if count==True:
            select1.deselect_by_index(0)
        select1.select_by_index(indxcount)
        for m in state2:
            if count==True:
                select2.deselect_by_index(0)
            select1.select_by_index(indxcount)
            indxcount+=1
            #count=False
            send = driver.find_element(by=By.XPATH, value="//*[@id='wonderform']/table/tbody/tr/td/div[3]/input[1]")
            driver.execute_script("arguments[0].click();", send)
            #argument[0].click();
           

            results2 = driver.find_element(by=By.XPATH, value="//*[@id='wonderform']/table/tbody/tr/td/div[3]/div/table[3]/tbody")
            results3 = results2.find_elements(by=By.TAG_NAME, value="tr")

            if len(results3)==0:
                driver.back()
            else:
                for k in results3:
                    name2= k.find_element(by=By.TAG_NAME, value="th")
                    elements = k.find_elements(by=By.TAG_NAME, value="td")
                    for p in range(len(elements)):
                        if p%2==0:
                            events = elements[p]
                            final = {"Date": j.text , "State": str(m) , "Symptom": name2.text, "Occurences":events.text}
                            name.insert_one(final)
                driver.back()
                vaccine = driver.find_element(by=By.NAME, value="F_D8.V14")
                vaccine2 = vaccine.find_elements(by=By.TAG_NAME, value="option")
                select = Select(driver.find_element(by=By.XPATH, value="//*[@id='codes-D8.V14']"))

                date = driver.find_element(by=By.NAME, value="F_D8.V3")
                date2 = date.find_elements(by=By.TAG_NAME, value="option")
                select1 = Select(driver.find_element(by=By.XPATH, value="//*[@id='codes-D8.V3']"))

                state = driver.find_element(by=By.NAME, value="V_D8.V12")
                state2 = state.find_elements(by=By.TAG_NAME, value="option")
                select2 = Select(driver.find_element(by=By.XPATH, value="//*[@id='SD8.V12']"))
               




                              

       