# -*- coding: utf-8 -*-
import re
import json
from pathlib import Path
import os
from pyecharts import options as opts
from pyecharts.options.global_options import InitOpts, TitleOpts
from pyecharts.charts import Line,Grid
import time 

rawpathdict = {
    'a' : {
        '1': './虚拟主播区专楼/虚拟主播【Asoul】/',
    },
    'b' : {
        '1': './虚拟主播区专楼/虚拟主播【B综】/',
    },
    'h' : {
       '1' : './虚拟主播区专楼/虚拟主播【H综】/',
    },
    'm' : {
        '1': './虚拟主播区专楼/虚拟主播【Mea楼】/',
    },
    'v' : {
        '1': './虚拟主播区专楼/虚拟主播【V综】/',
    },
}
# apaths = ['./S1PlainTextGeneral/虚拟主播区专楼/虚拟主播【Asoul】/','./S1PlainTextBackup/虚拟主播区专楼/2019599[【A18】A-SOUL讨论楼（8月8日，20：00，乃琳生日会）]/']

# bpaths = ['./S1PlainTextGeneral/虚拟主播区专楼/虚拟主播【B综】/','./S1PlainTextBackup/虚拟主播区专楼/2017705[【B32】VUP综合讨论楼]/']

# cpaths = ['./S1PlainTextBackup/虚拟主播区专楼/1966145[【C1】巧克拉拉／哔哩哔哩vup综合讨论楼]/']

# hpaths = ['./S1PlainTextGeneral/虚拟主播区专楼/虚拟主播【H综】/','./S1PlainTextBackup/虚拟主播区专楼/2018062-01[再放送スレ].md']

# mpaths = ['./S1PlainTextGeneral/虚拟主播区专楼/虚拟主播【Mea楼】/','./S1PlainTextBackup/虚拟主播区专楼/2018830-01[【M14】神楽Mea(KaguraMea)讨论楼].md']

# vpaths = ['./S1PlainTextGeneral/虚拟主播区专楼/虚拟主播【V综】/','./S1PlainTextBackup/虚拟主播区专楼/1972669[【V14】虚拟YouTuber(vtuber)综合讨论楼]/']

def getallfile(dirpath,allpath=[]):
    for pa in Path(dirpath).iterdir():
        if Path(pa).is_dir():
            print(pa)
            getallfile(pa)
        else:
            allpath.append(pa) 
    return allpath

# def getkwfile(flist, keyword):
#     res = []
#     for ff in flist:
#         if keyword in ff.split('\\')[-1]:   # 切分出文件名来再判断，可以缩短判断时间
#             res.append(ff)
#     return res

if __name__ == "__main__":
    pathdict = {}
    for key in rawpathdict.keys():
        count = 0
        for i in rawpathdict[key].keys():
            pathdict[key] = {}
            if i == 'A':
                pathdict[key][str(count)] = rawpathdict[key][i]
                count = count + 1
            else:
                temppaths =  getallfile(rawpathdict[key][i])
                for k in temppaths :
                    pathdict[key][str(count)] = k
                    count = count + 1
                    print(k)
        # for filepath in apath:
        #     with open (filepath, 'r',encoding='UTF-8') as f:
        #         lines = f.readlines() 
        #         a = ''
        #         for line in lines:
        #             a += line.strip()
        #             # a += line

        #     b = a.split("*****")

    #         res = []
    #         for post in b:
    #             post1 = post
    #             post2 = post
    #             data={}
    #             data['id'] = ''.join(re.findall(r"^[\*]{0,2}####\s\s([^#]+)#", post))
    #             # data['level'] = str(filepath)+''.join(re.findall(r"#####\s(\d+)#", post1))
    #             data['time'] = ''.join(re.findall(r"^.*?发表于\s(\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2})", post2))
    #             if(data['id']):
    #                 res.append(data)
    #         spath = ''.join(re.findall(r"\d{7}-\d{2}", str(filepath)))
    #         with open(rawdatapath+spath+'.json',"w",encoding='utf-8') as f:
    #                     f.write(json.dumps(res,indent=2,ensure_ascii=False))
    #         print(filepath)

    # allpath = getallfile(rawdatapath)                              
    # rawdata = []
    # with open('/home/riko/S1AllStars/V区专楼发言数量变迁/V-RawData.json', "w", encoding="utf-8") as f0:
    #     for filepath in allpath:
    #         print(filepath)
    #         with open(filepath, "r", encoding="utf-8") as f1:
    #             thdata = json.load(f1)
    #             rawdata = rawdata + thdata
    #             f1.close()
    #     f0.write(json.dumps(rawdata,indent=2,ensure_ascii=False))


    # with open('/home/riko/S1AllStars/V区专楼发言数量变迁/M-RawData.json', "r", encoding="utf-8") as f:
    #     rawdata = json.load(f)
    # data = {}
    # for post in rawdata:
    #     postintime = int(time.mktime(time.strptime(post['time'],"%Y-%m-%d %H:%M")))
    #     if postintime%86400 :
    #         postintime = postintime - postintime%86400
    #     posttime = time.strftime("%Y-%m-%d", time.localtime(postintime))
    #     if posttime not in data.keys():
    #         data[posttime] = {}
    #         data[posttime]['num'] = 1
    #         data[posttime]['ids'] = {}
    #     else:
    #         data[posttime]['num'] = data[posttime]['num'] +1
    #         data[posttime]['ids'][post['id']] = 1
    # with open('/home/riko/S1AllStars/V区专楼发言数量变迁/M-DataDict.json', "w", encoding="utf-8") as f:
    #     f.write(json.dumps(data,indent=2,ensure_ascii=False))


    # with open('/home/riko/S1AllStars/V区专楼发言数量变迁/H-DataDict.json', "r", encoding="utf-8") as f:
    #     datadict = json.load(f)
    # data = []
    # stime = []
    # reply = []
    # replyer = []
    # for key in datadict.keys():
    #     c = key
    #     d = datadict[key]['num']
    #     e = len(datadict[key]['ids'].keys())
    #     stime.append(c)
    #     reply.append(d)
    #     replyer.append(e)
    # data.append(stime)
    # data.append(reply)
    # data.append(replyer)
    # with open('/home/riko/S1AllStars/V区专楼发言数量变迁/H-Data.json', "w", encoding="utf-8") as f:
    #     f.write(json.dumps(data,indent=2,ensure_ascii=False))