# -*- coding: utf-8 -*-

from __future__ import print_function
import logging
import json
from lib.skill_control_behavior import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
  print(" ==== event.session ==== ")
  print(json.dumps(event['session']))
  print(" ==== event.request ==== ")
  print(json.dumps(event['request']))
  
  if event['session']['new']:
    on_session_started({'requestId': event['request']['requestId']},
                       event['session'])
  
  if event['request']['type'] == "LaunchRequest":
    return on_launch(event['request'], event['session'])
  elif event['request']['type'] == "IntentRequest":
    on_intent_response = on_intent(event['request'], event['session'])
    print(" == on_intent_response == ")
    print(json.dumps(on_intent_response))
    return on_intent_response
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
  elif intent_name == "UpdateUserInfo":
    return update_user_info(intent, session)
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
