# coding: utf-8

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
        # 这里已经可以返回
        elif interval.start > newInterval.end:
            results.append(interval)
        else:
            newInterval.start = min(interval.start, newInterval.start)
            newInterval.end = max(interval.end, newInterval.end)
    results.insert(insertPos, newInterval)
    return results

print insert([(1, 2), (3, 5), (8, 9)], (6, 7))
print insert([(1, 2), (3, 5), (8, 9)], (2, 4))


# -------------------
# 单链表逆置:
# 定义Node结构, 输出方法, 然后1, 2, 3, 4
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

lis = Node(1, Node(2, Node(3, Node(4, Node(5)))))
lis = reverse(lis)

while lis:
    print lis.value
    lis = lis.next


# -------------------
# 一个最简单的递归, 斐波那契数列
def digui(n):
    if n == 0 or n == 1:
        return n
    return n + digui(n-1)

n = 10
print digui(n)


# -------------------
# 快速排序
# 基本版本的快速排序
# (low和high要传0和len-1, if而不是while, while是<号不是<=, 暂存, 暂存的是nums[low])
def quickSort(seq, low, high):
    if low < high:
        pivot = partition(seq, low, high)
        quickSort(seq, low, pivot-1)
        quickSort(seq, pivot+1, high)

def partition(nums, low, high):
    key = nums[low]
    for low < high and nums[high] >= key:
        high -= 1
        nums[low] = nums[high]
    for low < high and nums[low] < key:
        low += 1
        nums[high] = nums[low]
    nums[low] = key
    return low

seq = [9, 8, 7, 6, 5, 4, 3, 2, 1]
quickSort(seq, 0, len(seq)-1)
print seq

# 另一个版本的快速排序
# 这个会好些, 不是原地
# (递归出口, 1:, [key])
def quickSort(nums):
    if len(nums) <= 1:
        return nums
    key = nums[0]
    left = quickSort([i for i in nums[1:] if i <= key])
    right= quickSort([i for i in nums[1:] if i > key])
    return left + [key] + right

seq = [9, 8, 7, 6, 5, 4, 3, 2, 1]
seq = quickSort(seq)
print seq


# -------------------
# bytedance面试
# python中list的pop和append方法使它更像是一个栈
# 用两个栈来实现一个队列(__init__, get, push)
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, key):
        self.stack1.append(key)

    def get(self):
        for i in range(len(self.stack1)):
           self.stack2.append(self.stack1.pop())
        res = self.stack2.pop()
        for i in range(len(self.stack2)):
           self.stack1.append(self.stack2.pop())
        return res

q = Queue()
q.inQueue(1)
q.inQueue(2)
q.inQueue(3)
q.showMe()
q.outQueue()
q.showMe()


# -------------------
# python实现约瑟夫环
# 定义Node数据结构, 生成单向循环列表, k-2!
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def yuesefu(n, k):
    # 边界检查
    if n < k:
        return False
    # 形成环
    root = Node(1)
    tmp = root
    for i in range(2, n+1):
        node = Node(i)
        tmp.next = node
        tmp = tmp.next 
    tmp.next = root
    # 依次报数
    tmp = root
    while True:
        for i in range(k-2):
            tmp = tmp.next
        o = tmp.next.value
        tmp.next = tmp.next.next
        tmp = tmp.next
        if tmp.next == tmp:
            return tmp.value
print yuesefu(10, 4)


# -------------------
# bytedance面试
# python递归实现全排列
# 这是一个天生的递归问题
def permute(nums):
    if nums == None:
        return None
    if len(nums) < 1:
        return [nums]
    res = []
    for i in range(len(nums)):
        key = nums[i]
        res_key = permute(nums[:i]+nums[i+1:])
        for item in res_key:
            res.append([key]+item)
    return res

res = permute([1, 2, 3])
for i in res:
    print i

# 非递归解法
# 这个更快
# 这个算法也很重要, 记住吧 O(n2)
def get_list(nums, new_num):
    res = []
    for i in range(len(nums)+1):
        res.append(nums[:i]+[new_num]+nums[i:])
    return res

def permute(nums):
    if nums == None:
        return None
    if len(nums) < 1:
        return [nums]
    nums = sorted(nums)
    res = [[nums[0]]]
    for num in nums[1:]:
        for res_item in res:
            res = res + get_list(res_item, num)
            res = res[1:]
    return res

