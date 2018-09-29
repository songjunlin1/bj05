import sys,os
"""
    os.sep: 动态获取/或者\，自动判断操作系统：如果你是windows那么获取出来的是\，如果是MAC获取出来的是/
"""
print(os.getcwd()+os.sep)