from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from .models import *


# Create your views here.
def create_account_tobb():

    driver = webdriver.Firefox()
    driver.set_window_position(-10000,0)
    driver.minimize_window()


    #-----get user and number from database
    account=AccountReport.objects.all()[0]
    account.number+=1
    account.save()
    #get user and number from database-----

    try:
        username=f"{account.user}{account.number}"

        #---------------------------------------------------------get an email from mohmal
        driver.get("https://www.mohmal.com/en")
        driver.find_element(By.ID, "rand").click()
        mail=driver.find_element(By.ID, "email").find_element(By.CLASS_NAME,"email").text
        time.sleep(7)
        #get an email from mohmal---------------------------------------------------------

        
        #-----------------------------------------------------------signup in tobb
        driver.get("https://sanayi.tobb.org.tr/firma_kayit3.php")

        business_feild = driver.find_element(By.NAME, "firma_unvani")
        name_feild = driver.find_element(By.NAME, "yetkili")
        post_feild = driver.find_element(By.NAME, "posta_adresi")
        tel02 = driver.find_element(By.NAME, "tel_2")
        tel03 = driver.find_element(By.NAME, "tel_3")
        faks02 = driver.find_element(By.NAME, "faks_2")
        faks03 = driver.find_element(By.NAME, "faks_3")
        mail_feild = driver.find_element(By.NAME, "email")
        status = driver.find_element(By.NAME, "statu")
        username_feild = driver.find_element(By.NAME, "kullanici")
        submit = driver.find_element(By.NAME, "gonder")

        business_feild.send_keys("AliParsa")
        name_feild.send_keys("AliParsa")
        post_feild.send_keys("AliParsa")
        tel02.send_keys("000")
        tel03.send_keys("0000")
        faks02.send_keys("000")
        faks03.send_keys("0000")
        mail_feild.send_keys(mail)
        username_feild.send_keys(username)
        status.click()
        submit.click()
        #signup in tobb-----------------------------------------------------------


        #-------------------------------------------------back to mohmal for get password
        time.sleep(7)
        driver.get("https://www.mohmal.com/en/refresh")
        time.sleep(7)
        driver.find_element(By.CLASS_NAME,"subject").click()
        time.sleep(7)
        inbox =BeautifulSoup(driver.page_source , "html.parser").find("iframe").attrs["src"]
        driver.get("https://www.mohmal.com"+inbox)
        password =BeautifulSoup(driver.page_source , "html.parser").find_all("td")[-1].text.strip()
        driver.close()
        #back to mohmal for get password-------------------------------------------------

        return {"user":username,"pass":password}
    except:
        driver.close()
        return False




