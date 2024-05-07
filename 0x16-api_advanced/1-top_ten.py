#!/usr/bin/python3
"""function that queries the Reddit API and
prints the titles of the first 10 hot posts
listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
    listed for a given subreddit."""

    apiUrl = "https://reddit.com/r/{}/hot.json".format(subreddit)

    # Define a user agent to mimic a web browser
    userAgent = "Mozilla/5.0"
    # Set the limit to 10 for fetching the top 10 posts

    limits = 10

    # Send an HTTP GET request to the API with the defined user agent
    response = requests.get(
            apiUrl, headers={"user-agent": userAgent},
            params={"limit": limits})

    # Check if response is not successful (status code other than 200)
    if not response:
        # Print 'None' and return if the response is not successful
        print('None')
        return

    # Parse the JSON response
    response = response.json()

    # Extract the list of posts from the response
    list_obj = response['data']['children']

    # Iterate through the list of posts and print their titles
    for obj in list_obj:
        print(obj['data']['title'])

    # End the function
    return
