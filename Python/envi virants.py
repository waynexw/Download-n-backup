# Python adding environmental virables to programs 添加环境变量
import sys
sys.path
系统环境是一个list，可以将自己需要的库添加进入，例如mysql库，hive库等等。有三种方式添加，均验证通过：
 
 
# 1 临时添加，在一个shell窗口中
import sys
sys.path
sys.path.append(path) 
但退出该shell窗口，即失效
 
 
# 2 使用pth文件永久添加 
 
使用pth文件，在 site-packages 文件中创建 .pth文件，将模块的路径写进去，一行一个路径，以下是一个示例，pth文件也可以使用注释：
# .pth file for the  my project(这行是注释)
E:\DjangoWord
E:\DjangoWord\mysite
E:\DjangoWord\mysite\polls
这个不失为一个好的方法，但存在管理上的问题，而且不能在不同的python版本中共享
 
 
# 3 使用PYTHONPATH环境变量
 
使用PYTHONPATH环境变量，在这个环境变量中输入相关的路径，不同的路径之间用逗号（英文的！)分开，如果PYTHONPATH 变量还不存在，可以创建它！
 
路径会自动加入到sys.path中，而且可以在不同的python版本中共享，应该是一样较为方便的方法

# example of envi virants in swagger.
import os
import uuid
import json  
import pymysql  # need to install pymysql first -wayne W
import mysql.connector 
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint

from validate_email import validate_email
REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API

# initializaed local database via creation a new database
# DB_NAME = "abc"
# you can set dbname1=1,2,3 or book, car ..., but you should set it pre-start the program.
DB_NAME = str(os.getenv('dbname1'))
if DB_NAME == "None":
    DB_NAME = "mydb"

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="www",  # please adjust the user name as same as the local MySQL's user name  -wayneW
  password="5566"  # change the password as you defined in your MySQL database  -wayneW
)

mycursor = mydb.cursor()
# 可以加一条判断 如果数据库已经存在 则跳过此步骤
# if mycursor then jump out.
if DB_NAME = "mydb":
 mycursor.execute(write 'the database existed.')
mycursor.execute("CREATE DATABASE " + DB_NAME)  # mydb is created to record the bookinfo. -wayneW

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="www",   # please adjust the user name as same as local database user name  -wayneW
  password="5566",  # change the password as you defined in your local database  -wayneW
  database=DB_NAME  
)
