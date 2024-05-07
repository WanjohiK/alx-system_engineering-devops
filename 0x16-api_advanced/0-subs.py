#!/usr/bin/python3
"""Script that returns the numbers of
subscribers of a subreddit passed to it"""

# Import the 'requests' library to make HTTP requests
import requests

# Define a function called 'number_of_subscribers' that takes a
# 'subreddit' as its parameter


def number_of_subscribers(subreddit):
    """Function that returns the numbers of
    subscribers of a subreddit passed to it"""

    # Construct the API URL with the provided subreddit name
    apiUrl = "https://reddit.com/r/{}/about.json".format(subreddit)

    # Define a user agent to mimic a web browser
    userAgent = "Mozilla/5.0"

    # Send an HTTP GET request to the API with the defined user agent
    response = requests.get(apiUrl, headers={"user-agent": userAgent})

    # Check if the response is successful (status code 200)
    if not response:
        # If the response is not successful, return 0 subscribers
        return 0

    # Parse the JSON response and extract the number of subscribers
    returnVal = response.json().get('data').get('subscribers')

    # Check if 'returnVal' contains a valid number of subscribers
    if returnVal:
        # If valid, return the number of subscribers
        return returnVal
    else:
        # If not valid, return 0 subscribers
        return 0
