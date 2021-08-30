from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep

from random import randint as ri 
from random import choice as ch

import pyperclip 

PATH = 'F:/Virtual Environment/Shared/python_projects/ChromeDriver/chromedriver.exe'

class Cookie():
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)
        self.clicker()
        
    def open(self):
        '''opens the coockie clicker website'''
        self.driver.get('https://orteil.dashnet.org/cookieclicker/')
        sleep(5)
        window = self.driver.window_handles[0] #changes the window from the cookie popup
        self.driver.switch_to_window(window)
        self.driver.fullscreen_window() 
        sleep(2)
 
    def click(self):
        '''finds the big cookie and clicks it'''

        btn = self.driver.find_element_by_id('bigCookie') #finds the cookie by ID
        i = ri(100, 5000) #randomly chooses how many clicks should be done
        click = 0

        print(f'Clicks made this round: {i}') #prints how many clicks were done this round
        while click < i:
            btn.click()   
            click += 1 
            if click % 100 == 0:
                self.goldenCOOKIE()
            else:
                continue
        return i       

    def item(self):
        '''sorts through the  items and buys them'''
        click = 0 #resets the click count for the self.click() 
        items = ['product' + str(i) for i in range(18, -1, -1)] #list of all item IDs
        multiplier = ch(['one', 'ten', 'hundred']) #randomly chooses whtehre to buy 1, 10 or 100 goods
        print(f'We will buy {multiplier} building(s)') # informs you about the multiplier selected
        while True:
            if multiplier == 'one':
                for item in items:
                    try:
                        item = self.driver.find_element_by_id(item)
                        item.click()
                    except:
                        continue 
                return click         
            elif multiplier == 'ten':       
                webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).perform()
                for item in items:
                    try:
                        item = self.driver.find_element_by_id(item)
                        item.click()
                    except:
                        continue 
                webdriver.ActionChains(self.driver).key_up(Keys.CONTROL).perform()
                return click
            elif multiplier == 'hundred':       
                webdriver.ActionChains(self.driver).key_down(Keys.SHIFT).perform()
                for item in items:
                    try:
                        item = self.driver.find_element_by_id(item)
                        item.click()
                    except:
                        continue 
                webdriver.ActionChains(self.driver).key_up(Keys.SHIFT).perform()
                return click
                   
    def upgrade(self):
        '''buys upgrades'''
        try:
            upgrade = self.driver.find_element_by_id('upgrade0')
            upgrade.click()
        except:
            pass
    
    def load(self):
        '''
        loads the gave
        '''
        try:
            with open('MetalPancakeBakery.txt') as save:
                save = save.read()
                pyperclip.copy(save)
        
            webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('o').perform()#hotkye for opening the load window
            sleep(1)
            webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').perform()#copy paste the link 
            load_button = self.driver.find_element(By.ID, 'promptOption0') # click the load button 
            load_button.click()
        except:
            pass
        
    def save(self):
        '''saves the game''' 
        options = self.driver.find_element(By.ID, 'prefsButton')
        options.click() 
        export = self.driver.find_element(By.LINK_TEXT, 'Export save')
        export.click()
        webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('c').perform()
        
        with open('MetalPancakeBakery.txt', 'w') as test:
            test.write(pyperclip.paste())
        
        all_done = self.driver.find_element(By.ID, 'promptOption0') # click the all done button
        all_done.click() 
        close = self.driver.find_element_by_class_name('menuClose')
        close.click()
        
    def goldenCOOKIE(self):
        '''
        monitors the appearing of the golden cookie on the screen and clicks it once it is present
        '''
        try:
            cookieg = self.driver.find_element_by_class_name('shimmer')
            cookieg.click()
        except:
            pass
            
    def sugarLUMP(self):
       '''
       does smthng with the sugar lump (have no idea what that is yet)
       DOESN'T WORK YET
       '''
       pass       

    def clicker(self):
        '''cookie clicker bot'''
        
        self.open()
        self.load()
      
        rounds = 1
        clicks = 0
        while rounds < 10_000:
            try:    
                print('____________________')
                print(f'This is round # {rounds}/10 000')
            
                clicks += self.click()   
                print(f'Totla clicks: {clicks}')
                
                self.upgrade()
                self.item()
                
                rounds += 1 
                if rounds % 5 == 0:
                    try:
                        self.save()
                        print('Game saved')
                    except:
                        print('did not save')
                        pass
                
            except:
                continue

if __name__ == '__main__':
    bot = Cookie()







        
       
            
        
            



       

 
        
     






