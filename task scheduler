class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        frequencyDict = [0]*26
        offset = ord('A')
        for i in range(len(tasks)):
            frequencyDict[ord(tasks[i])-offset] += 1
        print(frequencyDict)
        maxFreq = max(frequencyDict)
        repeatition = frequencyDict.count(maxFreq)
        return max(len(tasks), (maxFreq - 1)*(n + 1) + repeatition) 
