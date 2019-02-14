def checkuser(fun):
    def check(*args,**kwargs):
        name=input("请输入用户名")
        if name=="my":
            fun(*args,**kwargs)
        else:
            print("未授权")
    return check
@checkuser
def  showlist(n,all):
    print("这是第"+str(n)+"页，共有"+str(all)+"页")
showlist(5,100)

