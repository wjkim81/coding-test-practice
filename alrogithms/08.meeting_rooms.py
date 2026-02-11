"""
## Day 5 – Problem 2

## **Meeting Rooms** (또는 Non-overlap Intervals)

(보통 Merge Intervals 다음에 세트로 나옵니다)

### 문제 (Meeting Rooms I)

회의 시간 배열 `intervals`가 주어질 때,
**모든 회의를 한 사람이 참석할 수 있으면 True**, 아니면 False.

### 예시

```text
intervals = [[0,30],[5,10],[15,20]]
→ False
```

```text
intervals = [[7,10],[2,4]]
→ True
```

---

### 핵심 아이디어

* start 기준 정렬
* 이전 회의의 end와 현재 start 비교
* 겹치면 바로 False

이건 사실 **Merge Intervals의 부분 문제**입니다.
"""

def meeting_rooms(intervals: list[list[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        curr_start, _ = intervals[i]
        _, prev_end = intervals[i - 1]
        if curr_start < prev_end:
            return False
        
    return True

# 아주 미세한 개선(선택)
# def meeting_rooms(intervals: list[list[int]]) -> list[list[int]]:
#     intervals.sort(key=lambda x: x[0])
#     for i in range(1, len(intervals)):
#         if intervals[i][0] <= intervals[i - 1][1]:
#             return False

#     return True



if __name__ == "__main__":

    # intervals = [[0,30],[5,10],[15,20]]
    intervals = [[7,10],[2,4]]
    print(intervals)

    print(meeting_rooms(intervals))
