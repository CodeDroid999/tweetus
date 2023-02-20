import requests

def login_to_twitter(username, password):
    session = requests.Session()
    login_url = "https://twitter.com/login"
    # Get the authenticity_token from the login page
    # Get the authenticity_token from the login page
    resp = session.get(login_url)
    authenticity_token = resp.text.split('authenticity_token" value="')[1].split('"')[0]

    # Prepare the login data and headers
    login_data = {
        "session[username_or_email]": username,
        "session[password]": password,
        "authenticity_token": authenticity_token
    }
    headers = {
        "Referer": "https://twitter.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    # Send a post request to the login endpoint with the login data
    resp = session.post("https://twitter.com/sessions", data=login_data, headers=headers)

    # Check if the login was successful
    if resp.status_code == 200:
        return True
    else:
        return False