print permute([1, 2, 3, 4])

# 含有重复元素的列表全排列
# if not in


# -------------------
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

# 输出一个list中, 加和为m的所有的可能
# 递归
def func(seq, m, path=[]):
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
func(seq, m)


# -------------------
# 找出一个数组里有且仅有的两个相同的数字:
# 时间复杂度O(n), 空间复杂度O(n)
def findSame(l):

    hash = {} 
    for i in range(len(l)):
        if hash.get(l[i]):
            return l[i]
        hash[l[i]] = 1

    return 'No Same'

l = [7, 3, 4, 5, 2, 1, 2]
print findSame(l)


# -------------------
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

# -------------------
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


# -------------------
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


# -------------------
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


# -------------------
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


# -------------------
# 堆排序拓展:
# 求前一百个
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


# -------------------
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


# -------------------
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


# -------------------
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


# -------------------
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

# Queue: get or put 不是push
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
# 二叉树的先序遍历非递归
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

# 递归求深度
def getDepth(tree):
    if not tree:
        return 0
    return max(getDepth(tree.left), getDepth(tree.right)) + 1

# 非递归求深度
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

# 从根节点到叶子节点的最小加和
def getRootMinpath(tree):
    if not tree:
        return 0
    return min(getminpath(tree.left), getminpath(tree.right)) + tree.data

# 从根节点到叶子节点的最大加和
def getRootmaxpath(tree):
    if not tree:
        return 0
    return max(getmaxpath(tree.left), getmaxpath(tree.right)) + tree.data

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

# 判断两个树是否相同
def isSameTree(p, q):
    if not p and not q:
        return True
    elif p and q :
        return p.data == q.data and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    else:
        return False

tree = node(1, node(3, node(7, node(0)), node(6)), node(2, node(5), node(4)))
pretraverse(tree)
midtraverse(tree)
aftertraverse(tree)
leveltraverse(tree)
deeptraverse(tree)
print getdepth(tree)
print getmaxpath(tree)
print getminpath(tree)


# -------------------
# 由先序和中序可以确定一棵二叉树, 有中序和后续也可以确定一棵二叉树, 但由先序和后续不可以
# 由先序和中序构造二叉树
def buildTree(preorder, inorder):
    if not inorder:
        return None
    root = TreeNode(preorder[0])
    rootPos = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1:1+rootPos], inorder[:rootPos])
    root.right = self.buildTree(preorder[rootPos + 1 : ], inorder[rootPos + 1 : ])
    return root

# 由中序和后续构造二叉树
def buildTree(self, inorder, postorder):
    if not inorder:
        return None
    root = TreeNode(postorder[-1])
    rootPos = inorder.index(postorder[-1])
    root.left = self.buildTree(inorder[:rootPos], postorder[:rootPos])
    root.right = self.buildTree(inorder[rootPos+1:], postorder[rootPos:-1])
    return root

# 然后可以求出另外一种遍历


# -------------------
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

seq = [2, 11, 202, 1, 0, 22, 3]
seq = dicSort(seq)
print seq


# -------------------
# 有序数组去重
def delSame(nums):
    k = 1
    for i in range(1, len(nums)):
        if seq[i] != seq[i-1]:
            seq[k] = seq[i]
            k += 1
    return seq[:k]

num = [0, 1, 3, 3, 4, 5, 5, 5, 8, 9]
print delSame(num)


# -------------------
# douyin
# =====动态规划问题=====
# 一个矩阵中求一个路径从第一行到最后一行的最大值
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
# 求两个字符串的最长公共子串的长度, 算法问题->数学问题->代码
def longestCommonSubstring(a, b):
    x = len(a) + 1
    y = len(b) + 1
    dp = [[0] * y for _ in range(x)]

    Max = 0
    index_at_a = 0
    for i in range(1, x):
        for j in range(1, y):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                Max = max(Max, dp[i][j])
                index_at_a = i
    return Max, index_at_a

a = 'ABCBDAB'
b = 'BDCABA'
print longestCommonSubstring(a, b)

# 背包问题
# 动态规划
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

