import urllib.request, urllib.error, urllib.parse
from datetime import date, datetime
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def UtcNow():
    now = datetime.utcnow()
    return (now - datetime(1970, 1, 1)).total_seconds()


def CheckCreateFolder(folder):

    CHECK_FOLDER = os.path.isdir(folder)
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(folder)
        print("created folder : ", folder)

#########
SA = {'url': 'https://sacoronavirus.co.za/', 'name': 'South Africa'}
BR = {'url': 'https://sacoronavirus.co.za/', 'name': 'Brazil'}
CO = {'url': 'https://www.ins.gov.co/Noticias/Paginas/Coronavirus.aspx/',
      'name': 'Colombia'}
CZ = {'url': 'https://onemocneni-aktualne.mzcr.cz/covid-19',
      'name': 'Czech Republic'}
PH = {'url': 'https://www.doh.gov.ph/2019-nCoV', 'name': 'Philippines'}
ON = {'url': 'https://www.ontario.ca/page/2019-novel-coronavirus', 'name': 'Ontario'}
MA = {'url': 'http://www.moh.gov.my/index.php/pages/view/2019-ncov-wuhan', 'name': 'Malaysia'}
LA = {'url': 'https://arkartassituacija.gov.lv/', 'name': 'Latvia'}
IN = {'url': 'https://infeksiemerging.kemkes.go.id/', 'name':'Indonesia'}
SK = {'url': 'https://www.korona.gov.sk/', 'name': 'Slovakia'}
KO = {'url': 'http://ncov.mohw.go.kr/en/', 'name': 'Korea'}
#########
ES = {'url': 'https://www.terviseamet.ee/et/koroonaviirus/koroonakaart', 'name': 'Estonia'}
NO={'url': 'https://www.fhi.no/en/id/infectious-diseases/coronavirus/daily-reports/daily-reports-COVID19', 'name': 'Norway'}
AS={'url': 'https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert/coronavirus-covid-19-current-situation-and-case-numbers', 'name': 'Australia'}
FI={'url': 'https://thl.fi/en/web/infectious-diseases/what-s-new/coronavirus-covid-19-latest-updates', 'name': 'Finland'}
SE={'url': 'https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/aktuellt-epidemiologiskt-lage/', 'name': 'Sweden'}
SL={'url': 'https://www.gov.si/teme/koronavirus/', 'name': 'Slovenia'}
AR={'url': 'https://ncdc.am/coronavirus/confirmed-cases-by-days/', 'name': 'Armenia'}



country_list = [AR]

for country in country_list:
    print(country['name'])
    CheckCreateFolder(country['name'])

    response = urllib.request.urlopen(country['url'])
    webContent = response.read()
    #print(webContent)

    saveFile = True
    if saveFile is True:
        print('test')
        f = open('./'+country['name']+'/'+'gov-'+country['name']+'-'+str(date.today())+'-'
                 + str(UtcNow()), 'wb')
        f.write(webContent)
        f.close
        print('test')
        f = open('./'+country['name']+'/'+'gov-'+country['name']+'-'+str(date.today())+'-'
                 + str(UtcNow())+'.txt', 'wb')
        f.write(webContent)
        f.close
