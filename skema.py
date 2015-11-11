from bs4 import BeautifulSoup

doc = open("Eleven Gustav Stokholm Falkenthros, htx 1z - Skema - Lectio - Slotshaven Gymnasium.html")
soup = BeautifulSoup(doc, 'html.parser')
x = soup.find('table',
              id='s_m_Content_Content_SkemaNyMedNavigation_skema_skematabel')

weekhtml = x.find('tbody').find_all('tr')[0].find('td')
dayshtml = x.find('tbody').find_all('tr')[1].find_all('td')[1:]
weekdaysinfohtml = x.find('tbody').find_all('tr')[2].find_all('td')[1:]
schedulehtml = x.find('tbody').find_all('tr')[3].find_all('td')[1:]


for x in weekdaysinfohtml:
    for info in x:
        for point in info.find_all('div'):
            [print(x.find_all('span')[1].contents)
             for x in point.find_all('div')]
                                        

##########################################################################################################
# infodays = []                                                                                          #
# for i in list(range(0,len(infohtml))):                                                                 #
#     infodays.append(infohtml[i].find_all('a')[0].find('div').find('div').find_all('span')[1].contents) #
##########################################################################################################
