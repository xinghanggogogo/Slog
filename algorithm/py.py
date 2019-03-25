# coding: utf-8

# 单链表逆置:
# 定义Node结构, 输出方法, 然后1, 2, 3, 4
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse(lis):
    head = lis
    tmp = head.next
    head.next = None
    while tmp:
        last = tmp.next
        tmp.next = head
        head = tmp
        tmp = last
    return head

lis = Node(1, Node(2, Node(3, Node(4, Node(5)))))
lis = reverse(lis)

root = lis
while root:
    print root.value
    root = root.next

# 一个最简单的递归, 斐波那契数列
def digui(n):
    if n == 0 or n == 1:
        return n
    return n + digui(n-1)

n = 10
sum = digui(n)
print sum

# 快速排序
# 基本版本的快速排序
# 原地, if 而不是while, 是否稳定取决于partition函数的第二层while的等号写不
def quickSort(seq, low, high):
    if low < high:
        pivot = partition(seq, low, high)
        quickSort(seq, low, pivot-1)
        quickSort(seq, pivot+1, high)

def partition(seq, low, high):
    key = seq[low]
    while low < high:
        while low < high and seq[high] >= key:
            high -= 1
        seq[low] = seq[high]
        while low < high and seq[low] =< key:
            low += 1
        seq[high] = seq[low]
    seq[low] = key
    return low

seq = [9, 8, 7, 6, 5, 4, 3, 2, 1]
quickSort(seq, 0, len(seq)-1)
print seq
# 另一个版本的快速排序
# 不是原地, 注意递归出口和是否稳定
def quickSort(seq):
    if len(seq) <= 1:
        return seq
    key = seq[0]
    left = quickSort([i for i in seq[1:] if i < key])
    right = quickSort([i for i in seq[1:] if i >= key])
    return left + [key] + right

seq = [9, 8, 7, 6, 5, 4, 3, 2, 1]
seq = quickSort(seq)
print seq

# bytedance面试
# 用两个栈来实现一个队列
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def inQueue(self, key):
        self.stack1.append(key)

    def outQueue(self):
        for i in range(len(self.stack1)):
           self.stack2.append(self.stack1.pop())
        res = self.stack2.pop()
        for i in range(len(self.stack2)):
           self.stack1.append(self.stack2.pop())

    def showMe(self):
        print self.stack1

q = Queue()
q.inQueue(1)
q.inQueue(2)
q.inQueue(3)
q.inQueue(4)
q.showMe()
q.outQueue()
q.showMe()
q.inQueue(5)
q.showMe()

# python实现约瑟夫环
# 定义Node数据结构, 生成单向循环列表, k-2!
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def josefu(n, k):
    root = Node(1)
    tmp = root
    for i in range(2, n+1):
        tmp.next = Node(i)
        tmp = tmp.next
    tmp.next = root

    tmp = root
    while True:
        for i in range(k-2):
            tmp = tmp.next
        print tmp.next.value
        tmp.next = tmp.next.next
        tmp = tmp.next
        print tmp.value
        if tmp.next == tmp:
            print tmp.value
            break

n = 10
k = 4
josefu(n, k)

# bytedance面试
# python递归实现全排列
def func(seq):
    if len(seq) < 1:
        return [seq]

    res = []
    for i in range(len(seq)):
        key = seq[i]
        tmp_seq = seq[:i] + seq[i+1:]
        tmp_res = func(tmp_seq)
        for item in tmp_res:
            res.append([key]+item)
    return res

seq = [1, 2, 3]
res = func(seq)
for i in res:
    print i

# 输出一个list中, 加和为m的所有的可能
def func(seq, m, path):
    for i in seq:
        m -= i
        path.append(i)
        if m == 0:
            print path
        elif m > 0:
            func(seq[i+1:], m, path)
        m += i
        path.pop()

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m = 10
path = []
func(seq, m, path)

# 关于插入排序的两种写法
# 注意都是for j in range(i-1, -1, -1)
# 基于交换的插入排序
def insertSort(seq):
    for i in range(1, len(seq)):
        for j in range(i-1, -1, -1):
            if seq[j] > seq[j+1]:
                seq[j+1], seq[j] = seq[j], seq[j+1]

# 基于比较的插入排序
def insertSort(seq):
    for i in range(1, len(seq)):
        tmp = seq[i]
        for j in range(i-1, -1, -1):
            if seq[j] > tmp:
                seq[j], seq[j+1] = seq[j+1], seq[j]
            else:
                break
        seq[j] = tmp

seq = [8, 9, 7, 6, 5, 4, 3, 2, 1]
insertSort(seq)
print seq

# 选择排序
def selectSort(seq):
    for i in range(0, len(seq)):
        min = i
        for j in range(i+1, len(seq)):
            if seq[j] < seq[min]:
                min = j
        seq[i], seq[min] = seq[min], seq[i]

seq = [7, 8, 9, 6, 5, 4, 3, 2, 1, 0]
selectSort(seq)
print seq

