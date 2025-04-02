class goods:
    def __init__(self,name = "codetree",code = 50):
        self.name = name
        self.code = code
f_goods = goods()
print("product",f_goods.code,"is",f_goods.name)
n_name,n_code = input().split()
s_goods = goods
s_goods.name = n_name
s_goods.code = n_code
print("product",s_goods.code,"is",s_goods.name)