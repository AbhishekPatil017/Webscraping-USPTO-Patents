#Import selenium and beautiful soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import *

#download and copy paste the geckodriver.exe i am using firefox geckodriver to run selenium webdriver script
driver=webdriver.Firefox(executable_path=r'C:\Users\admin\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe')
#number of pages you want to iterate. 
pages=10

for page in range(1,pages):
#dynamic url to iterate through every page once download of one page is completed.

 url="http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=" + str(page) + "&u=%2Fnetahtml%2FPTO%2Fsearch-bool.html&r=0&f=S&l=50&TERM1=Energy&FIELD1=&co1=AND&TERM2=&FIELD2=&d=PTXT"
 driver.get(url)

#using xpath to copy all the links from the webpage and store it in the list 
 pattern_page_list=driver.find_elements_by_xpath('/html/body/table/tbody/tr/td[4]/a')
 link_list=[]

 #iterate the list of pattern links and get the href tag and store it in temporary list.
 for link in pattern_page_list:
    temp_link=link.get_attribute('href')
    link_list.append(temp_link)

 #create dynamic document to store every single pattern from the webbrowser.   
 #Remember i am using 'a'-append to store all pattern data into one file, every time you run the script append method will copy data into the same file.
 F=open('patent_data.txt','a')
 
 #automation script of opening the links and closing once the pattern is copied to the document folder.
 for mylinks in link_list:
      driver.get(mylinks)
      driver.find_elements_by_tag_name('a')[1].send_keys(Keys.CONTROL +'t')
      driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)

#you can use Beautiful soup or selenium webdriver to get the pattern-data , i suggest using selenium webdriver because finding element by using xpath is much easier.
      soup=BeautifulSoup(driver.page_source)
     # patent_number = soup.find('font')
  
# i wanted to get patent_number,paragraph,description,abstract and application information.

      patent_number=driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td[2]/font[1]/strong')
      paragraph=soup.find('p')
      description=driver.find_element_by_xpath('/html/body/font')
      abstract=driver.find_element_by_xpath('/html/body/center[2]')
      Application_info=driver.find_element_by_xpath('/html/body/table[3]/tbody')
     
# concate and sort it to readable format then store it in variable to write all the text data in the document file.

      mydata = patent_number.text +'\t'+ description.text + '\n\n' + abstract.text + '\n\n' + paragraph.text + '\n' + Application_info.text
      F.write(mydata+'\n\n')
  
#close the driver once every link and data is copied from all the url
driver.close()
