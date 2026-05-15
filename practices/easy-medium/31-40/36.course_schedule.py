from typing import List
from collections import deque, defaultdict

def course_schedule(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list) # reversemap
    in_degrees = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degrees[course] += 1


    q = deque()
    for i, count in enumerate(in_degrees):
        if count == 0:
            q.append(i)

    visited = 0
    while q:
        course = q.popleft()
        visited += 1
        for next_course in graph[course]:
            in_degrees[next_course] -= 1
            if in_degrees[next_course] == 0:
                q.append(next_course)

    return visited == numCourses


