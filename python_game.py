def lol():#定义游戏方法
    #声明4个变量，分别为两个角色的生命值和攻击力
    theshy_hp=1000
    theshy_ad=300
    new_hp=1000
    new_ad=200

    while True:#当循环结构，条件为真时执行循环
        theshy_hp = theshy_hp - new_ad
        new_hp = new_hp - theshy_hp
        #生命值计算方法


        if theshy_hp <= 0:# 判定游戏胜负条件
            print('gg,new win')
            break
            #break退出循环
        elif new_hp <= 0:
            print('gg,theshy win')
            break

lol()#调用游戏方法