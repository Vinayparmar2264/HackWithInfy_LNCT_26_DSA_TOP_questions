import heapq

class MedianFinder:

    def __init__(self):
        self.left_max_heap = []   # max heap (store negatives)
        self.right_min_heap = []  # min heap

    def addNum(self, num: int) -> None:

        if len(self.left_max_heap) == 0 or num <= -self.left_max_heap[0]:
            heapq.heappush(self.left_max_heap, -num)
        else:
            heapq.heappush(self.right_min_heap, num)

        # Balance heaps
        if len(self.left_max_heap) > len(self.right_min_heap) + 1:
            heapq.heappush(self.right_min_heap, -heapq.heappop(self.left_max_heap))

        elif len(self.left_max_heap) < len(self.right_min_heap):
            heapq.heappush(self.left_max_heap, -heapq.heappop(self.right_min_heap))

    def findMedian(self) -> float:

        if len(self.left_max_heap) == len(self.right_min_heap):
            return (-self.left_max_heap[0] + self.right_min_heap[0]) / 2

        else:
            return -self.left_max_heap[0]
