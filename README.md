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

> `git clone https://github.com/msterzhang/requests_htmls `,得到requests_htmls.py文件，放在python安装目录：D:\python\Lib\site-packages中，site-packages文件夹里，别搞错了，便可以直接导入使用。
# 使用教程： #

> 这里使用我的博客做教程，因为我的博客里的有一部分内容是通过javascript加载的，域名还没审批下来。

## 一.获取html： ##

### 注意看以下html的区别，标签的位置： ###
    

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
#### 运行结果： ####
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

#### 运行结果： ####
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


#### 运行结果： ####
    
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
    {'http://ws4.sinaimg.cn/mw600/006DuZvsgy1fqk2dopstkj30dw0ku75k.jpg', 'http://wx1.sinaimg.cn/mw600/6cca1403ly1fqk0r7re58j20gm0giabh.jpg', 'http://wx2.sinaimg.cn/mw600/e0e4ecc3gy1fqk2xtpwl7j20tt18gn6m.jpg', 'http://ww3.sinaimg.cn/mw600/0073ob6Pgy1fqk23yeay0j30v80ngx1c.jpg', 'http://wx3.sinaimg.cn/mw600/47850a75ly1fe4aumtjqfj20dw0kst9l.jpg', 'http://wx4.sinaimg.cn/mw600/cef04520ly1fqeocjlwpkj21wq2v31kz.jpg', 'http://ww3.sinaimg.cn/mw600/0073ob6Pgy1fqk23jtk7oj318g1v8u0z.jpg', 'http://wx4.sinaimg.cn/mw600/cef04520ly1fqeocpqeocj20rs15oteo.jpg', 'http://ww3.sinaimg.cn/mw600/006XNEY7gy1fqk1f0h6brj312011zwkc.jpg', 'http://wx1.sinaimg.cn/mw600/e0e4ecc3gy1fqk4j4735cj215o0ngak3.jpg', 'http://ww2.sinaimg.cn/mw600/47850a75jw1f46610ze0nj20qo0qoq73.jpg', 'http://ww3.sinaimg.cn/mw600/0073ob6Pgy1fqk1q23bgej30zk1bf79q.jpg', 'http://wx4.sinaimg.cn/mw600/e0e4ecc3gy1fqk2yhi9qwj20u00ybae2.jpg', 'http://wx4.sinaimg.cn/mw600/6cca1403ly1fqj8bgj8puj20p60ddwf0.jpg', 'http://wx4.sinaimg.cn/mw600/e0e4ecc3gy1fqk2ysk2mej20u0102q88.jpg', 'http://ww3.sinaimg.cn/mw600/0073ob6Pgy1fqk1hjvlb0j306y07jt96.jpg', 'http://wx3.sinaimg.cn/mw600/cef04520ly1fqeocnztj0j21qy2bckjl.jpg', 'http://ww3.sinaimg.cn/mw600/0073tLPGgy1fqk240ma5kj30v80ngx1c.jpg', 'http://ww3.sinaimg.cn/mw600/47850a75jw1f5w4rooqlnj20qo0qo458.jpg', 'http://ww3.sinaimg.cn/mw600/006XNEY7gy1fqk23vudz0j312w1x5u0z.jpg', 'http://ww3.sinaimg.cn/mw600/be421314jw1epob2clpz0j20dw0jeabl.jpg', 'http://ws1.sinaimg.cn/mw600/006EPd1dgy1fqk31of820j30g40o6dh9.jpg'}

### 4.获取文本 ###
    #!/usr/bin/env python
	# -*- coding: utf-8 -*-
	from requests_htmls import get_html
	from requests_htmls import find_all_links
	from requests_htmls import find,find_text
	
	
	def get_url(i):
	    if i == 0:
	        return 'http://www.gzgov.gov.cn/xwdt/gzyw/index.html'
	    else:
	        return 'http://www.gzgov.gov.cn/xwdt/gzyw/index_{}.html'.format(i)
	
	
	def get_find(url):
	    html = get_html(url)
	    html2 = find(html,'div',class_='right-list-box')
	    text_list = find_text(html2)
	    url_list = find_all_links(html2)
	    for a,b in zip(text_list,url_list):
	        print(a,b)
	
	
	if __name__ == '__main__':
	    for i in range(1):
	        url = get_url(i)
	        get_find(url)

#### 运行结果： ####
    贵州水利改革发展迎来“开门红” 一季度落实水利投资近180亿元 http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180422_1114760.html
	31万人参加“省考” 最俏岗位招录比1725:1 http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180422_1114759.html
	一季度贵州消费增速位居全国第三 http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180422_1114758.html
	2018年贵州省考21日开考 平均招录比约为68:1 http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180421_1114754.html
	“一带一路”南向通道贵州段测试班列开通运行 http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180421_1114753.html
	贵州：对外经济技术合作一季度实现“开门红” http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180421_1114752.html
	贵州磷化工行业刮起“绿色旋风” http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180421_1114751.html
	共话新时代贵州教育改革发展圆桌会议举行 http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180421_1114750.html
	2017年贵州植被生态质量及改善均列全国第六 http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180420_1114613.html
	贵州省首款智能电动汽车在京亮相 http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180420_1114614.html
	贵州：大数据驱动社会治理升级 http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180420_1114639.html
	贵州教育云：让智慧教育变成教育的智慧 http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180420_1114645.html
	贵州省农委成立产业大招商工作专班 http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180420_1114652.html
	一季度贵州省贷款增速列全国第三位 http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180420_1114690.html
	贵阳义务教育学生 5月起可免费托管 http://www.gzgov.gov.cn/xwdt/gzyw/201804/t20180420_1114681.html