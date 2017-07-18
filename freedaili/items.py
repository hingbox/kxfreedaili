# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class FreedailiItem(Item):
   content =Field()
   ip = Field()#ip
   port = Field()#端口
   type = Field()#类型
   rspspeed = Field()#响应速度
   lastvalidatetime = Field()#最后验证时间
   location = Field()#位置
   anondeg = Field()#匿名度
   def_flag = Field()#逻辑删除标记（0：显示；1：隐藏）
   remarks = Field()#备注信息