def http_crawler_tobb(request,city_slug):

    #-------------get last sector saved by this city slug
    city = Cities.objects.get(slug=city_slug)
    subsector_start = city.sub_sector_report
    sector_start = city.sector_report
    #get last sector saved by this city slug-------------


    #------------------------------------------------login
    check=True
    while check:

        #call def for create new account
        account=create_account_tobb()

        #login if account created
        if account:
            try:
                driver = webdriver.Firefox()
                driver.set_window_position(-10000,0)
                driver.minimize_window()

                driver.get("https://sanayi.tobb.org.tr/")

                username_feild = driver.find_element(By.NAME, "user")
                password_feild = driver.find_element(By.NAME, "pass")
                login = driver.find_element(By.NAME, "giris")

                username_feild.send_keys(account["user"])
                password_feild.send_keys(account["pass"])
                login.click()

                limit=0
                check=False
            except:
                driver.close()
                pass
    #login------------------------------------------------


    #---------------------------------------------------------------get sub sectors of saved in city
    try:
        time.sleep(3)
        driver.get("https://sanayi.tobb.org.tr/yeni_il08_0.php")
        city_button=driver.find_element(By.XPATH ,f"//select[@name='il']/option[@value={city_slug}]")
        city_button.click()
        driver.find_element(By.NAME, "arama").click()

        time.sleep(3)
        page=BeautifulSoup(driver.page_source , "html.parser")
        list_of_subsectors = page.find_all("center")[9:-2]
        list_of_subsectors = [f"https://sanayi.tobb.org.tr/yeni_il_urunlistesi02.php?il={city_slug}&sektor_kodu=" + x.find("a").text for x in list_of_subsectors ]
    except Exception as e:
        return HttpResponse(f"<h1 align='center' >error 2</h1> <br> <p align='center'>{e}</p><br><a href='/' align='center'>login</a>")
    #get sub sectors of saved in city---------------------------------------------------------------


    subsector_start_save=subsector_start
    sector_start_save=sector_start


    #---------------------------------------------------------------------------------------------------------get sectors of saved in city
    for subsector in list_of_subsectors[subsector_start_save:]:

        try:
            driver.get(subsector)
            page_0=BeautifulSoup(driver.page_source , "html.parser")
            list_of_sectors = page_0.find_all("td",attrs={"align":"left"})[1:]
            list_of_sectors = ["https://sanayi.tobb.org.tr/" + x.find("a").attrs["href"] for x in list_of_sectors ]
            sub_sector_name = page_0.find("td",attrs={"bgcolor":"#ffffff"}).find("center").find_all("h2")[1].text.strip()
            sub_sector_name = sub_sector_name[sub_sector_name.index("-")+1:].replace(";",".")
        except:
            continue

        for sector in list_of_sectors[sector_start_save:]:
            
            try:
                driver.get(sector)
                limit+=1
                page=BeautifulSoup(driver.page_source , "html.parser")
                table=page.find_all("table")[-2].find_all("tr")

                for row in table[1:]:
                    all_feild = row.find_all("td")
                    title = all_feild[1].text.strip()
                    address = all_feild[3].text.strip()
                    contact = all_feild[4].text.strip()
                    tel = contact[contact.index("T:")+2:contact.index("/")].replace("-","").replace(" ","").strip()
                    if "www" in contact:
                        site = contact[contact.index("www"):].strip()
                    elif "@" in contact:
                        try:
                            site = contact[contact.index("@")+1:contact.index("/",contact.index("@"))].strip()
                            site = "www."+site
                        except:
                            site = contact[contact.index("@")+1:].strip()
                            site = "www."+site
                    else:
                        site="bulunmadı"
                    population = all_feild[5].text.strip()
                    
                    company = Companies()
                    company.user = request.user
                    company.sector = sub_sector_name
                    company.name = title
                    company.short_name = title[0:11]
                    company.phone = tel
                    company.site = site
                    company.address = address
                    company.personels_caount = population
                    company.note = ""
                    company.fount = Fount.objects.get(name="TOBB")
                    company.city = Cities.objects.get(slug=city_slug)
                    company.last_status = Status.objects.get(name="Yeni")
                    try:
                        if not tel[0:3] in ["444","850"]:
                            company.save()
                            company.status.add(Status.objects.get(name="Yeni"))
                            company.save()
                    except :
                        pass
                if limit>95:
                    driver.close()
                    check=True
                    #login------------------------------------------------
                    while check:
                        account=create_account_tobb()
                        if account:
                            try:
                                driver = webdriver.Firefox()
                                driver.set_window_position(-10000,0)
                                driver.minimize_window()
                                driver.get("https://sanayi.tobb.org.tr/")

                                username_feild = driver.find_element(By.NAME, "user")
                                password_feild = driver.find_element(By.NAME, "pass")
                                login = driver.find_element(By.NAME, "giris")

                                username_feild.send_keys(account["user"])
                                password_feild.send_keys(account["pass"])
                                login.click()

                                limit=0
                                check=False
                            except:
                                driver.close()
                                pass
                    #login------------------------------------------------
                city.sub_sector_report = subsector_start
                city.sector_report = sector_start
                city.save()
                
                sector_start+=1
            except:
                pass
                
        subsector_start+=1
        sector_start=0

    city.sub_sector_report = 0
    city.sector_report = 0
    city.save()
    #get sectors of saved in city---------------------------------------------------------------------------------------------------------

    driver.close()




def login(request):
    return render(request,"login.html")