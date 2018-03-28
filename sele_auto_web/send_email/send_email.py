# -*- coding: utf-8 -*-
import smtplib,os.path,mimetypes,time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
def sendmail():
    From = "lixy@xiaoshouyi.com"
    To = "18633605169@163.com"    #这里添加收件人
    result_dir ='D:\\github\\sele_auto_web\\report\\' #测试报告html生成路径
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn)
    if not os.path.isdir(result_dir + "\\" + fn)
    else 0)
    print('最新测试生成的报告:'+ lists[-1])
    # 找到最新生成的文件
    file_new = os.path.join(result_dir, lists[-1])
    print(file_new)
    server = smtplib.SMTP("smtp.exmail.qq.com")  #smtp服务器    例如：smtp.163.com
    server.login("lixy@xiaoshouyi.com", "Hey88428977")  # 仅smtp服务器需要验证时

    # 构造MIMEMultipart对象做为根容器
    main_msg = MIMEMultipart()
    # 构造MIMEText对象做为邮件显示内容并附加到根容器
    # 正文
    text_msg = MIMEText(u"这是今天的jmeter接口自动化测试报告，请查收", _charset="utf-8")
    main_msg.attach(text_msg)
    # 构造MIMEBase对象做为文件附件内容并附加到根容器
    ctype, encoding = mimetypes.guess_type(file_new)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    file_msg = MIMEImage(open(file_new, 'rb').read(), subtype)
    print(ctype, encoding)
    ## 设置附件头
    basename = os.path.basename(file_new)
    file_msg.add_header('Content-Disposition','attachment', filename=basename)  # 修改邮件头
    main_msg.attach(file_msg)
    # 设置根容器属性
    main_msg['From']=From
    main_msg['Subject']="jmeter接口自动化测试报告"
    main_msg['Date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    # 得到格式化后的完整文本
    fullText = main_msg.as_string()
    # 用smtp发送邮件
    try:
        server.sendmail(From, To, fullText)
        print('测试报告发送成功')
    finally:
        server.quit()
if __name__ == '__main__':
    #执行发邮件
    sendmail()
