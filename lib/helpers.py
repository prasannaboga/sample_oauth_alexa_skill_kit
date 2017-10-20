# --------------- Helpers that build all of the responses ---------------------- #
def build_speechlet_response(text_response, card_response, reprompt_text, should_end_session, directives = []):
  
  response = {
    'outputSpeech': {
      'type': 'PlainText',
      'text': text_response['content']
    },
    'card': card_response,
    'reprompt': {
      'outputSpeech': {
        'type': 'PlainText',
        'text': reprompt_text
      }
    },
    'shouldEndSession': should_end_session,
    'directives': directives
  }

  return response


def build_response(session_attributes, speechlet_response):
  return {
    'version': '1.0',
    'sessionAttributes': session_attributes,
    'response': speechlet_response
  }
