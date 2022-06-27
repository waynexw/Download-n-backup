//// C:\Users\hasee\Games\node1\index.js  环境变量 the line22，启发是通过设置环境变量，适用不同de数据库 - wayneW

const express = require('express')
const app = express()
var cors = require('cors')
const path = require('path');
var request = require('request');

const sgTest = require('./app/sendGrid.js');

const port = 3000
 
app.use(express.static(path.join(__dirname, 'public')));
app.use(cors())


app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/abc/', (req, res) => {
  res.send('Hello ABC!' + process.env.abc )
})

app.get('/email/', (req, res) => {
  var s = sgTest.sendEmail();
  res.send(s);
})

app.listen(port, () => { 
  console.log(`Example app listening at http://localhost:${port}`)
})


#怎样在一个py文件中使用另一个py文件中变量,问题如下：
# demo1 code  :
import requests
r = requests.get("http://www.aaaaa.com")
r.encoding = r.apparent_encoding
demo = r.text
demo

#beautiful1 code:
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")
soup.prettify()
print(soup.prettify)

# 在demo1中的demo变量存储了百度首页的信息，想在beauful1文件中直接使用，开始时按照其他教程将demo在demo1中定义成全局变量等等，
# 但是感觉特别麻烦，后来查阅资料，发现可以将demo1文件像第三方库一样直接引入，方式如下：
# 如果直接将demo1全部引入the “import demo1”，程序还是会报错，所以就是使用哪个变量就从原来的文件中引入即可。
from demo1 import demo
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")
soup.prettify()
print(soup.prettify)
