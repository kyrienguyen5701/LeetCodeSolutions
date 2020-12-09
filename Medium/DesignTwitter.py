'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user
and is able to see the 10 most recent tweets in the user's news feed. Your design should support
the following methods:
postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed.
Each item in the news feed must be posted by users who the user followed or by the user herself.
Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
'''

from collections import defaultdict
from copy import deepcopy

class TwitterUser:
    def __init__(self):
        # self._id = id
        self.tweets = []
        self.followees = defaultdict(list)

class Twitter:

    def __init__(self):
        self.users = defaultdict(TwitterUser)
        self.count = 0
        

    def postTweet(self, userID, tweetID):
        self.users[userID].tweets.insert(0, {
            'id': tweetID,
            'order': self.count
        })
        if len(self.users[userID].tweets) >= 10:
            self.users[userID].tweets = self.users[userID].tweets[:10]
        self.count += 1
    
    def getNewsFeed(self, userID):
        newsfeed = deepcopy(self.users[userID].tweets)
        for followee in self.users[userID].followees.values():
            newsfeed += followee.tweets
        newsfeed.sort(reverse=True, key=lambda tweet: tweet['order'])
        return [tweet['id'] for tweet in newsfeed][:10]
        
    def follow(self, followerID, followeeID):
        if followeeID != followerID and followeeID not in self.users[followerID].followees.keys():
            self.users[followerID].followees[followeeID] = self.users[followeeID]

    def unfollow(self, followerID, followeeID):
        if followeeID in self.users[followerID].followees:
            del self.users[followerID].followees[followeeID]

'''
Runtime: 104ms - 24.86%
Memory: 19.6MB - 56.15%
'''

'''
Comment: I really enjoy solving this problem as
it is a practical problem that helps me improve
my systematic design and optimization skills. I
did come up with a way to optimize getNewsFeed
using Heap Queue, but my implementation of using
dictionary does not allow me to do so (yet?).
'''