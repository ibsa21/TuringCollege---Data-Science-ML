from sys import intern
import time
from typing import Deque, NamedTuple, DefaultDict, Dict, List, Optional
from collections import defaultdict, deque
from itertools import islice
from heapq import merge

# type annotation
User = str
Text = str

# build the data structure
Post = NamedTuple('Post', [('timestamp', float), ('user', User),('text', Text)])
posts:Deque() = deque()                 #form newest to oldest
user_posts:DefaultDict[User, deque] = defaultdict(deque)

# follower and following
following:DefaultDict[User, List[User]] = defaultdict(set)
followers: DefaultDict[User, List[User]] = defaultdict(set)

def post_message(user:User, text: Text, timestamp:float = None):
    user = intern(user)
    timestamp = timestamp or time.time()
    post = Post(user, text, timestamp)
    posts.appendleft(post)
    user_posts[user].appendleft(post)

def follow(user: User, followed_user:User)->None:
    user, followed_user = intern(user), intern(followed_user)
    following[user].add(followed_user)
    followers[followed_user].add(user)

def post_by_user(user:User, limit:Optional[int]= None)->List[Post]:
    return list(islice(user_posts[user], limit))

def post_for_user(user:User, limit:Optional[int] = None) ->List[Post]:
    relevant_post = list(merge(*[user_posts[followed_user] 
                                for followed_user in following[user]], reverse=True))
    return list(islice(relevant_post, limit))

def search_post(phrase: str, limit: Optional[int] = None)->List[Post]:
    return islice((post for post in posts if phrase in post.text), limit)