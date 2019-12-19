from rasa_core_sdk import Action
from rasa_core_sdk.events import *
from rasa_core.events import UserUtteranceReverted
import requests
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT

class ActionFAQ(Action):
    '''
    All FAQ answers
    '''
    def name(self):
        return 'action_faq'

    def run(self, dispatcher, tracker, domain):
        intent_name = tracker.latest_message['intent'].get('name')
        dispatcher.utter_template('utter_{}'.format(intent_name), tracker)
        return None
