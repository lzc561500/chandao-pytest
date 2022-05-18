# import pytest
# class TestAAA:
#     name_list=["zhangsan","wangwu"]
#     @pytest.mark.parametrize("name",name_list)
#     def test_lianxi(self,name):
#         print(name)


# print("{0:*>10}".format("开始执行"))
# print("{0:*<10}".format("开始执行"))
# print("{0:*^20}".format("开始执行"))
# # 保留3位小数
# print("{0:.3f}".format(124567.6678899090))
# # 转换成二进制
# print("{0:b}".format(13235))
# # 转换成8进制
# print("{0:o}".format(13235))
# # 转换成16进制
# print("{0:x}".format(13235))
# # 转换成千分之格式
# print("{0:,}".format(74179.50))
# userName = input("请输入您的姓名：")
# age = input("请输入您的年龄:")
# res = f'我的姓名为{userName},我的年龄为{age}'
# print(res)
#
# m = 10
# n = 20
# m,n = n,m
# print(m,n)
# m = {"name": "李四"}
# print(id(m))
# m["name"]="王五"
# print(id(m))
# import copy
# list1=["nihao","111",[111,222]]
# list2 = copy.deepcopy(list1)
# list1[2][0]="9999"
# print(list1)
# print(list2)
# a = 10
# print(bin(a))
# print(int("0b1010",2))


# msg = "age:18:name:lisi:18"
# print(msg.rindex("18"))#返回的是“18"起始元素的索引

# 将L中的元素取出依次放到new_l中使用list中内置方法extend
# l = [1,2,3]
# new_l = [111,"222","444"]
# new_l.extend(l)
# print(new_l.remove(111))
# print(new_l.pop(0))
# print(new_l)
# new_l = [111,"222","444"]
# new_l.reverse()
# print(new_l)
# def myFunc(e):
#     return len(e)
#
#
# new_l = [111, "a", 3333.33, "c", "m"]
# # new_l.sort(key=myFunc,reverse=True)
# # print(new_l)
# l = []
# for i in new_l:
#     l.append(i.__hash__())
# l.sort()
# print(l)

# info =[
#     ["age","18"],
#     ("name","lisi"),
#     ["sex","男"]
# ]
# print(dict(info))

# d = {"k1": 222}
# d["k1"] = "nihao"  # 当key值存在的时候此操作为修改
# print(d)
# d["k2"] = "zhongguo"  # 当 key值不存在的时候此操作为添加
# print(d)

# d = {'张三': '18', '王五': '20', '李四': '45'}
# d1 = {"赵云":"200","李四":"70"}
# d.update(d1)
# print(d)
# 如果字典中的key存在则不添加，返回key对应的值
# info = {"name":"张三"}
# res = info.setdefault("name","张三")
# print(res)
# name_1 = {"张三","李四","王五","赵云"}
# name_2 = {"大乔","小乔","马超","赵云","李四"}
# print(name_1.intersection(name_2))
# print(name_1.union(name_2))
# print(name_1.difference(name_2))
# print(name_1.symmetric_difference(name_2))
# print(name_1.issuperset(name_2))
# print(name_2.issubset(name_1))
# #对称差集：就是name_1-name_2和name_2-name_1取并集：
# #简单的些就是：
# # print(name_1 ^ name_2)
# 集合删除元素之discard
# s = {1,2,3,4}
# # s.discard(3)# 如果删除的元素不在集合内返回原集合什么都不做
# s.update({1,24,35,3,4})
# # s.difference_update({1,6,7})# 等同于s=s.difference({1,6,7})
# # s.isdisjoint({6,7})# 两个集合完全独立没有共同部分则返回True
# print(s)

# with open("./aaa.txt", "rt", encoding="utf-8") as f:
#     count = 1
#     lis_f = list(f)
#     f_len = len(lis_f)
#     for line in lis_f:
#         res = ""
#         userName, password = line.strip().split(":")
#         print(userName, password)
#         count1 = 0
#         for i in range(0, 3):
#             input_userName = input("请输入用户名：").strip()
#             input_password = input("请输入密码：").strip()
#             if input_userName == userName and input_password == password:
#                 res = "登录成功"
#                 print(res)
#                 break
#             else:
#
#                 if 3 - (count1 + 1) >=1:
#                     print("用户名密码错误请重新输入,您还有{}次机会！！！".format(3 - (count1 + 1)))
#                     count1 += 1
#         else:
#             if count < f_len:
#                 print("请更换用户再输入！！！")
#                 count += 1
#         if "登录成功" in res:
#             break
#
#     else:
#         print("您更换用户的次数已达到上限")
#

# copy所有文件（包括文件、图片、视频）
# source = input("输入原路径：").strip()
# copy_source = input("请输入目标路径：").strip()
# with open(r"{}".format(source), mode="rb") as f1, \
#         open("{}".format(copy_source), mode="wb") as f2:
#     res = f1.read()
#     f2.write(res)

# 使用while循环读图片视频
# with open(r"test.jpg","rb") as f :
#     while True:
#         res = f.read()
#         if len(res) == 0:
#             break
#         print(res)

# 第一种方式：写一行读一行
# with open(r"sanwen.txt",mode="rb") as f1,\
#     open(r"log.txt",mode="ab+") as f2:
#      while True:
#          res = f1.readline()
#          if len(res) == 0:
#              break
#          f2.write(res)
#          f2.seek(-len(res), 2)
#          print("光标所在的位置：{}".format(f2.tell()))
#          newest_text = f2.read()
#          print(newest_text.decode("utf-8"))

# 第二种：写一行读一行
import time
# 先启动本文件进行监测，然后在启动追加内容.py文件
# 注意：在写的模式不影响指针位置，只有读的模式才会影响指正位置
# with open(r"log.txt",mode="rb") as f:
#     # 模式2：从末尾向右移动0个字节也就是末尾
#     f.seek(0,2)
#     while True:
#         res = f.read()
#         if len(res) == 0:
#             time.sleep(0.3)
#         else:
#             print(res.decode("utf-8"))

# 文件修改的两种方式：修改文件的原理就是将修改的内容去覆盖老的内容
# 方式一：文件编辑器用的是这种方式，这个浪费的是内存空间
with open(r"aaa.txt",mode="rt",encoding='utf-8') as f1:
    data = f1.read()
    new_data = data.replace("zhangsan","egon")
with open(r"aaa.txt",mode='wt',encoding='utf-8') as f2:
    f2.write(new_data)

# 方式二：
import os
with open(r"aaa.txt",mode='rt',encoding='utf-8') as f3,\
    open(r"bbbb.txt",mode='wt',encoding='utf-8')as f4:
    for line in f3:
        f4.write(line.replace("egon","zhangsan"))

os.remove("aaa.txt")
os.rename("bbbb.txt","aaa.txt")




