from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = 'xxxxxxxxx@qq.com'  # 发送者的邮箱地址
    receivers = ['xxxxxxxxxx@qq.com']  # 接收者的邮箱地址
    message = MIMEText(open('data.txt').read(), _subtype='plain', _charset='utf-8')
    message['From'] = Header('Your Old Friend', 'utf-8')  # 邮件的发送者
    message['To'] = Header('Darling Jay', 'utf-8')   # 邮件的接收者
    message['Subject'] = Header('To darling Jay', 'utf-8') # 邮件的标题
    smtper = SMTP('smtp.qq.com')
    # 请自行修改下面的登录口令

    smtper.login(sender, 'xxxxxxxxxxxxxxxx')  # QQ邮箱smtp的授权码
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()