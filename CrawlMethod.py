from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time
#from selenium.webdriver.common.proxy import *

#myProxy = "10.3.100.207:8080"

'''proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': '' # set this value as desired
    })'''


def write_to_json(dictionary,filename):
    f=open(filename,'w')
    g=json.dumps(dictionary)
    f.write(g)
    f.close()


def get_page(url,count,path_write):
    #global proxy
    #browser=webdriver.Firefox(proxy=proxy)
    commdict = [{'Author':0,'ReplyTo':0,'Content':0,'TimeStamp':0} for k in range(0,1020)]
    q=-1
    err_cnt=0
    for j in range(1,21):
        try:
            if j==1:
                browser.get(url)
                time.sleep(2)
            else:
                url2=url+'?page='+str(j)
                browser.get(url2)
                time.sleep(2)
            x=browser.page_source
            soup=BeautifulSoup(x)
            check=soup.findAll('div',{'class':'d-comment__inner'})
            for i in range(len(check)):
                q+=1
                commdict[q]['Author'] = check[i].find('span',{'class':'d-comment__author'}).text.strip()
                commdict[q]['ReplyTo'] = check[i].find('span',{'class':'d-comment__reply-to-author'})
                if commdict[q]['ReplyTo']!=None:
                    commdict[q]['ReplyTo']=commdict[q]['ReplyTo'].text.strip()
                commdict[q]['TimeStamp']=check[i].find('div',{'class':'d-comment__timestamp'}).text.strip()
                #print(commdict[i]['TimeStamp'])
                commdict[q]['Content'] = check[i].find('div',{'class':'d-comment__content'}).text.strip()
        except:
            err_cnt+=1
            if err_cnt>=5:
                break
            else:
                pass
    write_to_json(commdict,path_write+"ArticleComments_"+str(count))

def get_maindata(url,count,path_write):
    #global proxy
    #browser=webdriver.Firefox(proxy=proxy)
    browser.get(url)
    time.sleep(2)
    x=browser.page_source
    soup=BeautifulSoup(x)
    artdict={'Headline':0,'Article':0}
    headline=soup.find('h1',{'class':'content__headline'}).text.strip()
    artdict['Headline']=headline
    body=soup.find('div',{'class':'content__article-body'}).text
    artdict['Article']=body
    comm_url=soup.find('div',{'class':'container__meta'})
    comm_url=comm_url.find('a')
    comm_url=comm_url.get('href')
    write_to_json(artdict,path_write+"ArticleStory_"+str(count))
    get_page(comm_url,count,path_write)

def getlinkarr(path,filename):
    arr=[]
    f=open(path+filename,'r')
    i=0
    for row in f:
        i+=1
        if i%2==1:
            arr.append(str(row))
    return arr

def main():
    path='C:/Users/Anindya Bhandari/Downloads/IRCodes/reguardiandataset/'
    path_write='C:/Users/Anindya Bhandari/Downloads/IRCodes/'
    #business=getlinkarr(path,'Business.txt')
    #politics=getlinkarr(path,'Politics.txt')
    #world=getlinkarr(path,'World.txt')
    environment=getlinkarr(path,'Environment.txt')
    #lifestyle=getlinkarr(path,'Lifestyle.txt')
    #opinion=getlinkarr(path,'Opinion.txt')
    #sport=getlinkarr(path,'Sports.txt')
    technology=getlinkarr(path,'Technology.txt')
    '''for i in range(0,len(business)):
        #time.sleep(2)
        try:
            get_maindata(business[i],(49+i),path_write+'Business/')
        except:
            pass
    
    for i in range(0,len(environment)):
        #time.sleep(2)
        try:
            get_maindata(environment[i],(58+i),path_write+'Environment/')
        except:
            pass
    
    for i in range(0,len(lifestyle)):
        #time.sleep(2)
        try:
            get_maindata(lifestyle[i],(46+i),path_write+'Lifestyle/')
        except:
            pass
        
    for i in range(2,len(opinion)):
        #time.sleep(2)
        try:
            get_maindata(opinion[i],(41+i),path_write+'OpinionNew/')
        except:
            pass
        
    for i in range(0,len(sport)):
        #time.sleep(2)
        try:
            get_maindata(sport[i],(42+i),path_write+'Sport/')
        except:
            pass
    '''
    print(len(technology))
    for i in range(27,len(technology)):
        #time.sleep(2)
        try:
            get_maindata(technology[i],(45+i),path_write+'Technology/')
        except:
            pass
    '''for i in range(0,len(politics)):
        #time.sleep(2)
        try:
            get_maindata(politics[i],(50+i),path_write+'PoliticsNew/')
        except Exception as e:
            print(e)
            pass
        
    for i in range(0,len(world)):
        #time.sleep(2)
        try:
            get_maindata(world[i],(35+i),path_write+'World/')
        except Exception as e:
            print(e)
            pass'''
browser=webdriver.Firefox()#proxy=proxy)
main()

