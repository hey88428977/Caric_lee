# coding:utf-8
import configparser

conf = configparser.ConfigParser()
# python2不需要加encoding ,python3需要加
conf.read("cfg.ini", encoding="utf-8")

sender = conf.get("email", "sender")
print(sender)

smtp_server = conf.get("email", "smtp_server")
print(smtp_server)





