## Task 2

Write a script that contains the following functionality: given a pandas dataframe with a column that contains the ID for reddit comments, return a filtered version of this dataframe with only
comments that have not been removed from reddit by the authors. Use the https://github.com/pushshift/api to send a request that returns you information about
the IDs. 
For example this request: 'https://api.pushshift.io/reddit/comment/search?ids=dlrezc8,dlrawgw,dlrhbkq' returns a json with information about three IDS. In this
case all IDs have been removed. 
This can be seen because the information in the field 'link_id' contains [removed].

An example dataframe is uploaded, called cmv_example_thread.tsv
