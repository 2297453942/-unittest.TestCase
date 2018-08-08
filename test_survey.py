# -*- coding: UTF-8 -*-
import unittest
from survey import Diaocha
class TestDiaocha(unittest.TestCase):
    def test_diaocha(self):
        wenti="你学的第一个语言是什么："
        my=Diaocha(wenti)
        my.stor_huida('python')
        self.assertIn('python',my.huida)
        
    def test_three_diaocha(self):
        wenti="你学的第一个语言是什么："
        my=Diaocha(wenti)
        yuyans=['python','c','c++']
        for yuyan in yuyans:
            my.stor_huida(yuyan)
            
        for yuyan in yuyans:
            self.assertIn(yuyan,my.huida)

unittest.main()
