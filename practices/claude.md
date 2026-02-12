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

다음에 오면 **Roman to Integer**부터 이어가고, Medium으로 올라가자! 💪🫡