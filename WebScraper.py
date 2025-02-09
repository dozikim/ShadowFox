import requests
from bs4 import BeautifulSoup

# Ask the user to input the URL
url = input("Enter the URL of the website you want to scrape: ")

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all text content from the page
    text_content = soup.get_text(strip=True)

    # Extract all links (href attributes)
    links = soup.find_all('a', href=True)
    print("\nLinks:")
    for link in links:
        print(link['href'])

    # Extract all image URLs (src attributes)
    images = soup.find_all('img', src=True)
    print("\nImage URLs:")
    for img in images:
        print(img['src'])

    # Extract all JavaScript files (src attributes for script tags)
    scripts = soup.find_all('script', src=True)
    print("\nJavaScript URLs:")
    for script in scripts:
        print(script['src'])

    # Extract all styles (for inline or external CSS)
    styles = soup.find_all('link', rel='stylesheet', href=True)
    print("\nCSS URLs:")
    for style in styles:
        print(style['href'])

    # Print all text content of the webpage (can be long for large pages)
    print("\nText Content:")
    print(text_content)

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
