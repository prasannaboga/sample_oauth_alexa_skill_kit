# -*- coding: utf-8 -*-
from __future__ import print_function


def handler(event, context):
  print("event.session.application.applicationId=" +
        event['session']['application']['applicationId'])
  
  if event['session']['new']:
    on_session_started({'requestId': event['request']['requestId']},
                       event['session'])
  
  if event['request']['type'] == "LaunchRequest":
    return on_launch(event['request'], event['session'])
  elif event['request']['type'] == "IntentRequest":
    return on_intent(event['request'], event['session'])
  elif event['request']['type'] == "SessionEndedRequest":
    return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
  """ Called when the session starts """
  print("on_session_started requestId=" + session_started_request['requestId'] + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
  """ Called when the user launches the skill without specifying what they want """
  print("on_launch requestId=" + launch_request['requestId'] + ", sessionId=" + session['sessionId'])
  # Dispatch to your skill's launch
  return get_welcome_response()


def on_intent(intent_request, session):
  """ Called when the user specifies an intent for this skill """
  print("on_intent requestId=" + intent_request['requestId'] + ", sessionId=" + session['sessionId'])
  
  intent = intent_request['intent']
  intent_name = intent_request['intent']['name']
  
  # Dispatch to your skill's intent handlers
  if intent_name == "Oauth":
    return get_user_info(intent, session)
  elif intent_name == "GetUserInfo":
    return get_user_info(intent, session)
  elif intent_name == "AMAZON.HelpIntent":
    return get_welcome_response()
  elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
    return handle_session_end_request()
  else:
    raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
  """ Called when the user ends the session. Is not called when the skill returns should_end_session=true """
  print("on_session_ended requestId=" + session_ended_request['requestId'] + ", sessionId=" + session['sessionId'])
  # add cleanup logic here


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
  
  speech_output = "I m going to get your details.. next time..."
  
  return build_response(session_attributes,
                        build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
  card_title = "Quiting"
  speech_output = "See you again"
  # Setting this to true ends the session and exits the skill.
  should_end_session = True
  return build_response({}, build_speechlet_response(
    card_title, speech_output, None, should_end_session))


# --------------- Helpers that build all of the responses ---------------------- #

def build_speechlet_response(title, output, reprompt_text, should_end_session):
  return {
    'outputSpeech': {
      'type': 'PlainText',
      'text': output
    },
    'card': {
      'type': 'Simple',
      'title': 'SessionSpeechlet - ' + title,
      'content': 'SessionSpeechlet - ' + output
    },
    'reprompt': {
      'outputSpeech': {
        'type': 'PlainText',
        'text': reprompt_text
      }
    },
    'shouldEndSession': should_end_session
  }


def build_response(session_attributes, speechlet_response):
  return {
    'version': '1.0',
    'sessionAttributes': session_attributes,
    'response': speechlet_response
  }
