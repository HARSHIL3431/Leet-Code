import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int):
        res = []
        heap = []

        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                time, tweetId = self.tweetMap[followee][-1]
                idx = len(self.tweetMap[followee]) - 1
                heapq.heappush(heap, (-time, tweetId, followee, idx))

        while heap and len(res) < 10:
            time, tweetId, user, idx = heapq.heappop(heap)
            res.append(tweetId)

            if idx > 0:
                time, tweetId = self.tweetMap[user][idx-1]
                heapq.heappush(heap, (-time, tweetId, user, idx-1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId] and followeeId != followerId:
            self.followMap[followerId].remove(followeeId)