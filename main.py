# main.py
#==============================================================================================================

import app_funcs

# app_funcs.set_env_var('BUDDY_LINK_TOKEN', "YOUR_TOKEN)
# Call the function to get the environment variable
access_token = app_funcs.get_user_env_var('BUDDY_LINK_TOKEN')

# Call the function from the imported module
app_funcs.get_facebook_profile(access_token)
app_funcs.list_fb_friends(access_token)

# Fetch and print your profile information and pages
profile = app_funcs.get_my_profile(access_token)
if profile:
    print("Profile:", profile)

pages = app_funcs.get_my_pages(access_token)
if pages:
    print("Pages:", pages)