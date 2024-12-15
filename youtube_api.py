from googleapiclient.discovery import build

# use pip install google-api-python-client in terminal to get API

api_key = "AIzaSyA51rPuo9cvxTta8y1G0zPf3sjct0-lah8"
youtube = build('youtube', 'v3', developerKey=api_key)

