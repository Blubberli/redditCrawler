## new tasks

### Extract Info for Comment ID 

Given a comment ID from reddit extract the following information:
- text
- whether it has been deleted
- post id
- post title
- author
- author id
- parent Id
- subreddit name
- flair
return the information as  a dictionary


### Extract Info for list as Comment IDS and save to dataframe

- given a list of comment IDs extract the information with the function above for each ID
- store all information in a pandas data frame and save it as a csv to "outpath"


### Extract all posts from a given thread

given a post id extract all comments posted under the thread
this function can just return comment IDs, all other info we can extract from the other method

### Extract meta discourse from CMV

extract comments and threads from the following subreddit: https://www.reddit.com/r/ideasforcmv/



### Annotation:


You will be presented with text snippets of a larger argument. The overall argument expresses a major claim / position. You will see a snippet of an argument together with such a major claim or position. Your Goal is to select "yes" if you believe the position matches the snippet / was the position that was expressed with the argument the snippet was taken from. Select "no" if you think they do not match. Keep in mind that this is not simply about matching topics, e.g. the overall topic can be immigration but there are many different major claims for the same topic. Rate the difficulty of the example on a scale from easy (1) to difficult (5).

Example 1:

"Off the top of my head , I cannot think of a single artist that progressed as quick and as vast as they did in as little time , while still holding onto what made their music uniquely theirs . There are very few artists that can reach a point where they can create both [ I Wanna Hold Your Hand ] ( and [ Tomorrow Never Knows ] ( very different songs , I admit , and perhaps not perfectly exemplary of their body of work at large ) in a way that is . . . natural . They progressed as opposed to mutated . Along with that comes the fact that bands like Radiohead would not have existed at the time ( that is to say , experimental bands that still achieved large mainstream appeal ) and would arguably never had achieved mainstream success or even existed were it not for the Beatles ."

Claim: 
"The constant updating on Nelson Mandela's condition is ghoulish and distasteful" 
matches ? No

Claim:
The author is of the view that Beatles are the trailblazers of what many bands enjoy the success and fame for. The kind of music they released was akin to much of the popular music that existed during their time and they were still able to make it big and inspire other big names today.
matches? Yes


Example 2: 

"In Holland , no one is illegal until the procedure continues . As long as the procedure continues , those people are legally considered to be lawfully residents of the country ’ s territory . Those , living for 12 years in Holland , had lived there legally for those 12 years , so where is the problem ? These people cannot do anything meanwhile ."

Claim:
"immigration can bring positive change because the author has observed restoration and improvement in their home town,"
matches ? No

Claim:
"immigrants should be allowed to work in the country while the immigration bureaucracy is still pending because many people are often unable to work or forced into poor living conditions until the process is complete,
matches? Yes

You will get this annotation task as a google form, such that you can just click trough the items.
