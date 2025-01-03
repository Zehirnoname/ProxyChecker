import requests

# Developer and GitHub address
print("Program Developer: Zehir")
print("GitHub: https://github.com/Zehirnoname")

# Function to load proxies
def load_proxies(filename="proxy.txt"):
    """Loads proxies from the proxy.txt file"""
    proxies = []
    try:
        with open(filename, 'r') as file:
            proxies = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"{filename} file not found.")
    return proxies

# Function to test the proxy
def check_proxy(proxy, test_url="http://www.google.com"):
    """Checks if the proxy is working"""
    try:
        # Send an HTTP request to test the proxy
        response = requests.get(test_url, proxies={"http": f"http://{proxy}", "https": f"https://{proxy}"}, timeout=10)
        if response.status_code == 200:
            print(f"Proxy {proxy} is working.")
            return True
        else:
            print(f"Proxy {proxy} is not working. Status Code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Proxy {proxy} is not working. Error: {e}")
        return False

# Function to save live proxies to a file
def save_live_proxies(live_proxies, filename="liveproxy.txt"):
    """Saves the live proxies to the 'liveproxy.txt' file"""
    try:
        with open(filename, 'w') as file:
            for proxy in live_proxies:
                file.write(f"{proxy}\n")
        print(f"{len(live_proxies)} live proxies have been saved to {filename}.")
    except Exception as e:
        print(f"Error saving live proxies: {e}")

# Main function to check proxies
def check_and_save_proxies():
    """Test all proxies and save the working ones"""
    proxies = load_proxies()  # Load proxies
    live_proxies = []  # List to store working proxies

    # Test proxies
    for proxy in proxies:
        if check_proxy(proxy):
            live_proxies.append(proxy)  # Add working proxy to the list

    # Save live proxies to the file
    save_live_proxies(live_proxies)

# Program execution
if __name__ == "__main__":
    check_and_save_proxies()
