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

def levelTraverse(tree):
    if not tree:
        return None
    stack = []
    stack.append(tree)
    while stack:
        current = stack.pop()
        print current.data
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

def deepTraverse(tree):
    if not tree:
        return None
    print tree.data 
    deepTraverse(tree.left)
    deepTraverse(tree.right)

def getDepth(tree):
    if not tree:
        return 0
    return max(getDepth(tree.left), getDepth(tree.right)) + 1

def getMinPath(tree):
    if not tree:
        return 0
    if tree.left and tree.right:
        return min(getMinPath(tree.left), getMinPath(tree.right)) + tree.data
    if tree.left:
        return getMinPath(tree.left) + tree.data
    if tree.right:
        return getMinPath(tree.right) + tree.data
    else:
        return tree.data

def getMaxPath(tree):
    if not tree:
        return 0
    if tree.left and tree.right:
        return max(getMaxPath(tree.left), getMaxPath(tree.right)) + tree.data
    if tree.left:
        return getMaxPath(tree.left) + tree.data
    if tree.right:
        return getMaxPath(tree.right) + tree.data
    else:
        return tree.data

if __name__ == '__main__':
    tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    preTraverse(tree)
    midTraverse(tree)
    afterTraverse(tree)
    levelTraverse(tree)
    deepTraverse(tree)
    print getDepth(tree)
    print getMaxPath(tree)
    print getMinPath(tree)

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
def getMax(seq):
    Max = seq[0]
    preMax = 0
    for i in seq:
        if preMax < 0:
            preMax = i 
        else:
            preMax += i
    Max = max(Max, preMax)
        return Max

if __name__ == '__main__':
    seq = [6, -3, 1, -2, 7, -15, 1, 2, 2]
    print getMax(seq)

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
# 输出5->0->7
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def func(l1, l2):

    lead = Node(0)
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
        cur.next = lead.next
        lead.next = cur

    return lead.next

def show(l):
    while l:
        print l.value
        l = l.next


l1 = Node(2, Node(4, Node(3)))
l2 = Node(5, Node(6, Node(1)))

l3 = func(l1, l2)
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

