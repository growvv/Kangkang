'use strict';

const nodemailer = require('nodemailer');

let transporter = nodemailer.createTransport({
  // host: 'smtp.ethereal.email',
  service: 'qq', // 使用了内置传输发送邮件 查看支持列表：https://nodemailer.com/smtp/well-known/
  port: 465, // SMTP 端口
  secureConnection: true, // 使用了 SSL
  auth: {
    user: 'growvv@qq.com',
    // 这里密码不是qq密码，是你设置的smtp授权码，去qq邮箱后台开通、查看
    pass: 'nveatabzjssudbfc',
  }
});

let mailOptions = {
  from: '"Rogn" <growvv@qq.com>', // sender address
  to: '1009526672@qq.com', // list of receivers
subject: '『康康』通知', // Subject line
  // 发送text或者html格式
  // text: 'Hello world?', // plain text body
  html: '<h2><font color="red">溢出警告!!</font></h2><p>垃圾桶已满，请及时清理</p><ul>  <li>垃圾体积：86%</li><li>位置： 西校门左侧100米</li></ul>' // html body
};

// send mail with defined transport object
transporter.sendMail(mailOptions, (error, info) => {
  if (error) {
    return console.log(error);
  }
  // console.log('Message sent: %s', info.messageId);
  console.log(info)
});
