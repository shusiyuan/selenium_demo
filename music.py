# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By

singers= {}
authors= []
driver = webdriver.Chrome()
driver.get("https://y.qq.com/n/ryqq/toplist/5")
songnames = driver.find_elements(By.XPATH,"//i[@class='icon_rank_up']/ancestor::div[contains(@class,'songlist__item')]/div[@class='songlist__songname']/span/a[@class='songlist__cover']/following-sibling::a")
upnums = driver.find_elements(By.XPATH,"//i[@class='icon_rank_up']/parent::div[@class='songlist__rank']")
ranknums = driver.find_elements(By.XPATH, "//i[@class='icon_rank_up']/ancestor::div[contains(@class,'songlist__item')]/div[@class='songlist__number ']")
for b in songnames:
    authors = driver.find_elements(By.XPATH, "//a[@title='{songname}']/ancestor::div[contains(@class,'songlist__item')]//i[@class='icon_rank_up']/ancestor::div[contains(@class,'songlist__item')]/div[@class='songlist__artist']/a".format(songname = b.text)) #通过歌曲名字定位歌手
    for i in authors:
        stop = False
        real_songs = driver.find_elements(By.XPATH, "//a[@title='{author}']/ancestor::div[contains(@class,'songlist__item')]/div[@class='songlist__songname']/span/a[@class='songlist__cover']/following-sibling::a".format(author = i.text))
        for a in real_songs: #双重保险，通过歌手名反向查找歌曲名再验证，防止有歌曲的title写成另外一首歌了,如果找到的歌曲名与之前定位的歌曲名不一致，这个歌手就不加入到singers里了
            if b.text != a.text:
                stop = True
        if stop:
            continue
            stop = False
        if b.text in singers:
            singers[b.text] = singers[b.text] + '/' + i.text
        else:
            singers[b.text] = i.text
print ('qq音乐内地榜排名攀升势头的歌曲如下：')
for i in range(0,len(songnames)):
    print ('歌曲名：{songname}，歌手：{author}，上升排名数：{upnum}，目前排名：{ranknum}'.format(songname = songnames[i].text, author = singers[songnames[i].text], upnum = upnums[i].text, ranknum = ranknums[i].text))



