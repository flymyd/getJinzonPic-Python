import urllib.request
import urllib.parse
import mkdir
import logger
from bs4 import BeautifulSoup
# 保存路径
mkpath = "c:\\jinzonpic\\"
mkdir.mkdir(mkpath)
page_head_url = "http://www.yiren30.com/se/yazhousetu/"
ua_header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Mobile Safari/537.36'}
# start = 496163 , test = 622013
for page_num in range(496167, 647100):
    # 获取该页源码
    page_url = page_head_url + str(page_num) + ".html"
    try:
        request = urllib.request.Request(page_url, headers=ua_header)
        response = urllib.request.urlopen(request)
    except:
        continue
    page_source_code = str(response.read(), encoding="utf-8")
    soup = BeautifulSoup(page_source_code, features="lxml")
    # 记录页码日志
    print("正在搜索第" + str(page_num) + "页")
    logger.logger(mkpath, "正在搜索第" + str(page_num) + "页\n")
    # 获取图包标题，创建同名文件夹
    pic_name_div = soup.find(attrs={"align": "center"})
    pic_folder_name = soup.find('font').string
    # 匹配关键字，此处可修改
    if 'jinzon' in pic_folder_name:
        create_folder_path = mkpath + pic_folder_name + "\\"
    else:
        continue
    try:
        mkdir.mkdir(create_folder_path)
    except IOError:
        continue
    # 抓取img地址并记录当前页码
    print("获取第"+str(page_num)+"页成功："+pic_folder_name)
    pic_div = soup.find(attrs={"class": "novelContent"})
    img_list = soup.find_all('img')
    logger.recorder(mkpath, "当前获取的是第"+str(page_num)+"页\n")
    # 生成图片编号并作为下载目标路径
    img_generate_num = 1
    for img_src in img_list:
        if 'pagoad.com' in img_src.get('src'):
            save_destination = mkpath + pic_folder_name + "\\" + str(img_generate_num) + ".jpg"
            logger.logger(mkpath, "第"+str(page_num)+"页匹配成功\n")
            try:
                # 按编号下载图片
                urllib.request.urlretrieve(img_src.get('src'),save_destination)
                # 记录图片路径
                logger.recorder(mkpath, "lorem" + pic_folder_name + "ipsum" + save_destination + "dolor" + "\n")
                img_generate_num = img_generate_num + 1
            except:
                continue
        else:
            break
    img_generate_num = 1