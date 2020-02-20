import time

class Solution:
    #n = input('please write your number:')
    def happynumber(self,n:int):
        unhappy = set()
        while n not in unhappy and n != 1:
            unhappy.add(n)
            n = self.GetSqureSum(n)
        print(unhappy)
        #return n == 1
    def GetSqureSum(self,n:int):
        sum1 = 0
        while n > 0:
            #获取尾数,/和int()都能用来获取整数位
            r =  n - (int(n/10)*10)
            #获取第一个数字,这个n最后带入r中，int(5/10)=0
            n = int(n/10)
            sum1 += r*r
        #print(sum1)
        return sum1

#GetSqureSum(52)

m = input('please write number:')
m = int(m)
start_time = time.time()
print('程序开始时间：{}'.format(start_time))
sol = Solution()
sol.happynumber(m)
end_time = time.time()
print('程序结束时间：{}'.format(end_time))
total_time = end_time-start_time
print('程序运行时间：{}'.format(total_time))