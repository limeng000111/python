#-*-coding:UTF-8-*-
import time
from selenium import webdriver
import requests
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import ssl
import json

requests.packages.urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context
# 打开chrome
# chrome = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
# driver = webdriver.Chrome(chrome)
# driver.maximize_window()
# #隐式等待3s
# driver.implicitly_wait(3)
# driver.get('https://www.zhipin.com/')
#
# driver.find_element_by_xpath('//*[@id="wrap"]/div[4]/div/div/div[1]/form/div[2]/p/input').click()
# #输入职称
# driver.find_element_by_xpath('//*[@id="wrap"]/div[4]/div/div/div[1]/form/div[2]/p/input').send_keys('自动化测试')
# time.sleep(2)
# #点击搜索
# sousuo = driver.find_element_by_xpath('//*[@id="wrap"]/div[4]/div/div/div[1]/form/button')
# ActionChains(driver).double_click().perform()
# time.sleep(3)
# #某家公司的信息
#
# ele = driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/ul/li[1]/div/div[1]/h3/a/div[1]')
# print(ele)
# for i in range(10):
#     # i = page + 1
#     ka ='page' + '-' +str(i)
#     print('i的参数为：',i)
#     print('ka的参数为：',ka)
def get_info():
    header = {
                # "accept": "application/json, text/javascript, */*; q=0.01",
                # "accept-encoding":"gzip, deflate, br",
                # "accept-language":"zh-CN,zh;q=0.8",
                # # "cookie":"lastCity=101210100; _uab_collina=156293140563804704765454; t=ZPs8NDHwfhMeCGps; wt=ZPs8NDHwfhMeCGps; __zp_stoken__=8d21ZcvjDJppZE57oRplOh5JxPe8TylVMH55w05n42CyXlghUVlQKMEnH8d3IG8ynyf92x%2FL%2FqFIgJpPCSJ327Of7Q%3D%3D; sid=sem_pz_bdpc_dasou_title; __c=1568174633; __g=sem_pz_bdpc_dasou_title; __l=l=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&r=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDIFkY0IWPB0KZEgsDBTM9I00000Kd7ZNC00000xgW1RZ.THdBULP1doZA8QMu1x60UWYsnW0sn1n4n7tzn-qCmyqxTAT0T1dBujPBPymvnW0snjfsnymv0ZRqnHbvPH03wHTvnY7AfRDsPWD4PjbYfbcvnYn3rDNawHT0mHdL5iuVmv-b5HnznWfvnjf1Pj6hTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8Xh9GTA-8QhPEUitOTv-b5gP-UNqsX-qBuZKWgvw9TvqdgLwGIAk-0APzm1Y1njnzr0%26tpl%3Dtpl_11534_19713_15764%26l%3D1511867677%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBoss%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526xp%253Did(%252522m3224604348_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D8%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%25E5%25AE%2598%25E7%25BD%2591%26issp%3D1%26f%3D3%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3D02003390_22_hao_pg%26inputT%3D2943%26prefixsug%3Dboss%26rsp%3D0&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&friend_source=0&friend_source=0; __a=49979853.1562931405.1568110831.1568174633.90.10.4.4; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1568110842,1568174632,1568174648,1568174747; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1568174747",
                # "cookie":"user_trace_token=20190816164142-929ce5cc-47d8-4002-ba1e-404d1bb2b7d4; _ga=GA1.2.549722071.1565944907; LGUID=20190816164145-adb9680a-c001-11e9-a500-5254005c3644; _gid=GA1.2.1273153486.1568175179; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d1e864603a7b-0a2892d0648373-3a614f0b-1327104-16d1e864604611%22%2C%22%24device_id%22%3A%2216d1e864603a7b-0a2892d0648373-3a614f0b-1327104-16d1e864604611%22%7D; gate_login_token=4829ba064c98caf1f349d9e8ff3251dfb8024fa0ad27a837; LG_LOGIN_USER_ID=6cc57ae2f1b567a785ebcfc9963178eed2596018fa25cc5f; LG_HAS_LOGIN=1; _putrc=978A08F6DE8F0BD9; JSESSIONID=ABAAABAABEEAAJA5E044A86D301B763D4F47FC0418C5DF9; login=true; unick=%E6%9D%8E%E8%90%8C; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=23; privacyPolicyPopup=false; index_location_city=%E5%85%A8%E5%9B%BD; WEBTJ-ID=20190911121325-16d1e86ab8d158-0e7dd1f6e4bbd1-3a614f0b-1327104-16d1e86ab8ef2; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1565944907,1568175159,1568252525; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=sp0.baidu.com; PRE_SITE=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZNKw_0YvF-0FNkUsKGCM-I00000PwnfNC00000Y3GYWZ.THL0oUhY1x60UWYsnW0sn1n4n7tzn-qCmyqxTAT0T1dBuhRLrjKWuH0snAf4n1Ih0ZRqnHbvPH03wHTvnY7AfRDsPWD4PjbYfbcvnYn3rDNawHT0mHdL5iuVmv-b5HnzrjbYrj0vPWmhTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8UA7MULR8mvqVQvk9UhwGUhTVTA7Muiqsmzq1uy7zmv68pZwVUjqdIAdxTvqdThP-5ydxmvuxmLKYgvF9pywdgLKWmMf0mLFW5HRkPHmL%26tpl%3Dtpl_11534_19968_16032%26l%3D1514228948%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591-%252520%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E5%2525AE%25259E%2525E6%252597%2525B6%2525E6%25259B%2525B4%2525E6%252596%2525B0%21%2526xp%253Did%28%252522m3289480666_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D207%26ie%3DUTF-8%26f%3D8%26tn%3D02003390_22_hao_pg%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26oq%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rqlang%3Dcn; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt; LGSID=20190912094205-86509834-d4fe-11e9-916d-525400f775ce; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=6e6fd4e4014e72507372528651669f8d63c2d3ef4e; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1568252738; LGRID=20190912094538-053a8887-d4ff-11e9-916e-525400f775ce; SEARCH_ID=06ea1b47e8cf43498f35cf0c08fe9552",
                # # "cookie": "E6XEyfZ%2BRHMWrbmN%2BkH2paJHU53RwfmRRykFRqrrtFg%3D%3D; sid=sem_pz_bdpc_dasou_title; __c=1568031044; __g=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1568021811,1568022157,1568024390,1568031044; t=ZPs8NDHwfhMeCGps; wt=ZPs8NDHwfhMeCGps; __l=l=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&r=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDIFkY0IWPB0KZEgsDtfguI00000Kd7ZNC00000xgW1RZ.THdBULP1doZA80K85H0znj01n1bsg1czgv99UdqsusK15Hbzm19hrjDYnj0snjRzuhf0IHYkrHmdnj97P1m1fRuKfH0vnHbYrHwafWm1f163wRF7PsK95gTqFhdWpyfqn1czPjmsPjnYrausThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA-spy38mvqVQ1q1pyfqTvNVgLKlgvFbTAPxuA71ULNxIA-YUAR0mLFW5Hf1n1fs%26tpl%3Dtpl_11534_19713_15764%26l%3D1511867677%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBoss%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526xp%253Did(%252522m3224604348_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D8%26ie%3DUTF-8%26f%3D8%26tn%3D02003390_22_hao_pg%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%26oq%3Dboss%25E7%259B%25B4%25E8%2581%2598%26rqlang%3Dcn&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title%26random%3D1568031128790&friend_source=0&friend_source=0; __a=49979853.1562931405.1568011911.1568031044.72.8.4.4; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1568031144",
                # # "referer": "https://www.zhipin.com/?sid=sem_pz_bdpc_dasou_title&random=1568031128790",
                # # "token": "bh0CpeJMGtUrWHh",
                # "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
                # "x-requested-with": "XMLHttpRequest"
                'accept':'application/json, text/javascript, */*; q=0.01',
                'accept-Encoding':'gzip, deflate',
                'accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'connection':'keep-alive',
                'cookie':'_lxsdk_cuid=16d2404dcfcc8-0ad68f11377a9d-3a614f0b-144000-16d2404dcfcc8; __mta=46055195.1568267361602.1568267361602.1568267361602.1; _lxsdk_s=16d2404dcfe-3ab-b24-27f%7C%7C2; uuid_n_v=v1; iuuid=1AD737E0D52111E99647B7113623AAF1D2279642C57E412EA3770A97B719BD6E; webp=true; ci=50%2C%E6%9D%AD%E5%B7%9E; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk=1AD737E0D52111E99647B7113623AAF1D2279642C57E412EA3770A97B719BD6E',
                'host':'m.maoyan.com',
                'referer':'http://m.maoyan.com/',
                'user-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
                'x-Requested-With':'XMLHttpRequest'
            }
    # formdata={
    #     'first': 'true',
    #     'pn': 1,
    #     'kd': '测试工程师'
    # }
    # proxy = '47.107.136.195:3128'
    # proxies = {
    #     'http':'http://' + proxy,
    #     'https':'https://' + proxy,
    # }
    req = requests.get('http://m.maoyan.com/ajax/movieOnInfoList?token=',headers=header, verify=False)
    # result = req.text
    # res = BeautifulSoup(req.text,'html.parser')
    # jd = json.loads(res.text)
    req.encoding='utf-8'
    page_contents = req.json()['movieList']
    print(page_contents)
    print('--------001')
    data_list=[]
    page_content001=[]
    for page_content in page_contents:
        page_content001.append(page_content)
        print(page_content001)
        # time.sleep(2)
        print('--------002')

        file = page_content['nm']
        star = page_content['wish']
        mingxing = page_content['star']
        time = page_content['rt']
        content = [file,star,mingxing,time]
        data_list.append(content)
        print(data_list)

        return(data_list)

def write(data_list):
    with open('file.csv','a+',encoding='utf-8',newline='') as f:
        f.write('电影,点赞数,明星,时间\n')
        for d in data_list:
            print('-----------003')
            print(d)
            print('-----------004')
            # row = '{},{},{},{},{}'.format(d[0], d[1], d[2], d[3], d[4])
            row = '{},{},{},{}'.format(d[0],d[1],d[2],d[3])
            f.write(row)
            f.write('\n')
        time.sleep(3)
if __name__ == '__main__':
    data_list = get_info()
    write(data_list)
    time.sleep(3)

