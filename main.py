import praw
from credentials import *

reddit2 = praw.Reddit(
    client_id=c_id,
    client_secret=c_secret,
    password=pw,
    user_agent=ua,
    username=uname,
)

reddit = praw.Reddit(
    client_id=c_id2,
    client_secret=c_secret2,
    password=pw2,
    user_agent=ua2,
    username=uname2,
)

#Print Old Subreddits
print("----------------------------------------")
print("Current Subreddits")
print("----------------------------------------")
for subreddit in reddit2.user.subreddits(limit=None):
    print(str(subreddit))

subs_to_copy = []

for subreddit in reddit.user.subreddits(limit=None):
    subs_to_copy.append(str(subreddit))

print(subs_to_copy)
eingabe = input("Do you want to join all of those subreddits? Y/N: ")

if(eingabe.lower() == "y"):
  for subs in subs_to_copy:
      reddit2.subreddit(str(subs)).subscribe()

  #Print New Subreddits
  print("----------------------------------------")
  print("New Subreddits after joining")
  print("----------------------------------------")
  for subreddit in reddit2.user.subreddits(limit=None):
      print(str(subreddit))

  print("----------------------------------------")
  print("Subs you joined:")
  print("----------------------------------------")
  print(subs_to_copy)
else:
  print("Aborted task")