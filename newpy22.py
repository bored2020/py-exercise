heros=["蜘蛛侠","绿巨人","黑寡妇","鹰眼","灭霸","雷神"]
heros[4] = "钢铁侠"
heros
#使用切片
heros[3:]=["武松","林冲","李逵"]
heros
nums=[1,2,3,5,9,10,11,4,5,6,1,2]
nums.sort()#使用Python的封装函数
nums
#逆转顺序
nums.reverse()
nums
heros.reverse()
heros
#查询列表
nums.count(3)#查询nums中的3的个数
heros.index("绿巨人")#查找绿巨人的索引值
heros[heros.index("绿巨人")] = "神奇女侠"
heros 
#index函数的参数，start,end从什么位置开始查找
nums.index(10,1,5)
#拷贝列表
nums_copy1 = nums.copy()
nums_copy1
#使用切片复制列表
nums_copy2 = nums[:]
nums_copy2