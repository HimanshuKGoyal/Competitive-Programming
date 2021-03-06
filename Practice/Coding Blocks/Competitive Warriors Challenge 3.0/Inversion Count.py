def merge(data, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    a = [0] * (n1)
    b = [0] * (n2)
    for i in xrange(n1):
        a[i] = data[start + i]
    for i in xrange(n2):
        b[i] = data[mid + 1 + i]
    i = 0
    j = 0
    k = start
    ans = 0
    while i < n1 and j < n2:
        if a[i] <= b[j]:
            data[k] = a[i]
            i += 1
        else:
            ans += mid - i + 1 - start
            data[k] = b[j]
            j += 1
        k += 1
    while i < n1:
        data[k] = a[i]
        i += 1
        k += 1
    while j < n2:
        data[k] = b[j]
        j += 1
        k += 1
    return ans
        
def merge_sort(data, start, end):
    ans = 0
    if start < end:
        mid = (start + end) / 2
        ans = merge_sort(data, start, mid)
        ans += merge_sort(data, mid + 1, end)
        ans += merge(data, start, mid, end)
    return ans

t = int(raw_input())
for i in xrange(t):
    n = int(raw_input())
    data = [int(j) for j in raw_input().split()]
    print merge_sort(data, 0, n - 1)
