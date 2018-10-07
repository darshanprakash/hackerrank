import heapq

def cookies(k, A):
    count=0
    heapq.heapify(A)
    while A[0] < k:
        least_sweet = heapq.heappop(A)
        if A == []: 
            return -1
        second_least_sweet = heapq.heappop(A)
        cookie = least_sweet + 2 * second_least_sweet
        heapq.heappush(A, cookie)
        count += 1
    return count
    
if __name__ == '__main__':
    k=7
    A=[1,2,3,9,10,12]
    print(cookies(k, A))