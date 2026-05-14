# 1. `list`

## Import

필요 없음. 기본 자료구조.

## 사용

```python
arr = []
arr.append(3)
arr.append(5)

arr[0]        # 3
arr[-1]       # 5
len(arr)      # 2
```

## 언제 쓰나

가장 기본적인 “순서 있는 컨테이너”.

코딩테스트에서는:

```python
values = []
for x in data:
    if condition:
        values.append(x)
```

이 패턴 엄청 많음.

ML preprocessing에서도 valid sample 모았다가 마지막에:

```python
X = np.stack(X_list)
```

이런 식으로 자주 씀.

## 주의

```python
arr.pop()
```

은 마지막 원소 제거는 빠름.

하지만:

```python
arr.pop(0)
```

은 느림. 앞에서 빼야 하면 `deque`가 낫다.

---

# 2. `tuple`

## Import

필요 없음.

## 사용

```python
point = (1.0, 2.0, 3.0)

x, y, z = point
```

## 언제 쓰나

변하지 않는 고정 구조.

예:

```python
point = (x, y, z)
bbox_min = (xmin, ymin, zmin)
shape = (N, D)
```

geometry 문제에서 많이 나옴.

## list와 차이

```python
[1, 2, 3]  # mutable
(1, 2, 3)  # immutable
```

tuple은 dict key로도 쓸 수 있음.

```python
visited = set()
visited.add((i, j))
```

---

# 3. `dict`

## Import

필요 없음.

## 사용

```python
d = {}

d["drag"] = 0.21
d["lift"] = 1.32

d["drag"]          # 없으면 KeyError
d.get("drag")      # 없으면 None
d.get("mass", 0.0) # 없으면 0.0
```

## 언제 쓰나

key-value mapping.

실무형 문제에서는 거의 항상 나옴.

예:

```python
sample = {
    "id": "case_001",
    "features": [1.0, 2.0],
    "target": 0.5,
}
```

## 안전한 접근

```python
features = sample.get("features")
if features is None:
    continue
```

이 패턴이 중요함.

## 자주 쓰는 메서드

```python
d.keys()
d.values()
d.items()
```

예:

```python
for key, value in d.items():
    print(key, value)
```

---

# 4. `set`

## Import

필요 없음.

## 사용

```python
seen = set()

seen.add("case_001")

"case_001" in seen
```

## 언제 쓰나

중복 제거, 빠른 membership check.

```python
ids = ["a", "b", "a"]
unique_ids = set(ids)
```

## 시간복잡도

```python
x in list   # O(N)
x in set    # average O(1)
```

## 코딩테스트 대표 패턴

```python
seen = set()

for x in nums:
    if x in seen:
        return True
    seen.add(x)
```

---

# 5. `collections.defaultdict`

## Import

```python
from collections import defaultdict
```

## 사용

```python
from collections import defaultdict

groups = defaultdict(list)

groups["angle_5"].append(0.21)
groups["angle_5"].append(0.18)
```

일반 dict였다면:

```python
if key not in groups:
    groups[key] = []
groups[key].append(value)
```

이렇게 해야 함.

## 언제 쓰나

grouping / aggregation.

예:

```python
from collections import defaultdict

metrics_by_angle = defaultdict(list)

for run in runs:
    angle = run["parameters"]["angle"]
    drag = run["metrics"]["drag"]
    metrics_by_angle[angle].append(drag)
```

## count용

```python
counts = defaultdict(int)

for label in labels:
    counts[label] += 1
```

---

# 6. `collections.Counter`

## Import

```python
from collections import Counter
```

## 사용

```python
from collections import Counter

labels = ["ok", "failed", "ok", "ok"]
counter = Counter(labels)

counter["ok"]      # 3
counter["failed"]  # 1
```

## 언제 쓰나

빈도수 세기.

```python
Counter("banana")
```

결과:

```python
Counter({'a': 3, 'n': 2, 'b': 1})
```

## 자주 쓰는 메서드

```python
counter.most_common()
counter.most_common(2)
```

---

# 7. `collections.deque`

## Import

```python
from collections import deque
```

## 사용

```python
from collections import deque

q = deque()

q.append(1)
q.append(2)

q.popleft()  # 1
q.popleft()  # 2
```

## 언제 쓰나

queue, BFS, sliding window.

list에서:

```python
arr.pop(0)
```

은 느림.

deque는:

```python
q.popleft()
```

가 빠름.

## BFS 예시

```python
from collections import deque

q = deque([start])
visited = set([start])

while q:
    node = q.popleft()

    for nxt in graph[node]:
        if nxt not in visited:
            visited.add(nxt)
            q.append(nxt)
```

---

# 8. `heapq`

## Import

```python
import heapq
```

## 사용

```python
import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 10)

heapq.heappop(heap)  # 2
```

