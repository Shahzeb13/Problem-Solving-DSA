

import heapq
from unittest import result


def TopKFreq(nums , k):
    count = {};
    for num in nums:
        count[num] = 1 + count.get(num , 0);
    print(f"Count  : {count}")
    heap = [];
    for key in count.keys():
        heapq.heappush(heap , (count[key] , key));
        if len(heap) > k:
            heapq.heappop(heap);
    print(f"Heap : {heap}")
    result = [];
    for _ in range(k):
        result.append(heapq.heappop(heap)[1]);
    print(f"result : {result}")


res = TopKFreq([2 ,2,2,3,4,3,3,3] , 2);
