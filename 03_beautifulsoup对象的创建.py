from bs4 import BeautifulSoup
import requests

# for example
# soup1.find('a')
# soup1.find(id='link1')
# soup1.find(attrs={'id':'link1'})

html='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>JD5</title>
    <link rel="stylesheet" href="reset.css">
    <link rel="stylesheet" href="fa/css/all.css">
    
</head>
<body>
<div class="top-bar-wrapper">
    <div class="top-bar">
        <div class="location">
            <div class="current-city">
                <i class="fa fa-map-marker"></i>
                <a href="javascript:;">
                    北京
                </a>
            </div>

            <div class="city-list">

            </div>
        </div>

        <ul class="shortcut">
            <li>
                <a href="javascript:;">你好，请登录</a>
                <a href="javascript:;" style="color: #f10215;">免费注册</a>
            </li>

            <li class="line"></li>
            <li><a href="javascript:;">我的订单</a></li>

            <li class="line"></li>
            <li>
                <a href="javascript:;">我的京东</a>
                <i class="fa fa-angle-down"></i>
            </li>


            <li class="line"></li>
            <li>
                <a href="javascript:;">京东会员</a>
                <i class="fa fa-angle-down"></i>
            </li>

            <li class="line"></li>
            <li>
                <a href="javascript:;" style="color: #f10215;">企业采购</a>
                <i class="fa fa-angle-down"></i>
            </li>

            <li class="line"></li>
            <li>
                <span>客户服务</span>
                <i class="fa fa-angle-down"></i>
            </li>

            <li class="line"></li>
            <li>
                <span>网站导航</span>
                <i class="fa fa-angle-down"></i>
            </li>

            <li class="line"></li>
            <li>
                <span>手机京东</span>
            </li>

        </ul>
    </div>
</div>
</body>
</html>
'''

# soup = BeautifulSoup(requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia").content.decode(),'lxml')
soup1=BeautifulSoup(html,'lxml')
# print(soup1.find_all('a'))
# title = soup.find_all('script')
# print(title)

# for example
print(soup1.find('a').attrs)
# soup1.find(id='link1')
# soup1.find(attrs={'id':'link1'})