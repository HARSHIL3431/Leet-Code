from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        wordSet = set(wordList)
        queue = deque([(beginWord, 1)])

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]

                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord, level + 1))

        return 0