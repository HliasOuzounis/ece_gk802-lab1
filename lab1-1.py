import requests

def main():
    # 1 get URL
    url = input("Enter a URL: ")
    if not url.startswith("www"):
        url = "www." + url
    if not url.startswith("http"):
        url = "http://" + url
    
    # 2 HTTP request
    with requests.get(url) as response:
        # 3 Print headers
        print(response.headers)
        
        # 4.1 get web server firmware
        server = response.headers.get("Server")
        print(f"Server: {server}" if server else "No server found")
        
        # 4 get cookies
        cookies = response.headers.get("Set-Cookie")
        print("Has cookies" if cookies else "No cookies")
        
        # 5 print cookies
        if cookies:
            print(cookies)
        


if __name__ == "__main__":
    main()