//// C:\Users\hasee\Games\node1\index.js  环境变量在line 22，启发是通过设置环境变量来配置不同的数据库 - wayne W

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
