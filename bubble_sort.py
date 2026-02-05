from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    """使用冒泡排序对整数列表进行升序排序，并返回新列表。"""
    arr = nums.copy()
    n = len(arr)

    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # 本轮没有发生交换，说明已经有序，可提前结束
        if not swapped:
            break

    return arr


if __name__ == "__main__":
    sample = [5, 1, 4, 2, 8]
    print("原始数组:", sample)
    print("排序结果:", bubble_sort(sample))
