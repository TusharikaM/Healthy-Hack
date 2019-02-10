import json
import boto3
BUCKET = 'cal-count'
KEY = 'foodDetails.json'
  
    # --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
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
    
    # --------------- Functions that control the skill's behavior ------------------

    
def get_welcome_response(userID):
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Sure! Let me help you track your calorie intake"
    should_end_session = False
    reprompt_text = "Do you still want to use Healthy Hack?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def get_help_response(userID): 
    client = boto3.client('s3',
                       aws_access_key_id='AKIAIYFP36BB2GLSMQJQ',
                       aws_secret_access_key='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'
                     )
    result = client.get_object(Bucket=BUCKET, Key=KEY)
    # Read the object (not compressed):
    text = result["Body"].read()
    jsonFileContent = json.loads(text)
    cal = jsonFileContent['user']['total_calories_consumed']
    status="Yout total calories consumptionis is "+str(cal)+" calories"
    
    session_attributes = {}
    card_title = "Help"
    speech_output = status 
    should_end_session = True
    reprompt_text = "Are you still there? Come back. Let me count your calories"
    return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, reprompt_text, should_end_session))

# coke method
def get_coke_count_response():
    client = boto3.client('s3',
                       aws_access_key_id='AKIAIYFP36BB2GLSMQJQ',
                       aws_secret_access_key='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'
                     )
    result = client.get_object(Bucket=BUCKET, Key=KEY)
    # Read the object (not compressed):
    text = result["Body"].read()
    jsonFileContent = json.loads(text)
    count = jsonFileContent['coke']['count']
    status="hmmmmmmmmmmm! You have consumed "+str(count)+" coke cans"
    
    session_attributes = {}
    card_title = "Help"
    speech_output = status 
    should_end_session = True
    reprompt_text = "Are you still there? Come back. Let me count your calories"
    return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, reprompt_text, should_end_session))
    
# dorito method

def get_doritos_count_response():
    client = boto3.client('s3',
                       aws_access_key_id='AKIAIYFP36BB2GLSMQJQ',
                       aws_secret_access_key='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'
                     )
    result = client.get_object(Bucket=BUCKET, Key=KEY)
    # Read the object (not compressed):
    text = result["Body"].read()
    jsonFileContent = json.loads(text)
    count = jsonFileContent['doritos']['count']
    status="You have consumed "+str(count)+" dorito pack"
    
    session_attributes = {}
    card_title = "Help"
    speech_output = status 
    should_end_session = True
    reprompt_text = "Are you still there? Come back. Let me count your calories"
    return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, reprompt_text, should_end_session))
    
# protein_bar method

def get_pbar_count_response():
    client = boto3.client('s3',
                       aws_access_key_id='AKIAIYFP36BB2GLSMQJQ',
                       aws_secret_access_key='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'
                     )
    result = client.get_object(Bucket=BUCKET, Key=KEY)
    # Read the object (not compressed):
    text = result["Body"].read()
    jsonFileContent = json.loads(text)
    count = jsonFileContent['protein_bar']['count']
    status="hmmmmm.. protein bars huh..You have consumed "+str(count)+" protein bars!"
    
    session_attributes = {}
    card_title = "Help"
    speech_output = status 
    should_end_session = True
    reprompt_text = "Are you still there?"
    return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, reprompt_text, should_end_session))    
    
# fsnack method

def get_fsnack_count_response():
    client = boto3.client('s3',
                       aws_access_key_id='AKIAIYFP36BB2GLSMQJQ',
                       aws_secret_access_key='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'
                     )
    result = client.get_object(Bucket=BUCKET, Key=KEY)
    # Read the object (not compressed):
    text = result["Body"].read()
    jsonFileContent = json.loads(text)
    count = jsonFileContent['fruit_snack']['count']
    status="You have consumed "+str(count)+" fruit snacks!"
    
    session_attributes = {}
    card_title = "Help"
    speech_output = status 
    should_end_session = True
    reprompt_text = "Are you still there?"
    return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, reprompt_text, should_end_session))        
# lays method

def get_lays_count_response():
    client = boto3.client('s3',
                       aws_access_key_id='AKIAIYFP36BB2GLSMQJQ',
                       aws_secret_access_key='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'
                     )
    result = client.get_object(Bucket=BUCKET, Key=KEY)
    # Read the object (not compressed):
    text = result["Body"].read()
    jsonFileContent = json.loads(text)
    count = jsonFileContent['lays']['count']
    status="hmmmmm.. potato chips huh..You have consumed "+str(count)+" lays!"
    
    session_attributes = {}
    card_title = "Help"
    speech_output = status 
    should_end_session = True
    reprompt_text = "Are you still there?"
    return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, reprompt_text, should_end_session))    
    
# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    userID = session['user']['userId']

    # Dispatch to your skill's launch
    return get_welcome_response(userID)

    #input any method to be called on launch with the application


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    userID = session['user']['userId']
    if intent_name == "test":
        return get_help_response(userID)
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request(userID)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response(userID)
    elif intent_name == "coke":
        return get_coke_count_response()
    elif intent_name == "doritos":
        return get_doritos_count_response() 
    elif intent_name == "protein_bar":
        return get_pbar_count_response()
    elif intent_name == "lays":
        return get_lays_count_response()    
    elif intent_name == "fruit_snack":
        return get_fsnack_count_response()        
    else:
         raise ValueError("Invalid intent")        


#-----------------Main Handler---------------
def lambda_handler(event, context):
    
    if ('session' in event):
        print("event.session.application.applicationId=" +
              event['session']['application']['applicationId'])
        if event['session']['new']:
            on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
        if ('request' in event):                       
            if event['request']['type'] == "LaunchRequest":
                return on_launch(event['request'], event['session'])
            elif event['request']['type'] == "IntentRequest":
                return on_intent(event['request'], event['session'])
            elif event['request']['type'] == "SessionEndedRequest":
                return on_session_ended(event['request'], event['session'])