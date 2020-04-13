import requests
'''
使用说明：
1、在musescore上搜索乐谱；
2、按f12，选择元素（ctrl+B）选取乐谱的元素，结果应该是；
<img class="_3DXeP" alt="score-13237befeb84b0edb2a7afd9d7f34975 sheet music  – 1 of 10 pages"
src="https://musescore.com/static/musescore/scoredata/gen/7/2/0/5985027/fc95d8187609b92d0d7f1222ee989ad276b00888/score_0.svg?no-cache=1582782117">
3、复制上面的链接，粘贴到代码url处，注意改写形式；
4、运行程序，等待；
5、检查E盘根目录下文件，完毕。
（另外，想保存合并成pdf可搜索在线工具）
'''

#注意为改成score_{}.svg，并删去末尾无关的东西
url = 'https://musescore.com/static/musescore/scoredata/gen/7/2/0/5985027/fc95d8187609b92d0d7f1222ee989ad276b00888/score_{}.svg'
urls = []
i = 0
while True:
    if str(requests.get(url.format(i))) == '<Response [200]>':
        urls.append(url.format(i))
        i += 1
    else:
        break

for i in urls:
    imgname = 'E:/'+i.split('/')[-1]#存入E盘根目录下
    img = requests.get(i)
    with open(imgname, 'wb') as file:
        file.write(img.content)
    print(i,imgname)
