import random
import time

class Sort:
    def __init__(self, n):
        self.len = n
        self.arr = [0] * n
        self.random_data()  # 在初始化中自动运行

    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0, 99)

    def partition(self, left, right):
        i = k = left

        random_position = random.randint(left, right)
        self.arr[random_position], self.arr[right] = (self.arr[right], self.arr[random_position])
        # 保证不会出现n方的时间复杂度（打破有序）

        for i in range(left, right):
            if self.arr[i] < self.arr[right]:
                self.arr[i], self.arr[k] = self.arr[k], self.arr[i]
                k += 1
        self.arr[k], self.arr[right] = self.arr[right], self.arr[k]
        return k

    def quicksort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.quicksort(left, pivot - 1)
            self.quicksort(pivot + 1, right)


    def adjust_max_heap(self, pos, arr_len):
        """
        把某个子树调整为大根堆
        :param pos: 被调整的元素位置，是父亲
        :param arr_len: 当时列表总长度
        :return:
        """
        arr = self.arr
        dad = pos
        son = 2 * dad + 1
        while son < arr_len:  # 左孩子小于列表长度
            if son + 1 < arr_len and arr[son] < arr[son + 1]:  # 判断右孩子存在，且右孩子大于左孩子
                son += 1
            if arr[son] > arr[dad]:
                arr[dad], arr[son] = arr[son], arr[dad]
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap_sort(self):
        # 把列表调整为大根堆
        for parent in range(self.len // 2 - 1, -1, -1):   # self.len//2-1是最后一个父节点的位置； 第三个-1是指倒着数
            self.adjust_max_heap(parent, self.len)
        arr = self.arr
        arr[0], arr[self.len - 1] = arr[self.len - 1], arr[0]  # 堆顶元素和最后一个元素交换
        for arr_len in range(self.len - 1, 1, -1):
            self.adjust_max_heap(0, arr_len)
            arr[0], arr[arr_len - 1] = arr[arr_len - 1], arr[0]


    def test_time_use(self, sort_func, *args, **kwargs):
        """
        回调函数
        :param sort_func:
        :param args:
        :param kwargs:
        :return:
        """
        start = time.time()
        sort_func(*args, **kwargs)
        end = time.time()
        print(f'总计用时{end - start}')

if __name__ == '__main__':
    sort1 = Sort(10000)
    # print(sort1.arr)
    # sort1.quicksort(0, 9)
    # print(sort1.arr)
    # strat = time.time()  # 距离1970某天的时间（秒）
    # sort1.heap_sort()
    # end = time.time()
    # print('堆排最终的时间是:', end-strat)
    # strat = time.time()
    # sort1.quicksort(0, 9999)
    # end = time.time()
    # print('快排最终的时间：:', end-strat)
    sort1.test_time_use(sort1.heap_sort)
