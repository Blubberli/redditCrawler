import pandas as pd
import requests
import timeit

# ids is the data-fullname in the HTML source code
df = pd.DataFrame(
    {'ids': ['dlrezc8', 'dlrawgw', 'dlrhbkq']})


# call request several times


# input is a dataframe with a column "ids"
# request called multiple times
def check_remove(df):
    # get the ids
    ids = df['ids']
    # initialize empty columns for the data and body
    df['json'] = ''
    df['body'] = ''
    # link to be used to retrieve the api request
    link = "https://api.pushshift.io/reddit/comment/search?ids="
    # loop through the ids
    for i, id in enumerate(ids):
        # get the json
        response = requests.get("".join((link, id)))
        # insert the retrieved data into the dataframe
        df['json'][i] = response.json()
        df['body'][i] = response.json()['data'][0]['body']
    # filter the data that has a "removed" body
    filtered_df = df[df['body'] != '[removed]']
    print("The original data has a length of:" + str(len(df)))
    print("The filtered data has a length of: " + str(len(filtered_df)))

    return filtered_df


start = timeit.default_timer()
check_remove(df)
stop = timeit.default_timer()
print('Time: ', stop - start)


# faster

def check_remove1(df):
    ids = df['ids']
    # initialize empty columns for the data and body
    df['json'] = ''
    df['body'] = ''
    # link to be used to retrieve the api request
    link = "https://api.pushshift.io/reddit/comment/search?ids="
    ids = ",".join(ids)

    response = requests.get("".join((link, ids))).json()
    for i, data in enumerate(response['data']):
        df['json'][i] = data
        df['body'][i] = data['body']
    # filter the data that has a "removed" body
    filtered_df = df[df['body'] != '[removed]']
    print("The original data has a length of:" + str(len(df)))
    print("The filtered data has a length of: " + str(len(filtered_df)))


# test
start = timeit.default_timer()
check_remove1(df)
stop = timeit.default_timer()
print('Time: ', stop - start)
