"""
좋습니다! 완전 다른 유형 갑니다.

---

## 문제: Dependency-Aware Task Scheduler

당신은 ML 파이프라인의 **태스크 스케줄러**를 설계하고 있습니다.

각 태스크는 다른 태스크에 **의존성(dependency)**을 가질 수 있습니다. 의존하는 태스크가 모두 완료된 후에만 실행할 수 있습니다.

```python
def schedule(tasks: dict[str, list[str]]) -> list[str]:
    Args:
        tasks: task_id -> list of dependency task_ids
        예시: {"train": ["preprocess", "validate"], 
               "preprocess": ["download"], 
               "validate": ["download"], 
               "download": []}

    Returns:
        실행 가능한 순서로 정렬된 task_id 리스트.
        순환 의존성이 있으면 빈 리스트 [] 반환.
```

### 예시

```
Input:  {"train": ["preprocess", "validate"],
         "preprocess": ["download"],
         "validate": ["download"],
         "download": []}

Output: ["download", "preprocess", "validate", "train"]
        또는 ["download", "validate", "preprocess", "train"]
        (같은 레벨이면 순서 무관)
```

### 순환 의존성 예시

```
Input:  {"A": ["B"], "B": ["C"], "C": ["A"]}
Output: []
```

---

### 이전 문제들과 완전히 다른 점

- 스트리밍이 아니라 **배치 처리**
- deque는 쓸 수도 있지만 역할이 다름
- **그래프 사고**가 필요

---

이전과 같은 규칙입니다. 불명확한 부분이나 가정 먼저, 그 다음 설계를 말로, 마지막에 코드!
"""

from collections import deque

def schedule(tasks: dict[str, list[str]]) -> list[str]:
    """
    Args:
        tasks: task_id -> list of dependency task_ids
        예시: {"train": ["preprocess", "validate"], 
               "preprocess": ["download"], 
               "validate": ["download"], 
               "download": []}
# example:
        reverse: {
            "train": []
            "validate": ["train"],
            "preprocess": ["train"],
            "download": ["validate", preprocess"]
        }
        in_degree = {
            "train": 2,
            "validate": 1,
            "preprocess": 1,
            "download": 0
        }
    """
    q = deque()

    reverse = defaultdict(list)        # dep -> [task1, task2....]
    in_degree = defaultdict(int)     # dep -> number of tasks

    for task, deps in tasks.items():
        # make in_degree map
        in_degree[task] = len(deps)

        # set initial start task
        if len(deps) == 0:
            q.append(task)

        # make reverse map
        for dep in deps:
            reverse[dep].append(task)

    batch_seq = []
    while q:     
        t = q.popleft()
        batch_seq.append(t)
                
        for dep in reverse[t]:
            in_degree[dep] -= 1
            if in_degree[dep] == 0:
                q.append(dep)

    if len(batch_seq) != len(tasks):
        return []

    return batch_seq    

    