# 手写冒泡排序
# n-1趟, for j in range(len(seq)-1, i, -1)
def bubbleSort(seq):
    for i in range(0, len(seq)-1):
        flag = False
        for j in range(len(seq)-1, i, -1):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]
                flag = True
        if not flag:
            return

seq = [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
bubbleSort(seq)
print seq

# 关于归并排序
# 写的很差
# return, merge, left、right
def mergeSort(seq):
    if len(seq) <= 1:
        return seq

    mid = len(seq) / 2
    left = mergeSort(seq[:mid])
    right = mergeSort(seq[mid:])
    res = merge(left, right)
    return res

def merge(left, right):
    i, j, res = 0, 0, []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res = res + left[i:] if i < len(left) else res + right[j:]
    return res


seq = [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
seq = mergeSort(seq)
print seq

# 堆排序:
def fixDown(l, k, n):
    while k * 2 <= n:
        j = k * 2
        if j < n and l[j] < l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
        if l[k] < l[j]:
            l[k], l[j] = l[j], l[k]
            k = j
        else:
            break

def heapSort(l):
    n = len(l)-1
    for i in range(n//2, 0, -1):
        fixDown(l, i, n)
    while n > 1:
        l[1], l[n] = l[n], l[1]
        n -= 1
        fixDown(l, 1, n)

if __name__  == '__main__':
    l = [2, 3, -6, 1, 5, 4, 0]
    l = [-1] + l
    heapSort(l)
    print l[1:]

# 堆排序拓展:
# 100万个数字里求最大的五个数:
# 这是最优解法
import random

def fixDown(l, k, n):
    while k*2 <= n:
        j = k*2
        if j < n and l[j] < l[j+1]:
            j += 1
        if l[k] < l[j]:
            l[k], l[j] = l[j], l[k]
            k = j
        else:
            break

def heapSort(l):
    n = len(l) - 1
    for i in range(n//2, 0, -1):
        fixDown(l, i, n)

    res = []
    for limit in range(0, 5):
        l[1], l[n] = l[n], l[1]
        res.append(l[n])
        fixDown(l, 1, n-1)
        n -= 1
    return res

l = random.sample(range(1, 100001), 1000)
l = [-1] + l
res = heapSort(l)
print res

# 手写二分查找
def find(seq, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if seq[mid] == key:
            return mid
        elif seq[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return 'NOT FIND'

# 正确的递归写法:
def find(seq, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if seq[mid] == key:
            return mid
        if seq[mid] > key:
            return search(seq, key, low, mid-1)
        else:
            return search(seq, key, mid+1, high)
    return 'Not Found.'


seq = [-1, 1, 0, 2, 3, 4, 6, 5, 7, 8, 9]
res = find(seq, 0, len(seq)-1, 9)
print res

########## for bytedance ##########

# 实现LRU
# 基于普通dict和list实现, douban和bitdance面试题目
class Memory:

    def __init__(self, size):
        self.size = size
        self.cache = dict()
        self.keys = []

    def set(self, key, value):
        if self.cache.has_key(key):
            self.cache[key] = value
            self.keys.remove(key)
            self.keys.insert(0, key)
        elif len(self.keys) == self.size:
            old_key = self.keys.pop()
            self.cache.pop(old_key)
            self.keys.insert(0, key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.keys.insert(0, key)

    def get(self, key):
        if not self.cache.has_key(key):
            return None
        value = self.cache.get(key)
        self.keys.insert(0, key)
        return value

if __name__ == '__main__':
    testMemory = Memory(3)
    testMemory.set('a', 1)
    testMemory.set('b', 2)
    testMemory.set('c', 3)
    testMemory.set('d', 2)
    print testMemory.get('a')

# 求两个有序数组前k大的数, 拓展求m个有序数组前k大的数
def search(l1, l2, n):

    res = []
    i, j = len(l1)-1, len(l2)-1

    while i > -1 and j > -1:
        if l1[i] > l2[j]:
            res.append(l1[i])
            i -= 1
        else:
            res.append(l2[j])
            j -= 1
        if len(res) == n:
            return res

    res = res + l2[:j+1] if i == -1 else res + l1[:i+1]
    return res[:6]


if __name__ == '__main__':
    n = 6
    l1 = [-3, 0, 1, 3, 4, 5, 7]
    l2 = [-2, 1, 3, 3, 5, 6, 9]
    l3 = [-2, 1, 3]
    res1 = search(l1, l2, n)
    res2 = search(l1, l3, n)
    print res1, res2

# python实现二叉树的各种遍历和深度, 最短路径和最长路径:
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left 
        self.right = right 

def preTraverse(tree):
    if not tree:
        return None
    print tree.data
    preTraverse(tree.left)
    preTraverse(tree.right)

def midTraverse(tree):
    if not tree:
        return None
    midTraverse(tree.left)
    print tree.data
    midTraverse(tree.right)

def afterTraverse(tree):
    if not tree:
        return None
    afterTraverse(tree.left)
    afterTraverse(tree.right)
    print tree.data


import Queue
queue = Queue.Queue()

def levelTraverse(tree):
    if not tree:
        return None
    res = []
    queue.put(tree)
    while queue:
        tmp = queue.get()
        res.append(tmp.data) 
        if current.left:
            queue.put(current.left)
        if current.right:
            queue.put(current.right)
    return res

# 对二叉树而言, 深度优先就是先序遍历
def deepTraverse(tree):
    if not tree:
        return None
    print tree.data 
    deepTraverse(tree.left)
    deepTraverse(tree.right)

# 二叉树深度优先非递归
def deepTraverse(tree):
    if not tree:
        return None
    res = []
    stack = [tree]
    while stack:
        tmp = stack.pop()
        res.append(tmp.data)
        if tmp.right:
            stack.append(tmp.right)
        if tmp.left:
            stack.append(tmp.left)
    return res

def getDepth(tree):
    if not tree:
        return 0
    return max(getDepth(tree.left), getDepth(tree.right)) + 1

def getminpath(tree):
    if not tree:
        return 0
    if tree.left and tree.right:
        return min(getminpath(tree.left), getminpath(tree.right)) + tree.data
    if tree.left:
        return getminpath(tree.left) + tree.data
    if tree.right:
        return getminpath(tree.right) + tree.data
    else:
        return tree.data

def getmaxpath(tree):
    if not tree:
        return 0
    if tree.left and tree.right:
        return max(getmaxpath(tree.left), getmaxpath(tree.right)) + tree.data
    if tree.left:
        return getmaxpath(tree.left) + tree.data
    if tree.right:
        return getmaxpath(tree.right) + tree.data
    else:
        return tree.data

tree = node(1, node(3, node(7, node(0)), node(6)), node(2, node(5), node(4)))
pretraverse(tree)
midtraverse(tree)
aftertraverse(tree)
leveltraverse(tree)
deeptraverse(tree)
print getdepth(tree)
print getmaxpath(tree)
print getminpath(tree)

# 经典的根据先序和中序遍历, 求解后序遍历:
preList = list('DBACEGF')
midList = list('ABCDEFG')
afterList = []

def findAfterLis(preList, midList, afterList):

    if len(preList) == 0:
        return

    if len(preList) == 1:
        afterList.append(preList[0])
        return

    root = preList[0]
    n = midList.index(root)
    findAfterLis(preList[1:n+1], midList[:n], afterList)
    findAfterLis(preList[n+1:], midList[n+1:], afterList)
    afterList.append(root)

findAfterLis(preList, midList, afterList)
print afterList

# 判断两个树是否相同
def isSameTree(p, q):
    if not p  and not q:
        return True
    elif p and q :
        return p.data == q.data and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    else:
        return False


# 给定1到n, 按照字典序排序, 求第k大的数字:
# 更优秀的解法是与快速排序结合, 这是使用了插入排序
def lesser(a, b):
    a = list(str(a))
    b = list(str(b))
    i = 0

    while i < len(a) and i < len(b):
        if a[i] < b[i]:
            return True
        if a[i] > b[i]:
            return False
        i += 1

    if len(a) < len(b):
        return True
    else:
        return False

def dicSort(seq):
    for i in range(1, len(seq)):
        for j in range(i, 0, -1):
            if lesser(seq[j], seq[j-1]):
                seq[j], seq[j-1] = seq[j-1], seq[j]
    return seq

if __name__ == '__main__':
    seq = [2, 11, 202, 1, 0, 22, 3]
    seq = dicSort(seq)
    print seq

# 找出一个数组里有且仅有的两个相同的数字:
# 时间复杂度O(n), 空间复杂度O(n)
def findSame(l):

    target = dict()
    for i in range(len(l)):
        if target.get(l[i]):
            return l[i]
        target[l[i]] = 1

    return 'No Same'

if __name__ == '__main__':
    l = [7, 3, 4, 5, 2, 1, 2]
    k = findSame(l)
    print k

# python的OrderDict是如何实现O(1)的:
# 用另外一个字典保存位置信息
import collections
d=collections.OrderedDict()

# 有序数组去重
def delSame(seq):
    k = 1
    for i in range(1, len(seq)):
        if seq[i] != seq[i-1]:
            seq[k] = seq[i]
            k += 1
    return seq[:k]

if __name__ == '__main__':
     seq = [0, 1, 3, 3, 4, 5, 5, 5, 8, 9]
     print delSame(seq)

# 动态规划问题:
# python的动态规划问题: 求一个路径从第一行到最后一行的最大值
n = 3
m = 4
a = [[1, 4, 5, 10], [2, 3, 7, 9], [6, 9, 10, 8]]
sum_a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
sum_a[n-1] = a[n-1]
for i in range(n-2, -1, -1):
    for j in range(0, m):
        if j != m-1:
            sum_a[i][j] = a[i][j] + max(sum_a[i+1][j], sum_a[i+1][j+1])
        sum_a[i][j] = a[i][j] + max(sum_a[i+1][j], sum_a[i+1][j-1])
print sum_a

# 动态规划问题
# 给出一个长度为n的序列A1, A2,...,An, 求最大连续和
def maxSubArray(self, nums):
    Max = nums[0]
    pre_max = nums[0]
    for i in range(1, len(nums)):
        if pre_max > 0:
            pre_max = pre_max + nums[i]
        else:
            pre_max = nums[i]
        Max = max(Max, pre_max)
    return Max

# 给定一个整数数组, 找出两个不重叠子数组使得它们的和最大
def maxTwoSubArrays(nums):

    # 考虑边界 
    if not nums:
        return None
    if len(nums) <= 2:
        return sum(nums)

    Max = -65535
    pre_max = -65535
    for i in range(1, len(nums)):
        pre_max = maxArrays(nums[:i]) + maxArrays(nums[i:])
        Max = max(Max, pre_max)
    return Max

seq = [6, -3, 1, -2, 7, -15, 1, 2, 2]
print maxSubArray(seq)
print maxTwoSubArrays(seq)


# 动态规划
# 求两个字符串的最大公共子序列, 算法问题->数学问题->代码 
def lcs(a, b):

    lena = len(a)
    lenb = len(b)

    c=[[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    flag=[[0 for i in range(lenb + 1)] for j in range(lena + 1)]

    for i in range(lena):
        for j in range(lenb):
            if a[i]== b[j]:
                c[i+1][j+1] = c[i][j]+1
                flag[i+1][j+1] = 'ok'

            elif c[i+1][j] > c[i][j+1]:
                c[i+1][j+1] = c[i+1][j]
                flag[i+1][j+1] = 'left'

            else:
                c[i+1][j+1] = c[i][j+1]
                flag[i+1][j+1] = 'up'

    return c, flag

def printLcs(flag, a, i, j):
    if i == 0 or j == 0:
        return

    if flag[i][j] == 'ok':
        printLcs(flag, a, i-1, j-1)
        print a[i-1]

    elif flag[i][j] == 'left':
        printLcs(flag, a, i, j-1)

    else:
        printLcs(flag, a, i-1, j)

if __name__ == '__main__':

    a = 'ABCBDAB'
    b = 'BDCABA'
    c, flag = lcs(a, b)

    for i in c:
        print i
    print ''

    for j in flag:
        print j
    print ''

    printLcs(flag, a, len(a), len(b))
    print ''

# 动态规划
# 求两个字符串的最大公共子串, 算法问题->数学问题->代码
def lcs(a, b):

    lena = len(a)
    lenb = len(b)

    c=[[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    flag=[[0 for i in range(lenb + 1)] for j in range(lena + 1)]

    maxlen = 0
    for i in range(lena):
        for j in range(lenb):
            if a[i]== b[j]:
                c[i+1][j+1] = c[i][j]+1
		if c[i+1][j+1] > maxlen
                    maxlen = c[i+1][j+1]
                    p = i+1

    return c, a[p-maxlen:p]

if __name__ == '__main__':

    a = 'ABCBDAB'
    b = 'BDCABA'
    c, s = lcs(a, b)

    for i in c:
        print i

    print s 

# 使用python实现一个双向的队列
class Node:
    def __init__(self, data, pre=None, next=None):
        self.data = data
        self.pre = pre
        self.next = next

class Dqueue:
    def __init__(self, lis=[], left=None, right=None):
        self.left = Node(lis[0])
        tmp = self.left
        for i in lis[1:]:
           new =  Node(i)
           tmp.next = new
           new.pre = tmp
           tmp = new
           if lis.index(i) == len(lis)-1:
               self.right = tmp

    def showFromleft(self):
        tmp = self.left
        while tmp:
            print tmp.data
            tmp = tmp.next

    def showFromright(self):
        tmp = self.right
        while tmp:
            print tmp.data
            tmp = tmp.pre

    def leftIn(self, key):
        node = Node(key)
        node.next = self.left
        self.left.pre = node

        self.left = node

    def rightIn(self, key):
        node = Node(key)
        self.right.next = node
        node.pre = self.right

        self.right = node


if __name__ == '__main__':
    lis = [1, 2, 3, 4]
    dqueue = Dqueue(lis)
    dqueue.showFromleft()
    print ''
    dqueue.showFromright()
    print ''
    dqueue.leftIn(0)
    dqueue.rightIn(5)
    dqueue.showFromleft()
    print ''
    dqueue.showFromright()
    print ''

# l1: 2->4->3
# l2: 5->6->1
# 342 + 165 = 507 
# 带着carry, 实现逆置
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# 输出5->0->7
def addLists(l1, l2):

    first = Node(0)
    cur1 = l1
    cur2 = l2
    carry = 0

    while cur1 or cur2 or carry:
        v1 = v2 = 0
        if cur1:
            v1 = cur1.value
            cur1 = cur1.next
        if cur2:
            v2 = cur2.value
            cur2 = cur2.next

        carry, v = divmod(v1 + v2 + carry, 10)
        print 'carry: %s' % carry
        print 'v: %s' % v

        cur = Node(v)
        cur.next = first.next
        first.next = cur

    return first.next

# 输出7->0->5
# 多了一个dumpy
def addLists(l1, l2):
    dumpy = cur = Node(0)
    cur1 = l1
    cur2 = l2
    carry = 0
    while cur1 or cur2 or carry:
        v1 = v2 = 0
        if cur1:
            v1 = cur1.value
            cur1 = cur1.next
        if cur2:
            v2 = cur2.value
            cur2 = cur2.next
        v = (v1 + v2 + carry) % 10
        carry = (v1 + v2 + carry) / 10

        n = Node(v)
        cur.next = n
        cur = n

    return dumpy.next

def show(l):
    while l:
        print l.value
        l = l.next


l1 = Node(2, Node(4, Node(3)))
l2 = Node(5, Node(6, Node(1)))
l3 = addLists(l1, l2)
show(l3)

# 两个链表合并

# 输出指定list
def func(n):
    if len(str(n)) <= 1:
        return [n]
    ret = reduce(lambda x, y: int(x)*int(y), list(str(n)))
    return [n] + func(ret)

print func(777)


# 数组顺序最大差值
# O(n^2) 
def find_max_in_list(l):
    _max = l[0]
    for i in range(1, len(l)):
        if l[i] > _max:
            _max = l[i]
    return _max

def func(l):
    res = l[1] - l[0]
    for i in range(1, len(l)):
        l_temp = l[i:]
        max_in_list = find_max_in_list(l_temp)
        dis = max_in_list - l[i-1]
        if dis > res:
            res = dis
    return res

l = [0, 1, 2, 3, 4, 5, 6]
print func(l)
# O(n)
def func(l):

    cur_min = l[0]
    cur_max = l[0]
    best_min = l[0]
    best_max = l[0]
    best_diff = best_max - best_min

    for i in range(len(l)):

        if l[i] > cur_max:
            cur_max = l[i]

        if l[i] <= cur_min:
            cur_max = l[i]
            cur_max = l[i]

        if cur_max - cur_min > best_diff:
            best_max = cur_max
            best_min = cur_min
            best_diff = best_max - best_min

    return best_diff


l = [0, 1, 2, 3, 4, 5, 6]
print func(l)

# 统计k在一个数组range(0, n+1)里出现的次数:
def digitcount(k, n):
    return ''.join(map(str, range(1, n+1))).count(str(k))

print digitcount(1, 100)

# 关于丑数: 丑数就是只包含质因数 2, 3, 5 的正整数
# 判断一个数字是不是丑数
def isUgly(num):
    while num > 0 and num % 2 == 0:
        num /= 2
    while num > 0 and num % 3== 0:
        num /= 3
    while num > 0 and num % 5== 0:
        num /= 5
    return True if num == 1 else False

# 给第n个丑数, 这里用大顶堆(heapq)
import heapq
def nthUglyNumber(self, n):
    heap = [1]
    for i in range(n - 1):
        cur = heapq.heappop(heap)
        for factor in [2, 3, 5]:
            temp = cur * factor
            if temp not in heap:
                heapq.heappush(heap, temp)
    return heapq.heappop(heap)

# 数组中第k大的元素
# 数组中第k小的元素

# 含有重复元素的列表全排列
# if not in

# 求当前列表的所有子集
def func(nums):
    nums = sorted(nums)
    res = [[]]
    for num in nums:
        for i in range(len(res)):
            res.append(res[i] + [num])
    return res

print func([2, 1, 3])

# 求当前列表的所有子集可能包含重复元素
# if not in

# 给出三个字符串:s1, s2, s3, 判断s3是否由s1和s2交叉构成:
# 这个解法在leetcode上打败了百分之100的提交, 这是一个值得纪念的时刻, 100%AC!
def isInterleave(s1, s2, s3):
    i = j = k = 0
    while i < len(s1) and j < len(s2):
        if s3[k] not in [s1[i], s2[j]]:
            return False
        if s3[k] == s1[i] and s3[k] == s2[j]:
            return isInterleave(s1[i+1:], s2[j:], s3[k+1:]) or isInterleave(s1[i:], s2[j+1:], s3[k+1:])
        if s3[k] == s1[i]:
            i += 1
        else:
            j += 1
        k += 1
    
    if i == len(s1):
        return s3[k:] == s2[j:]
    return s3[k:] == s1[i:]

print isInterleave('aabcc', 'dbbca', 'aadbbcbcac')

# 数组划分
# 给出一个整数数组nums和一个整数k, 划分数组使得所有小于k的元素移到左边, 所有大于等于k的元素移到右边
# 返回数组划分的位置
# 两个while要写在一起!以后要形成写等号的习惯!
# 这个返回值是真的考究
def partitionArray(nums, k):
    i = 0
    j = len(nums) - 1

    while i <= j:
        while i <= j and nums[i] < k:
            i += 1
        while i <= j and nums[j] >= k:
            j -= 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    return i

print partitionArray([3, 2, 1], 2)
print partitionArray([3, 2, 3, 1], 2)
print partitionArray([1, 2, 3], 4)

# 两数之和, 不用index, 用enmerate实现带有index的算法
# 解法1 O(n2)
def twoSum(target, l):
    res = []
    for i in range(len(l)):
        for item in enumerate(l):
            if item[1] == target - l[i] and item[0] is not i:
                if sorted([i, item[0]]) not in res:
                    res.append(sorted([i, item[0]]))
    return res
# 解法2 O(n), 空间复杂度O(n), 用哈希表
def twoSum(nums, target):
    res = []
    hash = {}
    for i in range(len(nums)):
        if target - nums[i] in hash:
            res.append([hash[target - nums[i]], i])
        hash[nums[i]] = i
    return res

# 三数之和: n2
# 四数之和: n3 
def threeSum(nums, target):
    res = []
    for i in range(len(nums)):
        res_i = twoSum(nums, target-nums[i])
        if res_i:
            for item in res_i:
                res_item = sorted([i]+item)
                if i not in item and res_item not in res:
                    res.append(res_item)
    return res

def fourSum(nums, target):
    res = []
    for i in range(len(nums)):
        res_i = threeSum(nums, target-nums[i])
        if res_i:
            # 求值
            for item in res_i:
                res_item = [nums[i]] + [nums[o] for o in item]
                res_item = sorted(res_item)
                if i not in item and res_item not in res:
                    res.append(res_item)
            # 求index
            # for item in res_i:
                # if i not in item and sorted([i]+item) not in res:
                    # res.append([i]+item)
    return res

# 寻找峰值: 一个长度为n的数组, 满足A[0]<A[1] and A[n-2] > A[n-1]
# 时间复杂n
def findPeak(nums):
    i = 1
    while i < len(nums):
        if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
            return i
        else:
            i += 1
    return None

# O(log2n)
# 效率是最高的
def findPeak(self, nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) / 2
        if mid == left:
            return left
        if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
            return mid
        if nums[mid-1] > nums[mid]:
            right = mid
        else:
            left = mid

# 递归, 消耗空间
def findPeak(nums):
    n = len(nums)
    处理边界
    if n == 1:
        return 0
    if n == 2:
        return 0 if nums[0] > nums[1] else 1

    i = n // 2
    if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
        return i

    if nums[i - 1] > nums[i]:
        return findPeak(nums[:i+1])
    else:
        print nums[i+1:]
        return i + findPeak(nums[i+1:]) + 1
print findPeak([1,2,1,2,3,1])

# 字符串大小排序 
# 这个问题类似于数组划分
def sortLetters(self, nums):
    nums = list(nums)
    i = 0
    j = len(nums) - 1
    while i <= j:
        while i <= j and nums[i] >= 'a':
            i += 1
        while i <= j and nums[j] < 'a':
            j -=1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    return ''.join(nums)

# 三道动态规划
# 背包问题
# 只算质量, 没有价格
# O(n*m), O(n*m)
def backPack(nums, m):
    y = len(nums) + 1
    x = m + 1
    resArr = [[0] * x for _ in range(y)]
    for i in range(1, y):
        for j in range(1, x):
            if nums[i-1] <= j:
                resArr[i][j] = max(resArr[i-1][j-nums[i-1]]+nums[i-1], resArr[i-1][j])
            else:
                resArr[i][j] = resArr[i-1][j]
    print resArr
    return resArr[-1][-1]
print backPack([3,4,8,5], 10)

# 用boolean类型解决
def backPack(nums, m):
    y = len(nums) + 1
    x = m + 1
    f = [[False] * x for _ in range(y)]

    f[0][0] = True
    for i in range(1, y):
        f[i][0] = True
        for j in range(1, x):
            if j >= nums[i - 1]:
                f[i][j] = f[i - 1][j] or f[i - 1][j - nums[i - 1]]
            else:
                f[i][j] = f[i - 1][j]
    for line in f:
        print line
    for i in range(m, -1, -1):
        if f[y-1][i]:
            return i
    return 0
print backPack([3,4,8,5], 10)

# 传统的二维动态规划
# O(m*n), O(m)
def backPack(wlist, vlist, totalWeight, totalLength):
    resArr = np.zeros((totalLength+1, totalWeight+1), dtype=np.int32)
    print resArr
    for i in range(1, totalLength+1):
        for j in range(1, totalWeight+1):
            if wlist[i] <= j:
                resArr[i, j] = max(resArr[i-1, j-wlist[i]] + vlist[i], resArr[i-1, j])
            else:
                resArr[i, j] = resArr[i-1, j]

    print resArr
    return resArr[-1,-1]

w = [0, 1, 2, 3]
v = [0, 6, 10, 12]
weight = 5
n = 3
result = backPack(w, v, weight, n)
print(result)

# 数组中有正负数随机分布, 讲负数放在正数之前, 且不改变其原来的顺序
def partitionArray(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i] < 0:
            temp = nums[i]
            for j in range(i-1, k-1, -1):
                nums[j+1] = nums[j]
            nums[k] = temp
            k += 1
        print nums
    return nums
print partitionArray([2, -3, 3, 4, -1])

# 数组由负数0和正数组成, 将其重新排列为前面是负数中间是0后面是正数的结构, 要求时间复杂度为n
def orderNums(nums):
    start = 0
    end = len(nums) - 1
    # 按照零划分 
    while start <= end:
        while start <= end and nums[start] < 0:
            start += 1
        while start <= end and nums[end] >= 0:
            end -=1
        if start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    # 将正数放在零的后边
    k = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
        if nums[i] > 0:
            nums[k] = nums[i]
            nums[i] = 0
            k -= 1
    return nums

print orderNums([-1, 2, 4, 0, 4, -1, 0])

# 给两个int a, b 不用temp将数值调换
# 你吗||-_-
a = a + b
b = a - b
a = a - b

# 左右翻转二叉树
def reverse(tree):
    if not tree:
        return None
    queue = [tree]
    while queue:
        tmp = queue.pop()
        if tmp:
            tmp.left, tmp.right = tmp.right, tmp.left
            queue.append(tmp.left)
            queue.append(tmp.right)

    return serialPrint(tree)

# 单链表的两两反转
def swapPairs(head):

    if head == None or head.next == None:
        return head

    first = Node(0)
    first.next = head
    current = first

    while current.next and current.next.next:
        n1 = current.next
        n2 = n1.next
        tmp = n2.next
        current.next = n2
        n2.next = n1
        n1.next = tmp
        current = n1

    root = first.next
    while root:
        print root.value
        root = root.next

    return first.next

lis = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print swapPairs(lis)

# -------------------
# 递归算法二叉树的最长路径
def getLongestPath(root):
    ans = 1
    def getHeight(root):
        if root == None:
            return 0
        l = getHeight(root.left)
        r = getHeight(root.right)
        self.ans = max(ans, l + r + 1)
        return max(l, r) + 1
    
    getHeight(root)
    return self.ans - 1
# 带value的最长路径
def getLongestPath(root)
    self.curr_max = float('-inf')

    def getMax(root):
        if root == None:
            return 0
        left = max(0,getMax(root.left))
        right = max(0,getMax(root.right))
        self.curr_max = max(self.curr_max , left + right + root.val)
        return max(left,right)+root.val

    getMax(root)
    return self.curr_max

# -------------------
# 非递归二叉树高度
# 递归
def getDepth(tree):
    if not tree:
        return 0
    return max(getDepth(tree.left), getDepth(tree.right)) + 1

# 非递归
def getDepth(self, tree):

        if not tree:
            return 0

        length = 0
        nodeList= [tree]
        while nodeList:
            tempNodeList = []
            for node in nodeList::
                if node.left:
                    tempNodeList.append(node.left)
                if node.right:
                    tempNodeList.append(node.right)
            nodeList = tempNodeList
            length += 1
        return length

# -------------------
# 链表分段反转
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse(head):

    if not head or not head.next:
        return head

    tmp = head.next
    head.next = None
    while tmp:
        last = tmp.next
        tmp.next = head
        head = tmp
        tmp = last
    return head

def findkth(head, k):
    if head is None:
        return None
    for i in xrange(k):
        head = head.next
    return head

def reverseBetween(head, m, n):
    dummy = Node(-1, head)
    mth_prev = findkth(dummy, m - 1)
    mth = mth_prev.next
    nth = findkth(dummy, n)
    nth_next = nth.next
    nth.next = None

    # 原地反转
    reverse(mth)

    mth_prev.next = nth
    mth.next = nth_next

    return dummy.next

lis = Node(1, Node(2, Node(3, Node(4, Node(5)))))
lis = reverseBetween(lis, 1, 2)
head = lis
while head:
    print head.value
    head = head.next

# -------------------
# 给定一个整数序列, 找到最长上升子序列(LIS), 返回LIS的长度
# 这种子序列不一定是连续的或者唯一的 
# 动态规划O(n2)
def longestIncreasingSubsequence(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for curr, val in enumerate(nums):
        for prev in xrange(curr):
            if nums[prev] < val:
                dp[curr] = max(dp[curr], dp[prev] + 1)
    return max(dp)

# O(nlogN)
def longestIncreasingSubsequence(nums):
        res = []
        if len(nums) == 0:
            return 0
        res.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                if nums[i] < res[0]:
                    res[0] = nums[i]
                else:
                    position = binarySearch(res, 0, len(res)-1, nums[i])
                    print position
                    res[position] = nums[i]
            print res
        return len(res)

def binarySearch(lis, left, right, number):
    if left == right:
        return left
    while left < right:
        mid = (left + right) / 2
        if mid == left or mid == right:
            if number > lis[left]:
                return right
            else:
                return left
        if number < lis[mid]:
            return binarySearch(lis, left, mid, number)
        else:
            return binarySearch(lis, mid, right, number)

print longestIncreasingSubsequence([4, 2, 4, 5, 3, 7])

# -------------------
# 链表排序 
# O(nlogn) 
# 链表的归并排序
def merge(head1, head2):
    if head1 == None: return head2
    if head2 == None: return head1
    dummy = ListNode(0)
    p = dummy
    while head1 and head2:
        if head1.val <= head2.val:
            p.next = head1
            head1 = head1.next
            p = p.next
        else:
            p.next = head2
            head2 = head2.next
            p = p.next
    if head1 == None:
        p.next = head2
    if head2 == None:
        p.next = head1
    return dummy.next

def sortList(head):
    if head == None or head.next == None:
        return head

    # 快慢指针用来均分链表
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    head1 = head
    head2 = slow.next
    slow.next = None

    head1 = sortList(head1)
    head2 = sortList(head2)
    head = merge(head1, head2)


# -------------------
# 链表是否带环
def detectCycle(head):
    if head == None or head.next == None:
        return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True 
    return False

# 返回环的入口
# 原理 
# a + b
# a + b + n(b + c)
# n(b + c) = a + b
# (n - 1) * b + n * c = a
# (n - 1) * b + (n - 1) * c + c = a
# 从head走到a步, 相当于从相遇点走n-1圈, 在走c步
def findCycleEngrance(head):
    if head == None or head.next == None:
        return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    if slow == fast:
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    return None

# -------------------
# 合并k的排序链表(104)
# 两两合并

# -------------------
# 重排链表(99)

# -------------------
# 落单的数字

# -------------------
# 主元素, 严格占队列的至少一半
def findMajorElement(nums):
    key = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == key:
            count += 1
        else:
            if count == 1:
                key = nums[i]
            else:
                count -= 1
    return key
# 这样写更加安全
def findMajorElement(nums):
    key = None
    count = 0
    for i in range(len(nums)):
        if nums[i] == key:
            count += 1
        else:
            if count = 0:
                key = nums[i]
                count = 1
            else:
                count -= 1
    return key if count > 0 else None
# 主元素, 严格占队列的的至少K分之一(或者输出最多的元素)
def findMajorElement(nums):
    nums = sorted(nums)
    i = 0
    while i < len(nums):
        count_i = nums.count(nums[i])
        if count_i > len(nums) / k:
            return nums[i]
        i = i + count_i
    return None


def findMajorElement(nums):
    hash = {}
    for i in nums:
        if hash.get(i):
            hash[i] += 1
        else:
            hash[i] = 1
    # 字典键值对的排序, 输出结果为了一list, 其中item是一个元组
    hash = sorted(hash.items(), key=lambda x: x[1], reverse=True)
    return hash[0][0]

# 最小调整代价
# 动态规划
# 空间复杂度无法优化
def MinAdjustmentCost(nums, target):

    y = len(nums) + 1
    x = 100 + 1
    sys_max = 65536
    dp = [[sys_max] * x for _ in range(y)]

    for j in range(1, x):
        dp[1][j] = abs(nums[0]-j)

    for i in range(2, y):
        for j in range(1, x):
            left = max(1, j - target)
            right = min(j + target, 100)
            for o in range(left, right+1):
                dp[i][j] = min(dp[i-1][o]+abs(nums[i-1]-j), dp[i][j])

    return min(dp[y-1])

print MinAdjustmentCost([1, 4, 2, 3], 2)

# -------------------
# 一个无序数组, 改变一个数字能否成为非递减序列:
def judgement(nums):
count = 0
for i in range(1, len(nums)):
    if nums[i] >= nums[i-1]:
        continue
    if i-2 >= 0 and nums[i] < nums[i-2]:
        nums[i] = nums[i-1]
    else:
        nums[i-1] = nums[i]
    count += 1
return count
print judgement([4, 5, 1, 2, 3])
print judgement([6, 4, 5, 6, 7])

# -------------------
# 一个数组, 前半部分是负数, 中间是0, 后半部分是正数, 返回最后一个负数和第一个正数
# 这就是二分查找

def findNum(nums):
    start = 0
    end = len(nums)-1
    # 找到负数 
    while start <= end:
        mid = (start + end) / 2
        if nums[mid] < 0:
            if nums[mid+1] == 0:
                yield mid
                break
            else:
                start = mid + 1
        else:
            end = mid - 1
    # 找到正数
    start = mid
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) / 2
        if nums[mid] > 0:
            if nums[mid-1] == 0:
                yield mid
                break
            else:
                end = mid - 1
        else:
            start = mid + 1
res = findNum([-1, 0, 0, 2, 3])
for item in res:
    print item

# -------------------
# 插入区间
# 这样写是不对的, 因为tuple一旦初始化, 就不能被修改
def insert(lis, new_interval):
        results = []
        pos = 0
        for interval in lis:
            if interval[1] < new_interval[0]:
                results.append(interval)
                pos += 1
            elif interval[0] > new_interval[1]:
                results.append(interval)
            else:
                new_interval[0] = min(interval[0], new_interval[0])
                new_interval[1] = max(interval[1], new_interval[1])
        results.insert(pos, new_interval)
        return results

# 必须定义数据结构
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def insert(intervals, newInterval):
    results = []
    insertPos = 0
    for interval in intervals:
        if interval.end < newInterval.start:
            results.append(interval)
            insertPos += 1
            
        elif interval.start > newInterval.end:
            results.append(interval)
        else:
            newInterval.start = min(interval.start, newInterval.start)
            newInterval.end = max(interval.end, newInterval.end)
    results.insert(insertPos, newInterval)
    return results

print insert([(1, 2), (3, 5), (8, 9)], (6, 7))
print insert([(1, 2), (3, 5), (8, 9)], (2, 4))



