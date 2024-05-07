#!/usr/bin/python3
""" Recursively  Returns a list containing the titles
of all hot articles for a given subreddit."""

# Import the 'get' function from the 'requests' library
from requests import get

# Define the base URL for Reddit
REDDIT = "https://www.reddit.com/"
# Define a custom user agent for the HTTP request headers
HEADERS = {'user-agent': 'my-app/0.0.1'}


# recursive function that retrieves the titles of hot articles from a subreddit
def recurse(subreddit, hot_list=[], after=""):
    """
    Returns a list containing the titles of all
    hot articles for a given subreddit."""
    # Check if there are no more articles to fetch (after is None)
    if after is None:
        # Return the accumulated 'hot_list'
        return hot_list

    # Construct the URL to fetch hot articles from the specified subreddit
    url = REDDIT + "r/{}/hot/.json".format(subreddit)

    # Define queryparams  for the request, including the 'limit' and 'after'
    params = {
        'limit': 100,  # Fetch up to 100 articles per request
        'after': after  # Use 'after' to paginate through articles
    }

    # Send an HTTP GET request to the Reddit API
    # with the defined headers and parameters
    r = get(url, headers=HEADERS, params=params, allow_redirects=False)

    # Check if the HTTP request was not successful (status code other than 200)
    if r.status_code != 200:
        return None

    # Try to parse the JSON response
    try:
        js = r.json()
    except ValueError:
        return None

    # Try to extract data, 'after', and 'children' from the JSON response
    try:
        data = js.get("data")
        after = data.get("after")
        children = data.get("children")

        # Iterate through the children and append the titles to the 'hot_list'
        for child in children:
            post = child.get("data")
            hot_list.append(post.get("title"))

    except Exception:
        return None

    # Recursively call the 'recurse' function to fetch more articles
    return recurse(subreddit, hot_list, after)
