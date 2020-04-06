def selection_sort(li):
    # 루프 한번에 가장 작은 수를 찾아서 가장 앞으로 보낸다
    # 복잡도: O(N^2)
    for i in range(len(li)):
        idx = None
        m = 9999
        for j in range(i, len(li)):
            if m > li[j]:
                m = li[j]
                idx = j

        li[i], li[idx] = li[idx], li[i]

    print("selection_sort => ", li)


def bubble_sort(li):
    # 옆과 비교해서 작은수를 앞으로 보낸다
    # 복잡도 O(N^2)
    for i in range(len(li)):
        for j in range(len(li) - 1 - i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

    print("bubble_sort => ", li)


def insertion_sort(li):
    # 필요할 때만 위치를 바꾼다
    # 복잡도: O(N^2),
    # 필요할 때만 삽입을 진행하기에 정렬된 상태라면 어떤 알고리즘 보다 빠르다
    for i in range(len(li)-1):
        j = i
        while j >= 0 and li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
            j -= 1

    print("insertion_sort => ", li)


def main():
    li = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

    # selection_sort(li)
    # bubble_sort(li)
    # insertion_sort(li)


if __name__ == "__main__":
    main()
