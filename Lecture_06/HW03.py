import random

def random_data(n):
    return [random.randint(1, 1000000) for _ in range(n)]

def seqSearch(arr, target):
    count = 0
    for num in arr:
        count += 1
        if num == target:
            return count
    return count

def binSearch(arr, target):
    count = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return count
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return count

# 데이터 생성
data = random_data(1000000)
target = random.choice(data)

# 정렬된 데이터 생성
sorted_data = sorted(data)

# 순차 검색 횟수 측정
seqSearch_count = seqSearch(data, target)

# 이진 검색 횟수 측정
binSearch_count = binSearch(sorted_data, target)

print('# 비정렬 배열(100만개) --> ', data)
print('# 정렬 배열(100만개) --> ', sorted_data)
print("순차 검색(비정렬 데이터) --> %d회 " % seqSearch_count)
print("이진 검색(정렬 데이터) --> %d회" % binSearch_count)


