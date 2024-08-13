# API Advanced Project

This project focuses on interacting with the Reddit API using Python. It involves querying data, handling pagination, and processing the results using recursive functions. The primary goal is to strengthen your understanding of API interactions, JSON parsing, and Python scripting.

## Learning Objectives

- How to read API documentation to find the endpoints you’re looking for.
- How to use an API with pagination.
- How to parse JSON results from an API.
- How to make a recursive API call.
- How to sort a dictionary by value.

## Requirements

- **Python Version**: Python 3.4.3
- **Libraries**: `requests`
- Code should follow PEP 8 style guidelines.
- All scripts must be executable.
- No external modules other than `requests` should be used.

## Files

### 0-subs.py

**Function**: `def number_of_subscribers(subreddit):`

- Queries the Reddit API and returns the number of subscribers for a given subreddit.
- Returns `0` if the subreddit is invalid.
- Example usage: 
  ```bash
  $ python3 0-main.py programming