# 动态规划O(n2)
# 给定一个整数序列, 找到最长上升子序列(LIS), 返回LIS的长度
# 这种子序列不一定是连续的或者唯一的 
def longestIncreasingSubsequence(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for curr, val in enumerate(nums):
        for prev in xrange(curr):
            if nums[prev] < val:
                dp[curr] = max(dp[curr], dp[prev] + 1)
    return max(dp)

# 动态规划
# 最小调整代价
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


# 给出三个字符串:s1, s2, s3, 判断s3是否由s1和s2交叉构成:
# 动态规划
def isInterleave(a, b, c):

    # 这个边界必须加
    if len(a) + len(b) != len(c):
        return False

    y = len(a) + 1
    x = len(b) + 1
    dp = [[False] * x for _ in range(y)]

    # 这里不用把dp[i][j]置True, 因为这个元素跟dp[1]和dp[0][1]无关, 他们是直接渲染的
    for i in range(1, y):
        dp[i][0] = a[:i] == c[:i]
    for i in range(1, x):
        dp[0][i] = b[:i] == c[:i]

    # or的用例('aba', 'a', 'aaba')
    for i in range(1, y):
        for j in range(1, x):
            k = i + j
            if c[k-1] == a[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i][j]
            if c[k-1] == b[j-1]:
                dp[i][j] = dp[i][j-1] or dp[i][j]

    return dp[y-1][x-1]

res = isInterleave('aba', 'a', 'aaba')
for row in res:
    print row

# 递归解法
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


# -------------------
# 使用python实现一个双向的队列
# 使用Node
class Node:
    def __init__(self, data, pre=None, next=None):
        self.data = data
        self.pre = pre
        self.next = next

class Dqueue:
    def __init__(self, lis=[], left=None, right=None):
        if not list:
            return None
        self.left = Node(lis[0])
        self.right = Node(lis[0]) 
        tmp = self.left
        for i in lis[1:]:
            node = Node(i)
            tmp.next = node
            node.pre = tmp 
            tmp = node
            self.right = node

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


# -------------------
# l1: 2->4->3
# l2: 5->6->1
# 342 + 165 = 507 
# 链表加法, 先搞个dumpy
# 带着carry, 实现逆置
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# 输出5->0->7
def addLists(l1, l2):

    dumpy = Node(0)
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


# -------------------
# 两个链表合并


# -------------------
# 数组顺序最大差值
# 老虎证券
# O(n^2) 
def find_max_in_list(l):
    Max = l[0]
    for i in range(1, len(l)):
        if l[i] > Max:
            Max = l[i]
    return Max

def func(l):
    Max = -65535 
    for i in range(1, len(l)):
        l_temp = l[i:]
        max_in_list = find_max_in_list(l_temp)
        dis = max_in_list - l[i-1]
        Max = max(dis, Max)
    return Max 
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
            cur_mix = l[i]
            cur_max = l[i]

        if cur_max - cur_min > best_diff:
            best_max = cur_max
            best_min = cur_min
            best_diff = best_max - best_min

    return best_diff

l = [0, 1, 2, 3, 4, 5, 6]
print func(l)


# -------------------
# 统计k在一个数组range(0, n+1)里出现的次数:
def digitcount(k, n):
    return ''.join(map(str, range(1, n+1))).count(str(k))
print digitcount(1, 100)


# -------------------
# 关于丑数: 丑数就是只包含质因数2, 3, 5 的正整数
# 判断一个数字是不是丑数
def isUgly(num):
    while num > 0 and num % 2 == 0:
        num /= 2
    while num > 0 and num % 3== 0:
        num /= 3
    while num > 0 and num % 5== 0:
        num /= 5
    return True if num == 1 else False

# 给第n个丑数 
# heaq是小顶堆
import heapq
def nthUgly(self, n):
    heap = [1]
    for i in range(n - 1):
        cur = heapq.heappop(heap)
        for factor in [2, 3, 5]:
            tmp = cur * factor
            if tmp not in heap:
                heapq.heappush(heap, tmp)
    return heapq.heappop(heap)


# -------------------
# 数组中第k大的元素
# 数组中第k小的元素
# 先排序, 去nums[k-1] (Onlogn)
# 小米面试
def kthLargestElement(nums, k):
    # 边界
    if not nums or k < 1 or k > len(nums):
        return None
    # 利用快排
    pivot = partition(nums, 0, len(nums)-1)
    length = len(nums) - (pivot+1)

    if length == k - 1:
        return nums[pivot]
    elif length > k - 1:
        return kthLargestElement(nums[pivot+1:], k)
    else:
        return kthLargestElement(nums[:pivot+1], k-length)

def partition(nums, low, high):
    key = nums[low]
    for low < high and nums[high] >= key:
        high -= 1
        nums[low] = nums[high]
    for low < high and nums[low] < key:
        low += 1
        nums[high] = nums[low]
    nums[low] = key
    return low

print kthLargestElement([9,3,2,4,8], 3)


# -------------------
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


# -------------------
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


# -------------------
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


# -------------------
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
        if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
            return mid
        if nums[mid-1] > nums[mid]:
            right = mid
        else:
            # 这里不能是mid-1 nums[mid-1] < nums[mid] < nums[mid+1]
            left = mid

# 递归, 消耗空间
def findPeak(nums):
    n = len(nums)
    # 处理边界
    if n == 1:
        return 0
    if n == 2:
        return 0 if nums[0] > nums[1] else 1
    # 找到
    i = n // 2
    if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
        return i
    if nums[i-1] > nums[i]:
        return findPeak(nums[:i+1])
    else:
        return i + findPeak(nums[i:])
print findPeak([1,2,1,2,3,1])


# -------------------
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



# -------------------
# 给两个int a, b 不用temp将数值调换
# 你吗||-_-
a = a + b
b = a - b
a = a - b


# -------------------
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
    return tree


# -------------------
# 单链表的两两反转
def swapPairs(head):

    if head == None or head.next == None:
        return head

    dumpy = Node(0)
    dumpy.next = head
    current = dumpy 

    while current.next and current.next.next:
        n1 = current.next
        n2 = n1.next
        tmp = n2.next
        current.next = n2
        n2.next = n1
        n1.next = tmp
        current = n1

    root = dumpy.next
    while root:
        print root.value
        root = root.next

    return dumpy.next

lis = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print swapPairs(lis)



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
    mth_prev = findkth(dummy, m-1)
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
# 把一个链表插入另外一个链表
# L0L1..Ln-1Ln
# L0LnL1Ln-1L2Ln-2...
def reorderList(self, head):
    if not head or not head.next:
        return head
    # 快慢指针
    slow = fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    l1 = head
    l2 = slow.next
    slow.next = None
    # 逆置
    l2 = self.listReverse(l2)
    # 插入
    tmp = l1
    while l2:
        last = l2.next
        l2.next = tmp.next
        tmp.next = l2
        tmp = tmp.next.next
        l2 = last
    return l1


# -------------------
# 落单的数字
# 异或
def singleNumber(nums):
    res = 0;
    for num in nums:
        res = res ^ x
    return res 


# -------------------
# 主元素问题
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

# 输出当前队列中对多的元素
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

# # 一个奇数node升序和偶数node降序的链表, 要求对这个链表排序
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def listReverse(head):
    # 边界
    if not head or head.next == None:
        return head
    tmp = head.next
    head.next = None
    while tmp:
        last = tmp.next
        tmp.next = head
        head = tmp
        tmp = last
    return head

def mergeLists(l1, l2):
    # 边界
    if not l1: return l2
    if not l2: return l1
    dumpy = Node(0)
    tmp = dumpy
    while l1 and l2:
        if l1.value <= l2.value:
            tmp.next = l1
            l1 = l1.next
        else:
            tmp.next = l2
            l2 = l2.next
        tmp = tmp.next
    tmp.next = l1 if l1 else l2
    return dumpy.next

def sortList(head):
    # 边界
    if not head or head.next == None:
        return head
    # 拆, 注意尾巴置空
    l1 = cur1 = head
    l2 = cur2 = head.next
    tmp = cur2.next
    cur1.next = None
    cur2.next = None
    Flag = True
    while tmp:
        if Flag:
            cur1.next = tmp
            cur1 = tmp
        else:
            cur2.next = tmp
            cur2 = tmp
        Flag = not Flag
        tmp = tmp.next
        cur1.next = cur2.next = None

    l2 = listReverse(l2)
    lis  = mergeLists(l1, l2)
    return lis

def printList(head):
    while head:
        print head.value
        head = head.next

lis = Node(1, Node(10, Node(3, Node(9, Node(5)))))
res = sortList(lis)
printList(res)
