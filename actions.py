from rasa_core_sdk import Action
from rasa_core_sdk.events import *
from rasa_core.events import UserUtteranceReverted
import requests
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from bson.json_util import dumps
import pymongo as pm

client = pm.MongoClient("mongodb://localhost:27017/")
db = client['pizza']
col1 = db['sizep']
col2 = db['crust']
col3 = db['veggies']
col4 = db['meat']
col5 = db['cheese']

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

class MakeOwnPizzaForm(FormAction):
    '''
    Appointment DATE and booking_time details
    '''
    def name(self):
       return "make_own_pizza_form"

    @staticmethod
    def required_slots(tracker):
        if ((tracker.get_slot('pizza_type') == 'veg') or (tracker.get_slot('pizza_type') == 'vegetarian')):
            return ['pizza_type', 'pizza_size', 'crust', 'toppings_veggies', 'toppings_cheese']
        else:
            return ['pizza_type', 'pizza_size', 'crust', 'toppings_veggies', 'toppings_meat', 'toppings_cheese']

    # def slot_mapping(self):
    #    return {"doc_id": self.from_entity(entity="doc_id"),
    #             "booking_time": self.from_entity(entity="booking_time")}

    def validate(self, dispatcher, tracker, domain):

        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        for slot, value in slot_values.items():
            if slot == 'pizza_type':
                if value not in ['veg', 'non veg']:
                    dispatcher.utter_message('I didn\'t get that. Please select veg or no veg.')
                    slot_values[slot] = None
            elif slot == 'pizza_size':
                data1 = [i['type'] for i in col1.find({},{'_id':0, 'type':1})]
                if value not in data1:
                    dispatcher.utter_message('Please select a valid response')
                    slot_values[slot] = None

        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def request_next_slot(self, dispatcher, tracker, domain):
        '''
        Request the next slot and utter template if needed,
        else return None
        '''

        for slot in self.required_slots(tracker):
            if self._should_request_slot(tracker, slot):
                logger.debug("Request next slot '{}'".format(slot))
                if slot == 'pizza_type':
                    buttons_pizza_type = []
                    for i in ['veg','non veg']:
                        buttons_pizza_type.append({"title": i, "payload": "/inform"})
                    dispatcher.utter_button_message('Let\'s begin.\nPlease select a a pizza type: ', buttons_pizza_type)
                elif slot == 'pizza_size':
                    buttons_pizza_size = []
                    dat = col1.find({},{'_id':0, 'type':1})
                    for i in dat:
                        buttons_pizza_size.append({"title": i['type'], "payload": "/inform"})
                    dispatcher.utter_button_message('Please select a size for your pizza: ', buttons_pizza_size)
                elif slot == 'crust':
                    buttons_crust = []
                    dat = col2.find({},{'_id':0, 'type':1})
                    for i in dat:
                        buttons_crust.append({"title": i['type'], "payload": "/inform"})
                    dispatcher.utter_button_message('Please select a crust: ', buttons_crust)
                elif slot == 'toppings_veggies':
                    buttons_toppings_veggies = []
                    # file = open('toppings_veggies.txt', 'r')
                    file = col3.find({},{'_id':0, 'type':1})
                    for i in file:
                        buttons_toppings_veggies.append({"title": i['type'], "payload": "/inform"})
                    dispatcher.utter_button_message('Now, select your veggies: ', buttons_toppings_veggies)
                    file.close()
                elif slot == 'toppings_meat':
                    buttons_toppings_meat = []
                    # file = open('toppings_meat.txt', 'r')
                    file = col4.find({},{'_id':0, 'type':1})
                    for i in file:
                        buttons_toppings_meat.append({"title": i['type'], "payload": "/inform"})
                    dispatcher.utter_button_message('Select meat: ', buttons_toppings_meat)
                    file.close()
                elif slot == 'toppings_cheese':
                    buttons_toppings_cheese = []
                    # file = open('toppings_cheese.txt', 'r')
                    file = col5.find({},{'_id':0, 'type':1})
                    for i in file:
                        buttons_toppings_cheese.append({"title": i['type'], "payload": "/inform"})
                    dispatcher.utter_button_message('Last thing, what type of cheese do you want?: ', buttons_toppings_cheese)
                    file.close()

                return [SlotSet(REQUESTED_SLOT, slot)]

        logger.debug("No slots left to request")
        return None

    def submit(self, dispatcher, tracker, domain):

        type = tracker.get_slot('pizza_type')
        if type == 'veg' or type == 'vegetarian':
            size = tracker.get_slot('pizza_size')
            crust = tracker.get_slot('crust')
            veggies = tracker.get_slot('toppings_veggies')
            cheese = tracker.get_slot('toppings_cheese')

            price_size = col1.find_one({'type': size},{'_id':0, 'price':1})['price']
            price_crust = col2.find_one({'type': crust},{'_id':0, 'price':1})['price']
            price_veggies = 0
            price_cheese = 0
            for val in veggies:
                price_veggies += col3.find_one({'type': val},{'_id':0, 'price':1})['price']
            for val in cheese:
                price_cheese += col5.find_one({'type': val},{'_id':0, 'price':1})['price']

            tot_price = price_size*price_crust + price_veggies + price_cheese
            dispatcher.utter_message('Here is your order:\nSize: {}\nCrust: {}\nVeggies: {}\nCheese: {}'.format(size, crust, veggies, cheese))
            dispatcher.utter_message('Your bill is: ${}'.format(tot_price))
        else:
            size = tracker.get_slot('pizza_size')
            crust = tracker.get_slot('crust')
            veggies = tracker.get_slot('toppings_veggies')
            meat = tracker.get_slot('toppings_meat')
            cheese = tracker.get_slot('toppings_cheese')

            price_size = col1.find_one({'type': size},{'_id':0, 'price':1})['price']
            price_crust = col2.find_one({'type': crust},{'_id':0, 'price':1})['price']
            price_veggies = 0
            price_cheese = 0
            price_meat = 0
            for val in veggies:
                price_veggies += col3.find_one({'type': val},{'_id':0, 'price':1})['price']
            for val in meat:
                price_meat += col4.find_one({'type': val},{'_id':0, 'price':1})['price']
            for val in cheese:
                price_cheese += col5.find_one({'type': val},{'_id':0, 'price':1})['price']

            tot_price = price_size*price_crust + price_veggies + price_cheese + price_meat
            dispatcher.utter_message('Here is your order:\nSize: {}\nCrust: {}\nVeggies: {}\nMeat: {}\nCheese: {}'.format(size, crust, veggies, meat, cheese))
            dispatcher.utter_message('Your bill is: ${}'.format(tot_price))
        # dispatcher.utter_message(size)
        # dispatcher.utter_message(crust)
        # dispatcher.utter_message(veggies)
        # dispatcher.utter_message(meat)
        # dispatcher.utter_message(cheese)

        # return [SlotSet(val, None) for val in ['pizza_size', 'crust', 'toppings_veggies', 'toppings_meat', 'toppings_cheese']]
        return []

class ActionOrderConfirmation(Action):
    '''
    Order confirmation
    '''
    def name(self):
        return 'action_order_confirmation'

    def run(self, dispatcher, tracker, domain):
        confirm = tracker.latest_message['intent'].get('name')

        if confirm == 'affirm':
            dispatcher.utter_message('You\'re all set!\nThank you for placing an order with us!')
            return [SlotSet(val, None) for val in ['pizza_type', 'pizza_size', 'crust', 'toppings_veggies', 'toppings_meat', 'toppings_cheese']]
        elif confirm == 'deny':
            dispatcher.utter_message('Okay, I won\'t place the order.\nI hope you come back soon!')
            return [SlotSet(val, None) for val in ['pizza_type', 'pizza_size', 'crust', 'toppings_veggies', 'toppings_meat', 'toppings_cheese']]
