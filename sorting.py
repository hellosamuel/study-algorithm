def merge_sort(li):
    # 반으로 쪼개고, 나중에 이것을 정렬하면서 합쳐 간다
    # 복잡도: O(N * logN)보장
    if len(li) > 1:
        mid = len(li) // 2
        left, right = li[:mid], li[mid:]

        l, r = merge_sort(left), merge_sort(right)
        l_idx, r_idx, arr = 0, 0, []

        while l_idx < len(l) and r_idx < len(r):
            if l[l_idx] < r[r_idx]:
                arr.append(l[l_idx])
                l_idx += 1
            else:
                arr.append(r[r_idx])
                r_idx += 1

        if l_idx < len(l):
            arr += l[l_idx:]
        else:
            arr += r[r_idx:]

        return arr
    else:
        return li


def quick_sort(li):
    # 기준값(Pivot)으로 큰 숫자, 작은 숫자를 나눠서 분할 정복
    # 피벗 값보다 작은 값의 인덱스가 큰 값의 인덱스보다 작으면 작은 값과 피벗 값을 바꿔준 (분할)
    # 분할이 되면 피벗 값보다 왼쪽은 모두 피벗 값보다 작은 수가 되고 오른쪽은 모두 큰 수가 된다는 특징이 있다
    # 복잡도: O(N * logN)도, 최악 O(N^2) : 기준값이 편향적일 때, 이를 막기위해 랜덤으로 추출하는 것이 좋다

    if len(li) > 1:
        # Pivot 선정, 이 경우는 제일 마지막 값
        pivot = li[-1]
        left, mid, right = [], [], []

        # Pivot 빼고 정리
        for i in range(len(li) - 1):
            if li[i] < pivot:
                left.append(li[i])
            elif li[i] > pivot:
                right.append(li[i])
            else:
                mid.append(li[i])

        mid.append(pivot)
        return quick_sort(left) + mid + quick_sort(right)
    else:
        return li


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

    return li


def bubble_sort(li):
    # 옆과 비교해서 작은수를 앞으로 보낸다
    # 복잡도 O(N^2)
    for i in range(len(li)):
        for j in range(len(li) - 1 - i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

    return li


def insertion_sort(li):
    # 필요할 때만 위치를 바꾼다
    # 복잡도: O(N^2),
    # 필요할 때만 삽입을 진행하기에 정렬된 상태라면 어떤 알고리즘 보다 빠르다
    for i in range(len(li)-1):
        j = i
        while j >= 0 and li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
            j -= 1

    return li


def main():
    li = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

    print("selection_sort => ", bubble_sort(li))
    print("bubble_sort => ", insertion_sort(li))
    print("insertion_sort => ", insertion_sort(li))
    print("quick_sort => ", quick_sort(li))
    print("merge_sort => ", merge_sort(li))


if __name__ == "__main__":
    main()
