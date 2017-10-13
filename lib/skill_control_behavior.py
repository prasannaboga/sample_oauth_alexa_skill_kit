from .sample_oauth import SampleOauth
from .helpers import *


# --------------- Functions that control the skill's behavior ------------------ #

def get_welcome_response():
  session_attributes = {}
  card_title = "Hello"
  speech_output = "Welcome to the Oauth example... Ask me."
  reprompt_text = "Oauth example is here I have only one skill"
  should_end_session = False
  return build_response(session_attributes,
                        build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def get_user_info(intent, session):
  session_attributes = {}
  card_title = intent['name']
  should_end_session = False
  reprompt_text = None
  
  sample_oauth = SampleOauth(session['user']['accessToken'])
  response = sample_oauth.get_user_info()
  profile = response.json()
  
  if 'errors' in profile:
    speech_output = "I m going to get your details.. next time..."
  else:
    speech_output = "Name {}, Date of Birth {}, Location {}".format(profile['name'], profile['dob'],
                                                                    profile['location'])
  
  return build_response(session_attributes,
                        build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def update_user_info(intent, session):
  session_attributes = {}
  card_title = intent['name']
  should_end_session = False
  reprompt_text = 'Ask me get latest user info.'
  
  sample_oauth = SampleOauth(session['user']['accessToken'])
  response = sample_oauth.update_user_info()
  if response.json()['success']:
    speech_output = "Updated user details successfully"
  else:
    speech_output = 'Error'
    reprompt_text = 'Ask again to update.'
  
  return build_response(session_attributes,
                        build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
  card_title = "Quiting"
  speech_output = "See you again"
  # Setting this to true ends the session and exits the skill.
  should_end_session = True
  return build_response({}, build_speechlet_response(
    card_title, speech_output, None, should_end_session))