Python heap은 기본적으로 min-heap.

## 언제 쓰나

가장 작은 값/큰 값 빠르게 꺼내기.

예:

* top-k
* priority queue
* Dijkstra
* streaming smallest/largest

## max-heap처럼 쓰기

```python
heapq.heappush(heap, -value)
largest = -heapq.heappop(heap)
```

---

# 9. `bisect`

## Import

```python
import bisect
```

또는:

```python
from bisect import bisect_left, bisect_right
```

## 사용

```python
from bisect import bisect_left, bisect_right

arr = [1, 3, 5, 7]

bisect_left(arr, 5)   # 2
bisect_right(arr, 5)  # 3
```

## 언제 쓰나

정렬된 배열에서 binary search.

예:

```python
idx = bisect_left(arr, target)
```

## 삽입 위치 찾기

```python
import bisect

arr = [1, 3, 7]
bisect.insort(arr, 5)

arr  # [1, 3, 5, 7]
```

단, insertion 자체는 list shift 때문에 O(N).

---

# 10. `dataclass`

## Import

```python
from dataclasses import dataclass
```

## 사용

```python
from dataclasses import dataclass

@dataclass
class SimulationRun:
    design_id: str
    drag: float
    lift: float
    status: str
```

```python
run = SimulationRun("wing_001", 0.21, 1.32, "ok")
run.drag
```

## 언제 쓰나

구조화된 데이터를 깔끔하게 표현할 때.

코딩테스트에서는 필수는 아니지만, 실무형 문제에서 readable하게 만들고 싶을 때 좋음.

다만 Coderbyte에서는 시간 아끼려고 dict/list로 가는 게 보통 안전함.

---

# 11. `namedtuple`

## Import

```python
from collections import namedtuple
```

## 사용

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y", "z"])

p = Point(1, 2, 3)
p.x  # 1
```

## 언제 쓰나

가벼운 immutable record.

요즘은 보통 `dataclass`를 더 많이 씀.

---

# 12. `numpy.ndarray`

## Import

```python
import numpy as np
```

## 사용

```python
import numpy as np

X = np.array([[1, 2], [3, 4]], dtype=float)

X.shape       # (2, 2)
X.ndim        # 2
X.size        # 4
X.dtype       # float64
```

## 언제 쓰나

숫자 배열, ML/scientific computing.

Coderbyte에서 Neural Concept 스타일이면 매우 중요.

## 자주 쓰는 생성

```python
np.array(data)
np.asarray(data)
np.zeros((N, D))
np.ones((N, D))
np.full((N, D), np.nan)
```

## 자주 쓰는 연산

```python
X.mean(axis=0)
X.std(axis=0)
X.min(axis=0)
X.max(axis=0)
np.sum(mask, axis=0)
```

## masking

```python
mask = np.isfinite(X)
valid = X[mask]
```

주의:

```python
X[mask]
```

는 보통 flatten된 1D 값들을 반환함.

column-wise 통계가 필요하면:

```python
X_clean = np.where(np.isfinite(X), X, np.nan)
means = np.nanmean(X_clean, axis=0)
```

## shape 관련

```python
x.ravel()
x.reshape(-1)
np.stack(list_of_arrays, axis=0)
np.concatenate(list_of_arrays, axis=0)
```

---

# 코딩테스트에서 자주 쓰는 import 세트

실전에서는 대충 이 정도면 충분함.

```python
import math
import heapq
import bisect
import numpy as np

from collections import defaultdict, Counter, deque
```

만약 standard library만 허용이면 `numpy` 제외.

---

# 상황별 선택

## 순서대로 모으기

```python
list
```

## key로 group 만들기

```python
dict
defaultdict
```

## 중복 제거 / 방문 체크

```python
set
```

## 빈도수 세기

```python
Counter
defaultdict(int)
```

## queue / BFS

```python
deque
```

## top-k / priority

```python
heapq
```

## 정렬된 배열 검색

```python
bisect
```

## 숫자 tensor / matrix

```python
numpy.ndarray
```

---

# 너한테 특히 중요한 것

Neural Concept / Coderbyte 대비로는 이 순서로 익숙해지면 좋음.

1. `dict.get()`
2. `defaultdict`
3. `set`
4. `deque`
5. `heapq`
6. `np.asarray`
7. `np.isfinite`
8. boolean masking
9. `axis=0/1`
10. `np.stack` vs `np.concatenate`

특히 오늘 봤을 때 너한테는 `numpy.ndarray`의 shape/mask semantics가 제일 레버리지 큼.

진짜 한 줄로 요약하면:

```python
list/dict/set + defaultdict/deque/heapq + numpy masking
```

이 조합만 탄탄해도 Coderbyte 실무형 문제는 꽤 안정적으로 풀 수 있어.
