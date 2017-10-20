from .sample_oauth import SampleOauth
from .helpers import *


# --------------- Functions that control the skill's behavior ------------------ #

def get_welcome_response():
  session_attributes = {}
  reprompt_text = "Oauth example is here I have only two skill"
  should_end_session = False
  text_response = card_response = {}
  text_response['title'] = card_response['title'] = "Welcome to the Oauth example..."
  text_response['content'] = card_response['content'] = "Welcome to the Oauth example... Ask me..."
  card_response['type'] = "Standard"
  card_response['image'] = {
    'smallImageUrl': "https://cdn.tutsplus.com/net/uploads/2013/07/oauth-retina-preview.jpg",
    'largeImageUrl': "https://cdn.tutsplus.com/net/uploads/2013/07/oauth-retina-preview.jpg"
  }
  return build_response(session_attributes,
                        build_speechlet_response(text_response, card_response, reprompt_text, should_end_session))


def get_user_info(intent, session):
  session_attributes = {}
  should_end_session = False
  reprompt_text = None
  text_response = {'title': intent['name']}
  card_response = {'type': 'Simple', 'title': intent['name']}
  
  sample_oauth = SampleOauth(session['user'].get('accessToken'))
  response = sample_oauth.get_user_info()
  profile = response.json()
  
  if 'errors' in profile:
    speech_output = "I m going to get your details.. next time..."
  else:
    speech_output = "Name {}\n Date of Birth {}\n Location {}".format(profile['name'], profile['dob'],
                                                                      profile['location'])
  
  text_response['content'] = speech_output
  
  if 'slots' in intent:
    if 'value' in intent['slots']['display']:
      if intent['slots']['display']['value'].lower() == 'standard':
        card_response['text'] = speech_output
        card_response['type'] = 'Standard'
        card_response['image'] = {
          'smallImageUrl': profile['small_avatar'],
          'largeImageUrl': profile['large_avatar']
        }
      elif intent['slots']['display']['value'].lower() == 'link account':
        card_response = {'type': "LinkAccount"}
    else:
      card_response['content'] = speech_output
  
  return build_response(session_attributes,
                        build_speechlet_response(text_response, card_response, reprompt_text, should_end_session))


def update_user_info(intent, session):
  session_attributes = {}
  should_end_session = False
  reprompt_text = 'Ask me get latest user info.'
  text_response = {'title': intent['name']}
  card_response = {'type': 'Simple', 'title': intent['name']}
  
  sample_oauth = SampleOauth(session['user'].get('accessToken'))
  response = sample_oauth.update_user_info().json()
  if 'errors' in response:
    speech_output = 'Error {}'.format(', '.join(response['errors']))
    reprompt_text = '{}. Ask again to update.'.format(', '.join(response['errors']))
  else:
    speech_output = "Updated user details successfully"

  text_response['content'] = card_response['content'] = speech_output
  return build_response(session_attributes,
                        build_speechlet_response(text_response, card_response, reprompt_text, should_end_session))


def handle_session_end_request():
  text_response = card_response = {}
  text_response['title'] = card_response['title'] = "Quiting"
  text_response['content'] = card_response['content'] = "See you again"
  card_response['type'] = 'Simple'
  # Setting this to true ends the session and exits the skill.
  should_end_session = True
  return build_response({}, build_speechlet_response(text_response, card_response, None, should_end_session))
