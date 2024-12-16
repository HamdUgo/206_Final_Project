from tikapi import TikAPI, ValidationException, ResponseException
import json

API_KEY = 'BzUf0VvqpyhrPNjcREqVAOyp1sPsArvrqWyKSVxffYDPP7sW'
api = TikAPI(API_KEY)

def trending_post_data():
    try:
        response = api.public.explore(
        session_id='0',
        country='us'
    )

        print(response.json())

    except ValidationException as e:
        print(e, e.field)

    except ResponseException as e:
        print(e, e.response.status_code)

trending_post_data()

