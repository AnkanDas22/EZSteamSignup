from selenium import webdriver
from string import ascii_lowercase,ascii_uppercase,digits
from random import choice
driver=webdriver.Chrome("chromedriver.exe") #Replace the "chromedriver.exe" with your location of the same
k='True'
print("================Created by Ankan Das from UEM, Kolkata out of no reason================\n================Just use it at your own will but credit my GitHub profile please=======\n")
while(k=='True'):
    driver.set_page_load_timeout(40)
    driver.get("https://store.steampowered.com/join/?")
    x=input("Input 1 or Yes or Y->OWN EMAIL ADDRESS\nANYTHING ELSE-Automated Email Address\n")
    if(x=="1" or x.upper()=='YES' or x.upper()=='Y'):
        c=input("Enter the email address that you want to register with: \n")
    else:
        y=input("Enter Y or Yes or 1-> Input the domain name\nANYTHING ELSE for @gmail.com as your preferred\n")
        if(y.upper()=='Y' or y.upper()=='YES' or y=='1'):
            x=input("Enter your preferred email domain?\nDOMAIN NAME EXAMPLE:@gmail.com or @yahoo.com\n")
            c=''.join(choice(ascii_lowercase+digits+ascii_uppercase) for i in range(15))+x
        else:
            c=''.join(choice(ascii_lowercase+digits+ascii_uppercase) for i in range(15))+"@gmail.com"
    print("The confirmed email ID is: %s"%c)
    driver.find_element_by_name("email").send_keys(c)
    driver.find_element_by_name("reenter_email").send_keys(c)
    while True:
        e=input("Hey wanna change the CAPTCHA?\n Enter 1 or Yes or Y->YES, ANYTHING ELSE->NO\n")
        if e=="1":
            driver.find_element_by_id("captchaRefreshLink").click()
        driver.find_element_by_name("captcha_text").clear()
        d=input("Enter the stuff from the CAPTCHA image:\n")
        driver.find_element_by_name("captcha_text").send_keys(d)
        driver.find_element_by_id("createAccountButton").click()
        f=input("The CAPTCHA box will GLOW if INCORRECT:\n\nSIDENOTE: Orange if you don't have colour blindness\nYellow if you have Protanopia or Deuteranopia\nPink/Reddish if you have Titranopia\n\nWILL NOT GLOW IF IT IS CORRECT\n\nHas the correct CAPTCHA been entered?1 or Yes or Y-Yes!, 2 or Anything else-NO!\n")
        if (f=="1" or f.upper()=='YES' or f.upper()=='Y'):
            break
    driver.find_element_by_name("i_agree_check").click()
    driver.find_element_by_id("createAccountButton").click()
    print("EMAIL ID: %s\n"%c)
    with open("steamaccountlist.txt","a+") as fp: #change the file location for saving the account details
        fp.write("EMAIL ID: %s\r\n"%c)
        fp.write("\n")
    t=input("Wanna create more accounts?\n1 or Yes or Y->YES!\nANYTHING ELSE->NO!\n")
    if(t.upper()=='YES' or t.upper()=='Y' or t=='1'):
        k='True'
    else:
        k='False'
driver.quit()

