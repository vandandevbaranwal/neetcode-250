# Pattern: Greedy + Math Formula — calculate idle slots needed for most frequent task
# Trigger: "schedule tasks with cooldown" = most frequent task dictates minimum time

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        maxf = max(count)          # frequency of most common task
        maxCount = 0
        for i in count:
            maxCount += 1 if i == maxf else 0   # how many tasks share that max frequency

        # formula: (maxf - 1) groups of size (n+1), plus maxCount tasks at the end
        # this accounts for the mandatory cooldown gaps around the most frequent task
        time = (maxf - 1) * (n + 1) + maxCount

        # if there are enough other tasks to fill gaps, no idle time needed
        # answer is just max of calculated time or total tasks
        return max(len(tasks), time)