# -*- coding : utf-8 -*-
import os,platform
ini="""[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=pypi.tuna.tsinghua.edu.cn
"""
os_version=platform.platform()
if 'Windows' in os_version:
    os_flag=False
    file_name='pip.ini'
else:
    os_flag=True
    file_name='pip.conf'
if os_flag==True:
    pippath=os.environ["HOME"]+os.sep+".pip"+os.sep
    #os.environ["HOME"]是linux下取用户家目录，os.sep为路径分隔符
else:
    pippath=os.environ["USERPROFILE"]+os.sep+"pip"+os.sep
    #os.environ["USERPROFILE"]windows下取用户家目录
if not os.path.exists(pippath):
    os.mkdir(pippath)
with open(pippath+file_name,"w+") as f:
    f.write(ini)
