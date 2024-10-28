
import requests
from bs4 import BeautifulSoup

print("Script started")

# Step 1: Fetch the webpage content
url = 'https://docs.python.org/3/tutorial/index.html'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the webpage content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Step 3: Extract specific information
    # Find all list items in the tutorial section
    tutorials = soup.select('.toctree-l2 a')  # Select all anchor tags under second-level list items

    # Step 4: Store the extracted data
    extracted_tutorials = []

    for tutorial in tutorials:
        title = tutorial.get_text(strip=True)
        link = tutorial['href']  # Get the tutorial link
        extracted_tutorials.append({'title': title, 'link': link})

    # Step 5: Output the extracted data
    if extracted_tutorials:  # Check if any tutorials were extracted
        for tutorial in extracted_tutorials:
            print(f"Tutorial Title: {tutorial['title']}, Link: {tutorial['link']}")
    else:
        print("No tutorials found.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

print("Script finished")


