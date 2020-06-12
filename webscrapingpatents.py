from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import *

driver=webdriver.Firefox(executable_path=r'C:\Users\admin\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe')
pages=10

for page in range(1,pages):

 url="http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=" + str(page) + "&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1=Energy&FIELD1=&co1=AND&TERM2=&FIELD2=&d=PTXT"
 driver.get(url)
 pattern_page_list=driver.find_elements_by_xpath('/html/body/table/tbody/tr/td[4]/a')
 link_list=[]

 for link in pattern_page_list:
    temp_link=link.get_attribute('href')
    link_list.append(temp_link)

 F=open('patent_data.txt','a')
 for mylinks in link_list:
      driver.get(mylinks)
      driver.find_elements_by_tag_name('a')[1].send_keys(Keys.CONTROL +'t')
      driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)

      soup=BeautifulSoup(driver.page_source)
     # patent_number = soup.find('font')
      patent_number=driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[2]/font[1]/strong')
      paragraph=soup.find('p')
      description=driver.find_element_by_xpath('/html/body/font')
      abstract=driver.find_element_by_xpath('/html/body/center[2]')
      Application_info=driver.find_element_by_xpath('/html/body/table[3]/tbody')

      mydata = patent_number.text +'\t'+ description.text + '\n\n' + abstract.text + '\n\n' + paragraph.text + '\n' + Application_info.text
      F.write(mydata+'\n\n')
      print('test')
driver.close()