from typing import List
import queue

class Solution:
    # N - length of wordList
    # L - length of longest str
    # time O(N^2*L)
    # space O(N)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = [False]*len(wordList)
        wordQueue = queue.Queue()
        wordQueue.put([beginWord,1])
        while not wordQueue.empty():
            word,transformationCount = wordQueue.get()
            if word == endWord: return transformationCount
            
            for i in range(len(wordList)):
                if (not visited[i]) and self.isAdjacent(wordList[i],word):
                    wordQueue.put([wordList[i],transformationCount+1])
                    visited[i] = True
        return 0

    def isAdjacent(self, strA, strB):
        count = 0

        if len(strB)>len(strA):
            strA, strB = strB,strA
        for i in range(len(strA)):
            if i >= len(strB) or strA[i]!=strB[i]:
                count+=1
                if count ==2:
                    return False
        
        return count == 1
    
import unittest
class Test0127(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]),5)

unittest.main()
