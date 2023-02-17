## Task 1

Your first task is to try to crawl one page from the subreddit ChangeMyView.
This subreddit allows people to engage in discussions about different controversial topics. The idea is that a person posts a start argument (OP = original pos) in which their opinion is explained 
and backed up with reasons. Then other people will answer to this post with counter arguments, trying to change the view of the person of the OP. If a person convinced the person of the OP to change their view, they will receive
a delta score. 
Our goal would be to crawl several threads from this reddit, all posts together with the user names and potentially other useful information.
We interested in getting the flair (https://www.reddit.com/r/modguide/wiki/flairs/, ika a pre-defined label that can be added to a comment by a user.
Flairs can look in different ways but we are especially interested in those, that label as post as a rule violation. Change my view as a defined set of rule agains which people should not violate.
One example of a rule is for example "Rule 2: Rude/Hostile Comment": Don't be rude or hostile to other users...". One can for example retrieve pages with a certain flair, entering the followin search expression
in the search field: flair_name:"Removed - Submission Rule C".

For a first start you should try to just crawl one page and try to have a look which type of information (post, user ID, time stamp) you can retrieve and how.
Then we can continue to find out how to crawl pages with certain flairs. 
Let's start with the following page:
https://www.reddit.com/r/changemyview/comments/kna7u4/cmv_i_dont_understand_the_debate_between_pro_and/
The page has deleted users, flairs and archived content so it should be a good test case.
You can have a look at the reddit API for crawling:
https://praw.readthedocs.io/en/stable/
But you are also free to do it in any way you find working. 



