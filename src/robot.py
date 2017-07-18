#!/usr/bin/env python
#coding:utf-8

dict = {
        'Hello'                        : 'Hello',
        'Nice to meet you'             : 'Nice to meet you',
        'Which fruit do you like best' : 'I like apple very much',
        'How old are you'              : '20 years old',
        'You are handsome'             : 'Thank you'
        }
# t--train 训练机器人对话；c--chat 同机器人聊天；l--leave 让机器人离开
flag = 'c'      #让机器人默认是聊天状态
work = True     #让机器人开默认是工作的

print 'Hi, my name is Python'
print 'Do you want to chat with me?'
while flag == 'c' or 't':
    flag = raw_input("你可以选择跟我聊天(c)还是训练我对话(t)，或者让我离开(l)? (c/t/l)")
    # 训练状态时
    if flag == "t":
        question = raw_input("请输入问题(key)：")   #获取输入作为key
        answer = raw_input("请输入回答(value): ")   #获取输入作为value
        dict[str(question)] = str(answer)         #像字典里存入键值对
        print u"训练成果"
        print u"现在我已经会%d个问题了！" % len(dict)
        continue                                   #跳出本次循环
    # 聊天状态时
    elif flag == 'c':
        if len(dict) == 0:
            print u"现在还不会任何问题，请先训练我！"
            continue;
        #获取输入作为要查找的key
        char_word = raw_input("谢谢你跟我聊天，你想对我说点什么？： ")    
        #遍历整个字典
        for key in sorted(dict.keys()):
            if str(char_word) == key:           #如果有相同的key
                work = True                     #设置机器人工作开启
                print dict[key]                 #打印出对应的key
                break                           #结束遍历
            else:
                work = False                    #无相同的key，机器人不工作
        #如果机器人不工作状态，打印提示信息，并重置工作状态为True
        if work == False:
            print u"抱歉，这句话我还不会回答"    
            work = True
    #执行离开操作时，打印提示信息
    elif flag == 'l':
        print u"好的，下次再见"
        break
    #其它情况，不输入或者输入非法信息时    
    else:
        print u"请输入提示的指令"
        continue                



