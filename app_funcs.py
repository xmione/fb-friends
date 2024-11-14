# app_funcs.py
#==============================================================================================================

import os
import platform
import facebook
import requests
import winreg

BASE_URL = 'https://graph.facebook.com/v14.0'

import os
import platform

def set_env_var(env_var, env_var_value):
    # Set for current session
    os.environ[env_var] = env_var_value

    if platform.system() == 'Windows':
        # Set User-level environment variable
        os.system(f'setx {env_var} "{env_var_value}"')
        print(f"{env_var} has been set at User level. Please restart your terminal to see the changes.")
    else:
        # Append export command to shell profile for macOS/Linux
        shell_profile = os.path.expanduser('~/.bashrc')  # Or ~/.zshrc for zsh users
        with open(shell_profile, 'a') as file:
            file.write(f'\nexport {env_var}="{env_var_value}"\n')
        print(f"{env_var} has been set at User level. Please restart your terminal to see the changes.")

def get_user_env_var(env_var):
    try:
        # Open the registry key for the User environment variables
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment")
        
        # Try to get the value of the environment variable
        value, regtype = winreg.QueryValueEx(reg_key, env_var)
        
        # Close the registry key
        winreg.CloseKey(reg_key)
        
        return value
    except FileNotFoundError:
        raise KeyError(f"The environment variable '{env_var}' is not set.")
    except Exception as e:
        raise e

# Usage
try:
    token = get_user_env_var('BUDDY_LINK_TOKEN')
    # for testing only because it is dangerous to print your token
    #print(f"Token: {token}")
except KeyError as e:
    print(e)

def get_facebook_profile(access_token):
    """
    Fetch and display Facebook profile information.

    :param access_token: str: Facebook Graph API access token
    """
    try:
        # Initialize the Graph API
        graph = facebook.GraphAPI(access_token)
        
        # Fetch profile information
        profile = graph.get_object('me', fields='id,name')
        
        # Print profile information
        print(f"ID: {profile['id']}")
        print(f"Name: {profile['name']}")
    
    except facebook.GraphAPIError as e:
        print(f"Graph API error: {e}")

def list_fb_friends(access_token):
    # Initialize the Graph API
    graph = facebook.GraphAPI(access_token)

    # Fetch friends list
    friends = graph.get_connections(id='me', connection_name='friends')

    # Print friends list
    if 'data' in friends:
        for friend in friends['data']:
            print(friend['name'])
    else:
        print("No friends found or no friends have authorized the app.")

# Example function to get basic profile information
def get_my_profile(access_token):
    url = f"{BASE_URL}/me?access_token={access_token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching profile:", response.json())
        return None

# Example function to get the pages you manage
def get_my_pages(access_token):
    url = f"{BASE_URL}/me/accounts?access_token={access_token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching pages:", response.json())
        return None
