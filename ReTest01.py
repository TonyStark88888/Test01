# -*- coding:utf-8 -*-
# @Time : 2021/12/13 20:50
# @Author : Tony Stark
# @File : ReTest01.py
# @Software : PyCharm

# 正则表达式，其实就是对字符串的规定
'''
操作符                         说明                          实例
.                       表示任何单个字符
[]                  字符集，对单个字符给出取值范围     [abc]表示a或b或c，[a-z]表示a到z单子字符
[^ ]               非字符集，对单个字符给出排除范围     [^abc]表示非a或b或c的单个字符
*                   前一个字符0次或无限次扩展           abc*表示ab、abc、abcc、abccc...等等
+                   前一个字符1次或无限次扩展           abc+表示abc、abcc、abccc...等等（不表示ab）
?                   前一个字符0次或1次扩展                abc？表示ab、abc
|                       左右表达式任意一个             abc|def表示abc、def

{m}                     扩展前一个字符m次               ab{2}c表示abbc
{m,n}                 扩展前一个字符m~n次（含n）       ab{1，2}表示abc，abbc
^                       匹配字符串开头             ^abc表示abc且在一个字符串的开头
$                       匹配字符串结尾             abc$表示abc且在一个字符串的结尾
( )                 分组标记，内部只能使用|操作符    (abc)表示abc,(abc|def)表示abc、def，与|不同的是能分好几组
\d                      digit数字，等价于[0-9]
\w                  word单词字符，等价于[A-Za-z0-9_]

                        Re库主要功能函数
函数                          说明
re.search()     在一个字符串中搜索匹配正则表达式是第一个位置，返回match对象
re.match()      从一个字符串的开始位置起匹配正则表达式，返回match对象
re.findall()    搜索字符串，以列表类型返回全部能匹配的字符串
re.sub()        在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
re.split()      将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
re.finditer()   搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象

                        Re的配置设置，修饰符
修饰符                         描述
re.l                   使匹配对大小写不敏感
re.L                  做本地化识别（local-aware）匹配
re.M                    多行匹配，影响^和$
re.S                  使.匹配包括换行在内的所有字符
re.U                  根据Unicode字符集解析字符。此标志影响\w,\W,\b,\B
re.X                  该标志通过给与更灵活的格式便于正则表达式编写得易于理解

'''
#正则表达式：字符串模式（判断字符串是否符合一定得标准）
import re
#创建模式对象
# pat = re.compile("AA")#此处”AA“为正则表达式，用以验证其他表达式
# m = pat.search("AACBAA")    #search字符串被校验的内容，进行匹配查找
# print(m)    #<re.Match object; span=(3, 5), match='AA'>【左闭右开的区间3-5，只找第一个】

#没有模式对象
# m = re.search("asd","AAAasddd")#前面是规则(正则表达式)，后面是被校验的对象-><re.Match object; span=(3, 6), match='asd'>
# print(m)

# m=re.findall("a","ASDaDFGJNAa")#前面是规则（正则表达式），后面是被校验的对象->['a', 'a']
# m = re.findall("[A-Z]","aGHDacdOKJasd")#单个大写字母->['G', 'H', 'D', 'O', 'K', 'J']
# m = re.findall("[A-Z]+","aGHDacdOKJasd")#多个大写字母连着（大写字母段）->['GHD', 'OKJ']

#sub
# m=re.sub("a","A","abcddeSAde")  #第一个字符串是被替换对象，第二个字符串是被用来替换的对象，在第三个字符串中查找->AbcddeSAde

#建议在正则表达式中，被比较字符前面加上r，不用担心转义字符的问题 a="\aabd-\'"--->a=r"\aabd-\'"

print(m)
