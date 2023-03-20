import pandas as pd
import requests
import timeit

# ids is the data-fullname in the HTML source code
df = pd.read_table("cmv_example_thread.tsv")


def check_remove(df):
    ids = df['id']
    # initialize empty columns for the data and body
    df['link_id'] = ''
    # link to be used to retrieve the api request
    link = "https://api.pushshift.io/reddit/comment/search?ids="
    ids = ",".join(ids)

    response = requests.get("".join((link, ids))).json()

    for i, data in enumerate(response['data']):
        df['link_id'][i] = data['link_id']
    print(df)
    # filter the data that has a "removed" body
    filtered_df = df[df['link_id'] != '[removed]']
    print("The original data has a length of:" + str(len(df)-1))
    print("The filtered data has a length of: " + str(len(filtered_df)-1))
    return filtered_df


# test
start = timeit.default_timer()
check_remove(df)
stop = timeit.default_timer()
print('Time: ', stop - start)
