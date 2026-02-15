# Easy~Medium Practice with Claude

[Link](https://claude.ai/chat/1b367a51-6c54-44f7-9b9c-cc4ccd8f5d6e)

## Day 1 (20문제)

| # | 문제 | 패턴 | 상태 |
|---|------|------|------|
| 1 | Two Sum | HashMap | ✅ |
| 2 | Valid Parentheses | Stack | ✅ |
| 3 | Merge Intervals | Sort + Sweep | ✅ |
| 4 | Best Time to Buy/Sell Stock | Min 추적 Sweep | ✅ |
| 5 | Maximum Subarray | Kadane's DP | ✅ |
| 6 | Contains Duplicate | Set | ✅ (add 빠뜨림) |
| 7 | Product of Array Except Self | Prefix/Suffix | ✅ |
| 8 | Move Zeroes | Two Pointer | ✅ |
| 9 | Climbing Stairs | 1D DP (피보나치) | ✅ |
| 10 | Linked List Cycle | Fast & Slow | ✅ |
| 11 | Reverse Linked List | 3 Pointer | 🔄 다시 연습 |
| 12 | Middle of Linked List | Fast & Slow | ✅ |
| 13 | Max Depth of Tree | Tree DFS | ✅ |
| 14 | Invert Binary Tree | Tree DFS | ✅ |
| 15 | Same Tree | Tree DFS 동시 재귀 | ✅ |
| 16 | Subtree of Another Tree | DFS + 헬퍼 | 🔄 base case 연습 |
| 17 | LCA of BST | BST 값 비교 | ✅ |
| 18 | Valid Anagram | HashMap 빈도 | ✅ |
| 19 | Binary Search | 이분탐색 | ✅ |
| 20 | Flood Fill | BFS Grid | ✅ |

## Day 2 (10문제)

| # | 문제 | 패턴 | 상태 |
|---|------|------|------|
| 21 | Balanced Binary Tree | Tree DFS + 센티널(-1) 전파 | ✅ |
| 22 | Number of Islands | BFS Grid + Count | ✅ |
| 23 | 01 Matrix | Multi-source BFS | ✅ |
| 24 | Coin Change | 1D DP | ✅ (초기값 수정) |
| 25 | House Robber | 1D DP (선택 vs 스킵) | ✅ (초기값 수정) |
| 26 | Longest Palindrome | HashMap 빈도 + Greedy | ✅ |
| 27 | Majority Element | Boyer-Moore Voting | ✅ |
| 28 | Add Binary | 뒤에서부터 + Carry | ✅ (carry/reverse 수정) |
| 29 | Diameter of Binary Tree | Tree DFS + nonlocal 추적 | 🔄 다시 연습 |
| 30 | Roman to Integer | — | 📋 다음 시작 |

---

## 커버한 패턴 요약

| 패턴 | 문제 수 | 숙련도 |
|------|---------|--------|
| HashMap / Set | 5 | ⭐⭐⭐ |
| Tree DFS | 7 | ⭐⭐⭐ |
| BFS Grid | 3 | ⭐⭐⭐ |
| 1D DP | 4 | ⭐⭐ |
| Two Pointer | 2 | ⭐⭐ |
| Linked List | 3 | ⭐⭐ |
| Binary Search | 1 | ⭐⭐ |
| Sort + Sweep | 1 | ⭐⭐ |
| Prefix/Suffix | 1 | ⭐⭐ |
| Stack | 1 | ⭐⭐ |
| Greedy | 2 | ⭐⭐ |

## 아직 안 푼 핵심 패턴

| 패턴 | 대표 문제 | 우선순위 |
|------|----------|----------|
| Sliding Window 심화 | Minimum Window Substring | 🔴 높음 |
| Backtracking | Subsets, Permutations | 🔴 높음 |
| Topological Sort | Course Schedule | 🟡 중간 |
| 2D DP | Unique Paths | 🟡 중간 |
| Heap | Merge K Sorted Lists | 🟡 중간 |
| Trie | Word Search | 🟢 낮음 |
| Union-Find | Connected Components | 🟢 낮음 |

## 🔄 다시 연습 필요

| 문제 | 이유 |
|------|------|
| Reverse Linked List | 포인터 3개 순서 헷갈림 |
| Subtree of Another Tree | base case 순서 |
| Diameter of Binary Tree | nonlocal 패턴 새로움 |

---

| # | 문제 | 패턴 | 상태 |
|---|------|------|------|
| 30 | Roman to Integer | Sweep + 비교 | ✅ |
| 31 | Subsets | Backtracking | ✅ |
| 32 | Permutations | Backtracking + seen | ✅ |
| 33 | Combination Sum | Backtracking + 반복 허용 | ✅ |

**Backtracking 패턴 핵심 — 이것만 기억해:**

```
넣기 → 재귀 → 빼기(pop)
```

---

쉬고 다음에 오면:
1. 🔄 Backtracking 3문제 안 보고 다시 풀기
2. 2D DP (Unique Paths) 진입
3. Balanced Binary Tree 복습

---

오 LeetCode에서도 빡세게 했네! 👏

체크된 거 기준으로 정리할게:

---

## Array (10/11 완료)

| 문제 | 우리 세션 | 새로 푼 거 |
|------|----------|-----------|
| Remove Duplicates from Sorted | | ✅ 새로 풀음 |
| Best Time to Buy and Sell Stock | ✅ | |
| Rotate Array | | ✅ 새로 풀음 |
| Contains Duplicate | ✅ | |
| Single Number | | ✅ 새로 풀음 |
| Intersection of Two Arrays II | | ✅ 새로 풀음 |
| Plus One | | ✅ 새로 풀음 |
| Move Zeroes | ✅ | |
| Two Sum | ✅ | |
| Valid Sudoku | | ☐ 아직 |
| Rotate Image | ✅ | |

## Strings (8/8 완료) 🎉

| 문제 | 우리 세션 | 새로 푼 거 |
|------|----------|-----------|
| Reverse String | | ✅ |
| Reverse Integer | | ✅ |
| First Unique Character | | ✅ |
| Valid Anagram | ✅ | |
| Valid Palindrome | | ✅ |
| String to Integer (atoi) | | ✅ |
| Implement strStr() | | ✅ |
| Longest Common Prefix | | ✅ |

## Linked List (6/7 완료)

| 문제 | 우리 세션 | 새로 푼 거 |
|------|----------|-----------|
| Delete Node in a Linked List | | ✅ |
| Remove Nth Node From End | | ✅ |
| Reverse Linked List | 🔄 | ✅ 복습함! |
| Merge Two Sorted Lists | | ✅ |
| Palindrome Linked List | | ✅ |
| Linked List Cycle | ✅ | |

## Trees (5/5 완료) 🎉

| 문제 | 우리 세션 | 새로 푼 거 |
|------|----------|-----------|
| Maximum Depth of Binary Tree | ✅ | |
| Validate Binary Search Tree | | ✅ |
| Symmetric Tree | | ✅ |
| Binary Tree Level Order Traversal | | ✅ |
| Convert Sorted Array to BST | | ✅ |

---

## 오늘 요약

| 카테고리 | 상태 |
|----------|------|
| 우리 세션과 겹침 | ~8문제 (복습 효과 ✅) |
| 익숙하지만 새로 풀음 | ~10문제 |
| 완전 새로 본 거 | ~6문제 |
| **오늘 LeetCode 총** | **~24문제** 😱 |

---

# 📌 이 세션 코테 연습 정리

## 1️⃣ Array / Two Pointers / Sweep

| 문제                           | 패턴                   |
| ---------------------------- | -------------------- |
| Two Sum                      | HashMap              |
| Best Time to Buy/Sell Stock  | Min 추적               |
| Move Zeroes                  | Two Pointer          |
| Rotate Array                 | Reverse 3-step       |
| Container With Most Water    | Two Pointer Greedy   |
| Merge Sorted Array           | Backward Two Pointer |
| Missing Number               | Sum / XOR            |
| Product of Array Except Self | Prefix/Suffix        |
| Plus One                     | Carry 처리             |
| Single Number                | XOR                  |
| Intersection of Arrays       | Counter              |
| Pascal's Triangle            | 2D 생성                |

**현재 숙련도:** ⭐⭐⭐
→ 배열 기본기 충분히 안정권

---

## 2️⃣ String / Parsing / Sweep

| 문제                            | 패턴                 |
| ----------------------------- | ------------------ |
| Reverse String                | Two Pointer        |
| Reverse Integer               | Digit 처리           |
| First Unique Character        | HashMap            |
| Valid Anagram                 | Counter            |
| Valid Palindrome              | Two Pointer        |
| String to Integer (atoi)      | Parsing + Overflow |
| strStr()                      | Naive / KMP        |
| Longest Common Prefix         | Vertical scan      |
| Longest Palindromic Substring | Center Expansion   |
| Zigzag Conversion             | Row simulation     |
| Roman to Integer              | Sweep 비교           |
| Integer to Roman              | Greedy             |
| Regex Matching                | 2D DP              |

**현재 숙련도:** ⭐⭐~⭐⭐⭐
→ 문자열 처리 + 파싱 상당히 많이 경험함

---

## 3️⃣ Linked List

| 문제                     | 패턴            |
| ---------------------- | ------------- |
| Reverse Linked List    | 3 pointer     |
| Remove Nth From End    | Fast-Slow     |
| Delete Node            | 값 복사          |
| Merge Two Sorted Lists | Pointer merge |
| Palindrome Linked List | Reverse half  |
| Linked List Cycle      | Fast-Slow     |

**현재 숙련도:** ⭐⭐
→ 기본 패턴은 거의 커버됨

---

## 4️⃣ Tree / DFS / BFS

| 문제                          | 패턴               |
| --------------------------- | ---------------- |
| Max Depth                   | DFS              |
| Invert Tree                 | DFS              |
| Same Tree                   | 동시 DFS           |
| Balanced Tree               | Sentinel         |
| Diameter                    | DFS + global     |
| Validate BST                | Range 전달         |
| Symmetric Tree              | Mirror DFS       |
| Level Order                 | BFS              |
| Convert Sorted Array to BST | Divide & Conquer |

**현재 숙련도:** ⭐⭐⭐
→ 트리 기본 패턴 상당히 안정적

---

## 5️⃣ Graph / Grid

| 문제                | 패턴               |
| ----------------- | ---------------- |
| Flood Fill        | BFS              |
| Number of Islands | BFS              |
| 01 Matrix         | Multi-source BFS |

**현재 숙련도:** ⭐⭐~⭐⭐⭐

---

## 6️⃣ Dynamic Programming

| 문제                | 패턴     |
| ----------------- | ------ |
| Climbing Stairs   | 1D DP  |
| House Robber      | 선택/스킵  |
| Coin Change       | 최소값 DP |
| Maximum Subarray  | Kadane |
| Regex Matching    | 2D DP  |
| Unique Paths (예정) | 2D DP  |

**현재 숙련도:** ⭐⭐
→ 1D는 안정, 2D는 확장 중

---

## 7️⃣ Bit Manipulation

| 문제               | 패턴         |
| ---------------- | ---------- |
| Hamming Weight   | n&(n-1)    |
| Hamming Distance | XOR        |
| Reverse Bits     | Shift      |
| Power of Three   | Math Trick |
| Missing Number   | XOR        |

**현재 숙련도:** ⭐⭐
→ 기본 비트 영역 상당히 커버

---

# 🔥 종합 패턴 커버 현황

| 영역                | 상태    |
| ----------------- | ----- |
| Array 기본          | 안정권   |
| Two Pointer       | 안정권   |
| HashMap           | 안정권   |
| Tree DFS/BFS      | 안정권   |
| Linked List       | 안정권   |
| Bit               | 안정권   |
| 1D DP             | 안정권   |
| 2D DP             | 확장 중  |
| Backtracking      | 진입 완료 |
| Sliding Window 심화 | 아직 부족 |
| Topological Sort  | 아직    |
| Heap              | 아직    |
| Union-Find        | 아직    |

---

# 📊 지금 레벨을 냉정하게 말하면

* Easy → 거의 자동
* Medium → 50~60% 즉시 가능
* Hard → 구조는 이해, 즉시 구현은 아직 어려움

그리고 이게 70~80문제 구간의 정상 위치입니다.

---

# 🔥 제일 중요한 포인트

당신이 지금 느끼는:

> “처음 보면 못 푼다”

이건 패턴이 부족해서가 아니라
**패턴 연결 속도가 아직 완전히 자동화되지 않았기 때문**입니다.

이미 커버한 영역은 생각보다 엄청 많습니다.

---

원하면 내가 지금 상태 기준으로
**“빅테크 코테까지 남은 진짜 핵심 영역만 압축 로드맵”** 정리해줄까요?
