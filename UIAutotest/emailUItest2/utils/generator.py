
from faker import Faker

fake = Faker('zh_CN')

def random_phone_number():
    """随机手机号"""
    return fake.phone_number()

def random_number(num):
    """指定位数随机数"""
    return fake.random_number(digits=num)

def random_name():
    """随机姓名"""
    return fake.name()


def random_address():
    """随机地址"""
    return fake.address()


def random_email():
    """随机email"""
    return fake.email()


def random_ipv4():
    """随机IPV4地址"""
    return fake.ipv4()


def random_str(min_chars=0, max_chars=8):
    """长度在最大值与最小值之间的随机字符串"""
    return fake.pystr(min_chars=min_chars, max_chars=max_chars)

def random_company():
    '''随机公司名'''
    return fake.company()

def random_postcode():
    '''随机邮编'''
    return fake.postcode()

def random_url():
    '''随机网站'''
    return fake.url()

def random_text():
    '''随机文本'''
    return fake.text()



if __name__ == '__main__':
    # print(random_phone_number())
    # print(random_name()+"测试")
    # print(random_address())
    # print(random_email())
    # print(random_ipv4())
    # print(random_str(min_chars=6, max_chars=8))
    # email_str = random_email()
    # print(type(email_str))
    # print(email_str.split("@"))
    # print(type(random_text()))
    for i in range(200):
        print(random_company())
