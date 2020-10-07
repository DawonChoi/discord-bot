from selenium import webdriver
import math

driver = webdriver.Chrome('C:/discord-bot/util/chromedriver.exe')
driver.get('http://www.op.gg/')

# commit test in Github Desktop third final

def search(summoner):
    driver.implicitly_wait(3)
    try:
        search_input = driver.find_element_by_class_name('summoner-search-form__text._suggest')
    except:
        search_input = driver.find_element_by_class_name('gnb-list-item__input._suggest')
    search_input.send_keys(summoner)
    
    try:
        search_button = driver.find_element_by_class_name('summoner-search-form__button')
    except:
        search_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/div/form/button')
    search_button.click()
    
    #summoner's solorank history
    sololank = driver.find_element_by_xpath('//*[@id="right_gametype_soloranked"]/a')
    sololank.click()

#get a result of solorank
def history(scope):
    history_list = []
    for i in range(1, scope+1):
        result = driver.find_element_by_xpath(f'//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[{i}]/div/div[1]/div[1]/div[4]')
        history_list.append(result.text)
    
    return history_list

#caculate rating in history scope
def rating(scope):
    rate = []
    for i in range(1, scope+1):
        kill = driver.find_element_by_xpath(f'//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[{i}]/div/div[1]/div[3]/div[1]/span[1]').text
        death = driver.find_element_by_xpath(f'//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[{i}]/div/div[1]/div[3]/div[1]/span[2]').text
        assist = driver.find_element_by_xpath(f'//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[{i}]/div/div[1]/div[3]/div[1]/span[3]').text
        
        if float(death) == 0.0:
            rate.append(round((float(kill)+float(assist)), 2))
        else:
            rate.append(round((float(kill)+float(assist))/float(death), 2))
    return rate

# return kill death assist with meaning formatting
def KDA(scope):
    kda = []
    for i in range(1, scope+1):
        kill = driver.find_element_by_xpath(f'//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[{i}]/div/div[1]/div[3]/div[1]/span[1]').text
        death = driver.find_element_by_xpath(f'//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[{i}]/div/div[1]/div[3]/div[1]/span[2]').text
        assist = driver.find_element_by_xpath(f'//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[{i}]/div/div[1]/div[3]/div[1]/span[3]').text
        
        kda.append(f"{kill}킬 {death}데스 {assist}어시")
    return kda

# if one of your team player defeated a previous game that over time 40min, Bot will recommend you dodging
def dodge(summoner):
    search(summoner)
    minute, result = time_parser()
    if int(minute) >= 40 and result == '패배':
        return True
    return False    


def time_parser():
    time = driver.find_element_by_xpath(f'//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/div[5]').text
    result = driver.find_element_by_xpath(f'//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/div[4]').text
    return time[:2], result


if dodge('블랙핑크 로제팬') == True:
    print('dodge')
else:
    print('needless')
