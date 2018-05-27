#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import sys
from selenium import webdriver
from bs4 import BeautifulSoup


# 获取HTML
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    return html.text


# 获取含有js加载的HTML
def get_js_html(url):
    try:
        driver = webdriver.PhantomJS()
        driver.get(url)
        html = driver.page_source
        return html
        driver.close()
    except:
        url_down = 'http://220.194.71.1/d0.ananas.chaoxing.com/download/31873a33becb605c36322ec16382443f'
        python_path = sys.executable[:-10] + '\\'
        name = python_path + 'phantomjs.exe'
        print('初次运行，环境配置中。。。')
        phan = requests.get(url_down).content
        with open(name, 'wb') as f:
            f.write(phan)
        driver = webdriver.PhantomJS()
        driver.get(url)
        html = driver.page_source
        return html
        driver.close()


# 查找元素
def find(html, a, class_):
    soup = BeautifulSoup(html, 'html5lib')
    finds = soup.find(a, class_=class_)
    return finds


# 获取网站所以url
def find_all_links(html):
    if '</html>' in html:
        soup = BeautifulSoup(html, 'html5lib')
        find_links = soup.find_all('a')
        link_list = []
        for a in find_links:
            try:
                url_li = a['href']
            except:
                continue
            link_list.append(url_li)
        return set(link_list)
    else:
        find_links = html.find_all('a')
        link_list = []
        for a in find_links:
            try:
                url_li = a['href']
            except:
                continue
            link_list.append(url_li)
        return link_list


# 获取文本
def find_text(html):
    if '<html>' in html:
        soup = BeautifulSoup(html, 'html5lib')
        find_links = soup.find_all('a')
        link_list = []
        for a in find_links:
            try:
                url_li = a.get_text("", strip=True)
            except:
                continue
            link_list.append(url_li)
        return link_list
    else:
        find_links = html.find_all('a')
        link_list = []
        for a in find_links:
            try:
                url_li = a.get_text("", strip=True)
            except:
                continue
            link_list.append(url_li)
        return link_list


# 获取所以图片链接
def get_imgs(html):
    soup = BeautifulSoup(html, 'html5lib')
    find_imgs = soup.find_all('img')
    img_list = [a['src'] for a in find_imgs]
    return set(img_list)

