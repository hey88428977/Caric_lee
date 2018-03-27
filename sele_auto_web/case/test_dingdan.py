# __author__ = " Caric Lee "
import requests,unittest,urllib3,time
urllib3.disable_warnings()

class TestDingDan(unittest.TestCase):
    # 按照环境进行配置变量
    uri = "https://crm.xiaoshouyi.com"
    loginName = "88428977@qq.com"
    password = 111111
    tenantId = 337503 # 租户ID
    encryptionKey = "f2d7d588d2e4f4a485d023a6e0f05128"  # 保持登陆的key


    KeHuId = {}
    ChanPinId = {}
    OrderId = {}
    # 全局变量
    s = requests.session()
    @classmethod   # setUpClass 只执行一次， 必须加@classmethod 装饰器
    def setUpClass(cls):
        # 账号登陆
        print("------------->>>>>>>>>>: 账号登陆")
        url = cls.uri+"/global/do-login.action"
        body = {
            "loginName": cls.loginName,
            "password": cls.password,
            "pcCodeForFocusMedia": 0
        }
        a = cls.s.post(url, data=body, verify=False)
        data = a.json()
        print(data['status'])
        print(a.json())


        # 选择租户
        print("------------->>>>>>>>>>: 选择租户")
        url1 = cls.uri+"/global/login-entry.action"
        body1 = {
            "tenantId":	cls.tenantId,
            "passport.id":	"833365",   # 跟据账号进行填写，同一个账户下的多个租户，passport.id不用更改
            "encryptionKey"	: cls.encryptionKey,
            "loginName":	cls.loginName
        }
        b = cls.s.post(url1, data=body1, verify=False)
        print(b.json())

        # 新建客户（保存）,提取客户id
        print("------------->>>>>>>>>>: 新建客户save")
        start_time = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        # print(start_time)
        url2 = cls.uri + "/json/crm_account/save.action"
        body2 = {
            "belongTypeId":	5931581,
            "paramMap['accountName']":	"自动化测试_"+str(start_time),  #客户名称
            "paramMap['dimDepart']":	561202,      #全公司
            "paramMap['customItem155__c']":	"映射",   # 必填项 映射-test
            "paramMap['customItem156__c']":	"必填项"   # 必填项 test_文本
        }
        c = cls.s.post(url2, data=body2, verify=False)
        print(c.json())
        try:
            data = c.json()['data']  # 这里是字符串
            # print(data)
            import re
            id = re.findall("id=(.+?),", data)
            # print(id[0])
            TestDingDan.KeHuId = id[0]
        except Exception:
            print("data是空的，获取不到id")

        # 新建产品save，提取产品id
        print("------------->>>>>>>>>>: 新建产品save")
        start_time1 = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        url3 = cls.uri + "/json/crm_product/save.action"
        body3 = {
            "belongTypeId":	5931384,
            "type":	1,
            "paramMap['productName']":	"测试产品_"+str(start_time1),
            "paramMap['parentId']":	0,
            "paramMap['priceUnit']":1000,
            "paramMap['unit']":	"件",
            "paramMap['fileImage1']":	"[]",
            "paramMap['description']": "",
            "paramMap['enableStatus']":	1,
            "paramMap['dimDepart']":	"561202"
        }
        d = cls.s.post(url3, data=body3, verify=False)
        TestDingDan.ChanPinId = d.json()["id"]
        print(d.json())

    def test_02(self):
        u'''订单保存测试，并取出订单ID'''
        url = self.uri +"/json/crm_order/save.action"
        body = {
            "belongTypeId":	5931386,
            "belongId":	35,
            "paramMap['entityType']":	5931386,
            "paramMap['accountId']": self.KeHuId, # 客户名称
            "paramMap['dimDepart']":	561202,
            "detailEntityMap":"[{'entityId':'19','entityData':[{'belongId':'19','entityType':'5931781','productId':'%s','standardPrice':1000,'unitPrice':1000,'quantity':1,'discount':1,'comment':'','customItem129__c':'','customItem132__c':'','customItem136__c':'','customItem137__c':'','customItem138__c':'','customItem139__c':'','customItem140__c':'','customItem141__c':'','customItem119__c':''}]}]" %self.ChanPinId,
            "detailEntityId":  19,
            "productFamilyId":	103864717,
        }
        a = self.s.post(url, data=body, verify=False)
        print("------------->>>>>>>>>>: 订单保存")
        data = a.json()
        print(a.json())
        data2 = a.content
        import json
        ass = json.loads(data2)
        bss = json.loads(ass['data'])
        TestDingDan.OrderId = bss.get("id")
        # 断言
        self.assertEqual(data['status'], 0, msg="失败原因: %s != %s " % (data['status'], 0))

    def test_03(self):
        # 订单删除
        u'''用订单ID，删除新建的订单'''
        print("------------->>>>>>>>>>: 订单删除")
        url = self.uri + "/json/crm_order/delete.action"
        body = {
            "orderIds":self.OrderId
        }
        a = self.s.post(url, data=body, verify=False)
        print(a.json())
        data = a.json()
        self.assertEqual(data['status'], 0, msg="失败原因: %s != %s " % (data['status'], 0))

    @classmethod
    def tearDownClass(cls):
        # 删除产品
        print("------------->>>>>>>>>>: 删除产品 delete")
        url = cls.uri + "/json/crm_product/delete.action"
        body = {
            "productIds":cls.ChanPinId,
        }
        a = cls.s.post(url, data=body, verify=False)
        print(a.json())

        # 删除客户
        print("------------->>>>>>>>>>: 删除客户 delete")
        url1 = cls.uri + "/json/crm_account/delete.action"
        body1 = {
            "accountIds":cls.KeHuId,
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.32 Safari/537.36"
        }
        b = cls.s.post(url1, data=body1, headers=headers, verify=False)
        print(b.json())

if __name__ == "__main__":
    unittest.main()