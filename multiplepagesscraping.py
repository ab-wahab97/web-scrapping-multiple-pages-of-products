import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

name=[]
price=[]
stock=[]
for num in range(1,10):
    url="https://www.czone.com.pk/laptops-pakistan-ppt.74.aspx?page="+str(num)
    html=requests.get(url).text

    soup=BeautifulSoup(html,'lxml')

    products=soup.find_all('div',class_='product')

    
    for i in products:
        name.append(i.find('h4').text)
        price.append(i.find('div',class_='price').text)
        

    new1=[re.sub(r'\n','',j) for j in price]

df=pd.DataFrame({'Name':name,'Price':new1})


df.to_csv('LaptopPrices.csv')




# url='https://www.czone.com.pk/laptops-pakistan-ppt.74.aspx?page='+str(i)

# html=requests.get(url).text

# soup=BeautifulSoup(html,'lxml')
    # link=soup.find('a',id='anNextPage',class_='NextPage').get('href')

    # completelink='https://www.czone.com.pk'+link

        
    # print(completelink)




    
    
    









    
