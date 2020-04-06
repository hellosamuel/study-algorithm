li_for_quick = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]


def quick_sort(data, start, end):
    # 기준값(Pivot)으로 큰 숫자, 작은 숫자를 나눠서 분할 정복
    # 피벗 값보다 작은 값의 인덱스가 큰 값의 인덱스보다 작으면 작은 값과 피벗 값을 바꿔준 (분할)
    # 분할이 되면 피벗 값보다 왼쪽은 모두 피벗 값보다 작은 수가 되고 오른쪽은 모두 큰 수가 된다는 특징이 있다
    # 복잡도: O(N * logN)
    if start >= end:
        # 원소가 한 개인 경우
        return data

    key = start
    i = start + 1
    j = end

    # 분할 (엇갈릴 떄)까지 반복
    while i <= j:
        while i <= end and data[i] <= data[key]:
            i += 1
        while j > start and data[j] >= data[key]:
            j -= 1

        # 엇갈리면 키 값과 교체, 아니면 큰 값, 작은 값 서로 교체
        if i > j:
            data[j], data[key] = data[key], data[j]
        else:
            data[i], data[j] = data[j], data[i]

    quick_sort(data, start, j - 1)
    quick_sort(data, j + 1, end)


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
    selection_sort(li)
    bubble_sort(li)
    insertion_sort(li)

    quick_sort(li_for_quick, 0, len(li_for_quick)-1)
    print(li_for_quick)


if __name__ == "__main__":
    main()
