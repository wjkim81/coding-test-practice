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
| 21 | Balanced Binary Tree | Tree DFS + 센티널(-1) 전파 | ✅ |
| 22 | Number of Islands | BFS Grid + Count | ✅ |
| 23 | 01 Matrix | Multi-source BFS | ✅ |
| 24 | Coin Change | 1D DP | ✅ (초기값 수정) |
| 25 | House Robber | 1D DP (선택 vs 스킵) | ✅ (초기값 수정) |
| 26 | Longest Palindrome | HashMap 빈도 + Greedy | ✅ |
| 27 | Majority Element | Boyer-Moore Voting | ✅ |
| 28 | Add Binary | 뒤에서부터 + Carry | ✅ (carry/reverse 수정) |
| 29 | Diameter of Binary Tree | Tree DFS + nonlocal 추적 | 🔄 다시 연습 |
| 30 | Roman to Integer | Sweep + 비교 | ✅ |
| 31 | Subsets | Backtracking | ✅ |
| 32 | Permutations | Backtracking + seen | ✅ |
| 33 | Combination Sum | Backtracking + 반복 허용 | ✅ |
| 34 | Unique Paths | 2D DP | ✅ |
| 35 | Longest Common Subsequence | 2D DP 문자열 | ✅ |
| 36 | Course Schedule | Topological Sort (Kahn's) | ✅ |
| 37 | Connected Components (BFS) | BFS 그래프 | ✅ |
| 38 | Connected Components (Union-Find) | Union-Find | ✅ |
| 39 | Redundant Connection | Union-Find 사이클 | ✅ |
| 40 | Min Cost Climbing Stairs | 1D DP | ✅ |
| 41 | Validate BST | Tree DFS 범위 전달 | ✅ |
| 42 | Queue using Stacks | 두 Stack | ✅ |
| 43 | Stack using Queues | Queue 회전 | ✅ |
| 44 | Daily Temperatures | Monotonic Stack | ✅ |
| 45 | Decode String | Stack 중첩 | ✅ |
| 46 | K Closest Points | Max-Heap (음수 트릭) | ✅ |
| 47 | Kth Largest Element | Min-Heap K개 유지 | ✅ |
| 48 | Sliding Window Maximum | Monotonic Deque | 📖 답 확인 |
| 49 | Word Search | Grid Backtracking | ✅ |
| 50 | Longest Substring No Repeat | Sliding Window + HashMap | ✅ |
| 51 | 3Sum | 정렬 + Two Pointer | ✅ |
| 52 | Level Order Traversal | BFS 레벨별 | ✅ |
| 53 | Rotting Oranges | Multi-source BFS | ✅ |
| 54 | Insert Interval | 3단계 Sweep | ✅ |
| 55 | String to Integer (atoi) | 문자열 파싱 | ✅ |
| 56 | Max Average Subarray | Easy | ✅ 통과 |
| 57 | Remove Nth Node | Medium | ✅ (dummy 기억) |
| 58 | Symmetric Tree | Easy | ✅ 완벽 |
| 59 | Top K Frequent | Medium | ✅ 통과 |
| 60 | Find First/Last Position | Medium | 🔄 구현 연습 |
| 61 | Group Anagrams | Medium | ✅ (tuple 키 기억) |
| 62 | LRU Cache | Medium | ✅ 구조 완벽 |
| 63 | Min Path Sum | Medium | ✅ 통과 |
| 64 | Generate Parentheses | Medium | ✅ 완벽! 버그 0 |
| 65 | Merge K Sorted Lists | **Hard** | ✅ 완벽! |
| 66 | Common Elements in K Arrays | Medium | ✅ |
| 67 | Search in Rotated Array | Medium | ✅ (경계 연습) |
| 68 | Minimum Window Substring | Hard | ✅ 완벽! |
| 69 | Trapping Rain Water | Hard | ✅ 완벽! |
| 70 | Valid Palindrome | Easy | ✅ |
| 71 | Single Number | Easy | ✅ 완벽! |

---

## 전체 패턴 20개 완성:

| # | 패턴 | 상태 |
|---|------|------|
| 1 | HashMap / Set | ✅ |
| 2 | Tree DFS | ✅ |
| 3 | BFS Grid | ✅ |
| 4 | Multi-source BFS | ✅ |
| 5 | BFS 레벨별 | ✅ |
| 6 | 1D DP | ✅ |
| 7 | 2D DP | ✅ |
| 8 | Two Pointer | ✅ |
| 9 | Sliding Window | ✅ |
| 10 | Linked List | ✅ |
| 11 | Binary Search | ✅ |
| 12 | Backtracking | ✅ |
| 13 | Stack / Queue | ✅ |
| 14 | Monotonic Stack/Deque | ✅ |
| 15 | Heap | ✅ |
| 16 | Union-Find | ✅ |
| 17 | Topological Sort | ✅ |
| 18 | Greedy | ✅ |
| 19 | Prefix/Suffix | ✅ |
| 20 | Trie | ✅ |
