# 高级爬虫库[requests_htmls](https://github.com/msterzhang/requests_htmls) #

![](http://p16.qhimg.com/t016924b01742e3063a.jpg)

# 介绍： #

##  该库是我对常用的爬虫库进行封装，产生的高级库，旨在尽可能简单直观地解析HTML，欢迎大家Fork。当使用这个库时，你会自动获得: 

* 集请求与解析于一个库。
* 完全支持javascript,能够获取javascript加载后的HTML。
* 适合小白，代码简单，更容易的上手,轻松爬取图片，链接。

## 安装依赖库，可直接双击运行install.bat文件进行安装： ##
    pip install requests
	pip install beautifulsoup
	pip install selenium
	pip install html5lib

## 此库的安装： ##

* `git clone https://github.com/msterzhang/requests_htmls `,得到requests_htmls.py文件，放在python安装目录：D:\python\Lib\site-packages中，site-packages文件夹里，别搞错了，便可以直接导入使用。
# 使用教程： #

> 这里使用我的博客做教程，因为我的博客里的有一部分内容是通过javascript加载的，域名还没审批下来。

## 一.获取html： ##

### 注意看以下html的区别： ###
    

    <header>
        <a class="label label-important" id='biao' href="">标签：2 <i
                class="label-arrow"></i>
        </a>
        <h2>
            <a target="_blank" href="/program/6/"
               title="django配置mysql数据库问题解决">django配置mysql数据库问题解决 </a>
        </h2>
    </header>

### 1.获取静态页面的html： ###
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
    from requests_htmls import get_html

	url = 'http://39.108.216.131/program/'
	html = get_html(url)
	print(html)
#### 得到： ####
    <header>
        <a class="label label-important" id='biao' href="">标签：2 <i
                class="label-arrow"></i>
        </a>
        <h2>
            <a target="_blank" href="/program/6/" title="django配置mysql数据库问题解决">django配置mysql数据库问题解决 </a>
        </h2>
    </header>

### 2.获取javascript加载后的html： ###
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
    from requests_htmls import get_js_html

	url = 'http://39.108.216.131/program/'
	html = get_js_html(url)
	print(html)

#### 得到： ####
	<header>
        <a class="label label-important" id="biao" href="">标签：django</a>
        <h2>
            <a target="_blank" href="/program/6/" title="django配置mysql数据库问题解决">django配置mysql数据库问题解决 </a>
        </h2>
    </header>

## 二.解析html ##

### 1.获取元素，和BeautiSoup的用法完全相同，注意光标点的地方： ###

![](https://i.imgur.com/KNSwqDR.jpg)
---

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
    from requests_htmls import get_js_html
	from requests_htmls import find
	
	url = 'http://39.108.216.131/program/'
	html = get_js_html(url)
	find = find(html,'div',class_='label')
	print(find)


#### 得到： ####
    
    <div class="label">
            
                <article class="excerpt">
                    <header>
                        <a class="label label-important" href="" id="biao">标签：django</a>
                        <h2>
                            <a href="/program/6/" target="_blank" title="django配置mysql数据库问题解决">django配置mysql数据库问题解决 </a>
                        </h2>
                    </header>
                    <div class="focus">
                        <a href="/program/6/" target="_blank">
                            <!--<img class="thumb" src="" style="" alt="django配置mysql数据库问题解决">-->
                        </a>
                    </div>
                    <span class="note"><h6>windows本地django配置mysql数据库问题解决...</h6>
                    <p>发布时间：2018-04-21   11:04     阅读量：0 </p>
                    </span>
                </article>
                <h1></h1>
                <h1></h1>
            
                <article class="excerpt">
                    <header>
                        <a class="label label-important" href="" id="biao">标签：有趣的小项目</a>
                        <h2>
                            <a href="/program/5/" target="_blank" title="文本转音频并自动播放">文本转音频并自动播放 </a>
                        </h2>
                    </header>
                    <div class="focus">
                        <a href="/program/5/" target="_blank">
                            <!--<img class="thumb" src="" style="" alt="文本转音频并自动播放">-->
                        </a>
                    </div>
                    <span class="note"><h6>这个项目可以批量将文本转为音频，并且支持一般播放器播放，这里我们使用了python的一个库来播放，主要是源于我自己做的一个语音聊天机器人...</h6>
                    <p>发布时间：2018-04-21   11:04     阅读量：6 </p>
                    </span>
                </article>
                <h1></h1>
                <h1></h1>
            
        </div>

### 2.获取网页所有链接： ###
    #!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from requests_htmls import get_html
	from requests_htmls import find_all_links
	
	url = 'http://39.108.216.131/program/'
	html = get_html(url)
	find = find_all_links(html)
	print(find)

#### 运行结果： ####
    {'', '/program/6/', '/qu/', 'http://duanxu0830.top/', '/program/', '/program/5/', '/program/3/', '/program/2/', '/robot/', '/django/', '/program/1/', '/flask/', '/pa/', '/shijue/', '/ji/', '/program/4/', 'https://github.com/msterzhang', '/'}

### 3.获取图片链接 ###
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	
	from requests_htmls import get_js_html
	from requests_htmls import get_imgs
	
	url = 'http://jandan.net/ooxx/page-87'
	html = get_js_html(url)
	find = get_imgs(html)
	print(find)

#### 运行结果： ####
    {'http://ws4.sinaimg.cn/mw600/006DuZvsgy1fqk2dopstkj30dw0ku75k.jpg', 'http://wx1.sinaimg.cn/mw600/6cca1403ly1fqk0r7re58j20gm0giabh.jpg', 'http://wx2.sinaimg.cn/mw600/e0e4ecc3gy1fqk2xtpwl7j20tt18gn6m.jpg', 'http://ww3.sinaimg.cn/mw600/0073ob6Pgy1fqk23yeay0j30v80ngx1c.jpg', 'http://wx3.sinaimg.cn/mw600/47850a75ly1fe4aumtjqfj20dw0kst9l.jpg', 'http://wx4.sinaimg.cn/mw600/cef04520ly1fqeocjlwpkj21wq2v31kz.jpg', 'http://ww3.sinaimg.cn/mw600/0073ob6Pgy1fqk23jtk7oj318g1v8u0z.jpg', 'http://wx4.sinaimg.cn/mw600/cef04520ly1fqeocpqeocj20rs15oteo.jpg', 'http://ww3.sinaimg.cn/mw600/006XNEY7gy1fqk1f0h6brj312011zwkc.jpg', 'http://wx1.sinaimg.cn/mw600/e0e4ecc3gy1fqk4j4735cj215o0ngak3.jpg', 'http://ww2.sinaimg.cn/mw600/47850a75jw1f46610ze0nj20qo0qoq73.jpg', 'http://ww3.sinaimg.cn/mw600/0073ob6Pgy1fqk1q23bgej30zk1bf79q.jpg', 'http://wx4.sinaimg.cn/mw600/e0e4ecc3gy1fqk2yhi9qwj20u00ybae2.jpg', 'http://wx4.sinaimg.cn/mw600/6cca1403ly1fqj8bgj8puj20p60ddwf0.jpg', 'http://wx4.sinaimg.cn/mw600/e0e4ecc3gy1fqk2ysk2mej20u0102q88.jpg', 'http://ww3.sinaimg.cn/mw600/0073ob6Pgy1fqk1hjvlb0j306y07jt96.jpg', 'http://wx3.sinaimg.cn/mw600/cef04520ly1fqeocnztj0j21qy2bckjl.jpg', 'http://ww3.sinaimg.cn/mw600/0073tLPGgy1fqk240ma5kj30v80ngx1c.jpg', 'http://ww3.sinaimg.cn/mw600/47850a75jw1f5w4rooqlnj20qo0qo458.jpg', 'http://ww3.sinaimg.cn/mw600/006XNEY7gy1fqk23vudz0j312w1x5u0z.jpg', 'http://ww3.sinaimg.cn/mw600/be421314jw1epob2clpz0j20dw0jeabl.jpg', 'http://ws1.sinaimg.cn/mw600/006EPd1dgy1fqk31of820j30g40o6dh9.jpg', '//cdn.jandan.net/static/sos/699pic/5.png', 'http://ws2.sinaimg.cn/mw600/00671KYngy1fqk2b3mvi4j316o1kw4dt.jpg', 'http://ww3.sinaimg.cn/mw600/0073tLPGgy1fqk1opww38j30hs0hs0ue.jpg', 'http://ww3.sinaimg.cn/mw600/0073ob6Pgy1fqk1elvrt3j30un0uogpd.jpg', 'http://wx2.sinaimg.cn/mw600/cef04520ly1fqeoconabhj20pu0z4481.jpg', 'http://ww3.sinaimg.cn/mw600/0073ob6Pgy1fqk1pplkbgj30ku0ku770.jpg'}
