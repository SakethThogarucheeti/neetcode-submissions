import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.userFollowList = defaultdict(set)
        self.userTweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        heapq.heappush_max(self.userTweets[userId], (self.time, tweetId))
        self.userTweets[userId] = heapq.nlargest(10, self.userTweets[userId])
        print("postTweet:",self.userTweets[userId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        print("getNewsFeed logs: ", userId)
        follows = self.userFollowList[userId]
        allUsers = follows.union(set([userId]))
        noOfTweetsToFetch = 10
        print(follows, allUsers)

        newsFeed = []

        for user in allUsers:
            recentTweets = heapq.nlargest(10, self.userTweets[user])
            print("recenttweets", recentTweets, self.userTweets[user])
            for time, tweetId in recentTweets:
                heapq.heappush_max(newsFeed, (time, user, tweetId))
            newsFeed = heapq.nlargest(10,newsFeed)
            print("newsfeed", newsFeed)

        res = []
        while newsFeed:
            time, user, tweetId = heapq.heappop_max(newsFeed)
            res.append(tweetId)

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollowList[followerId]:
            self.userFollowList[followerId].remove(followeeId)
