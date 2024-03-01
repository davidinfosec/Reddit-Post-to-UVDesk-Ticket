import requests
import feedparser

# RSS feed URL for the subreddit
# Replace this ticket creation Full-Text RSS URL with the subreddit you'd like to use for your tickets.
RSS_FEED_URL = "https://www.reddit.com/r/techsupport.rss"

# Endpoint URL for creating tickets
# Replace this ticket creation URL with your UVDesk support link.
TICKET_CREATION_URL = "http://172.22.22.32:6744/en/customer/create-ticket/" 


def fetch_reddit_posts():
    """Fetches posts from the Reddit RSS feed."""
    return feedparser.parse(RSS_FEED_URL)

def create_ticket(name, email, ticket_type, subject, message):
    """Creates a ticket using the provided details."""
    payload = {
        'name': name,
        'from': email,
        'type': ticket_type,
        'subject': subject,
        'reply': message,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.post(TICKET_CREATION_URL, data=payload, headers=headers)
    return response

def main():
    """Main function to fetch posts and create tickets."""
    posts = fetch_reddit_posts()
    for post in posts.entries:
        username = getattr(post, 'author', 'UnknownAuthor')
        profile_link = f"https://www.reddit.com/user/{username}"
        subject = post.title
        message = post.summary

        name = username
        email = profile_link  # Using profile link as a placeholder
        ticket_type = "1"  # Placeholder ticket type

        response = create_ticket(name, email, ticket_type, subject, message)
        if response.status_code == 200:
            print(f"Ticket created for {username}")
        else:
            print(f"Failed to create ticket for {username}. Response code: {response.status_code}, Response content: {response.text}")

if __name__ == "__main__":
    main()
