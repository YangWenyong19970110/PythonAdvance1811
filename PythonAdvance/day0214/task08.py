def checkaccess(fun):
    def check():
        name=input("请输入用户名")
        if name=="zzy":
            fun()
        else:
            print("未授权")
    return check
@checkaccess
def selectgoods():
    print("开始查询商品")
@checkaccess
def getmongey():
    print("您的余额为1000￥")
@checkaccess
def discounts():
    print("您的优惠券有200￥")
selectgoods()
getmongey()
discounts()