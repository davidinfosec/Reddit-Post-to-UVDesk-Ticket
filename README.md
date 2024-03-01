# Home IT Ticketing System using Reddit posts

This Python script automates the creation of IT support tickets from Reddit posts in the /r/techsupport subreddit. It fetches posts from a specified RSS feed and creates tickets for each post in an external ticketing system, UVDesk.

There's some quirks with this - I want to be able to run the script and only add new, not duplicates -- but, this is an ongoing project. Feel free to contribute.

Check out the full blog post here: https://davidinfosec.com/2024/03/home-it-support-ticketing-system-revisited/

## Features

- Fetches the latest posts from the /r/techsupport subreddit via RSS.
- Creates tickets in an external ticketing system using post details.
- Handles missing `author` attributes gracefully.
- Detailed logging for troubleshooting ticket creation issues.
![firefox_JjrShJmLqB](https://github.com/davidinfosec/Reddit-Post-to-UVDesk-Ticket/assets/87215831/64c67a93-1287-4bd9-9e62-89c528523d0b)
![firefox_p4Mj3wOzWO](https://github.com/davidinfosec/Reddit-Post-to-UVDesk-Ticket/assets/87215831/7c83f424-3da1-46c2-af04-99ca7f330c55)

## Installation

### Prerequisites

- Python 3.6 or higher.
- `requests` and `feedparser` libraries.

### Setup

1. Clone the repository:

   ```
   git clone https://github.com/davidinfosec/home-it-ticketing-system.git
   ```

2. Navigate to the cloned directory:

   ```
   cd home-it-ticketing-system
   ```

3. Install the required Python libraries:

   ```
   pip install requests feedparser
   ```

## Usage

To run the script, navigate to the script's directory and execute the following command:

```
python reddit2ticket.py
```

The script will automatically fetch posts from the /r/techsupport subreddit RSS feed, create tickets for each post, and print the status of each ticket creation attempt to the console.

## Configuration

Before using the script, you must configure the following variables in the `reddit2ticket.py` file:

- `RSS_FEED_URL`: The URL of the RSS feed for the /r/techsupport subreddit.
- `TICKET_CREATION_URL`: The endpoint URL for creating tickets in your ticketing system.

Optionally, you can customize the `create_ticket` function to include additional headers, cookies, or authentication tokens required by your ticketing system.

## Contributing

Contributions to improve the script are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push your branch and submit a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- Reddit and the /r/techsupport community for providing the RSS feed.
- The developers of the `requests` and `feedparser` libraries for making HTTP requests and parsing RSS feeds easier.
```
