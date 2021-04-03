#!/usr/bin/env python3

import re
import arrow
from bs4 import BeautifulSoup
import scrape_common as sc


main_url = 'https://www.sg.ch/ueber-den-kanton-st-gallen/statistik/covid-19.html'
url = 'https://stada.sg.ch/covid/Durchimpfung_SG.html'
d = sc.download(url)
soup = BeautifulSoup(d, 'html.parser')

vd = sc.VaccinationData(canton='SG', url=main_url)

element = soup.find('td', string=re.compile(r'Total verabreichte Impfdosen'))
element = element.find_next('td')
vd.total_vaccinations = int(element.text)

element = soup.find('td', string=re.compile(r'Anzahl vollst.ndig geimpfte Personen'))
element = element.find_next('td')
vd.second_doses = int(element.text)

vd.first_doses = vd.total_vaccinations - vd.second_doses

print(vd)
