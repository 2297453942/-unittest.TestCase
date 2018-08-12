# -*- coding: UTF-8 -*-
import random
quzhi=random.randint(1,20)
print('猜1到20,只有6次机会哦')
for guess in range(1,7):
    print('猜一猜')
    guess = int(input())
    
    if guess < quzhi :
        print('数字小了')
    elif guess > quzhi :
        print('数字大了')
    else :
        break
        
if guess == quzhi :
    print('恭喜你猜对了,是'+str(quzhi))
else:
    print('我的正确数字是:'+str(quzhi))
