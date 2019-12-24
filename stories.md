## story 1
* greet
  - utter_greet
* goodbye
  - utter_goodbye

## goodbye
* goodbye
  - utter_goodbye

## greet
* greet
  - utter_greet

## thankyou
* appraisal_thank_you
    - utter_appraisal_thank_you

## FAQ
* bot_functions_faq OR agent_age_faq OR agent_identity_faq OR agent_health_faq
    - action_faq

## story 2
* greet
    - utter_greet
* bot_functions_faq OR agent_age_faq OR agent_identity_faq OR agent_health_faq
    - action_faq
* goodbye
    - utter_goodbye

## FAQs
* bot_functions_faq OR agent_age_faq OR agent_identity_faq OR agent_health_faq
    - action_faq
* bot_functions_faq OR agent_age_faq OR agent_identity_faq OR agent_health_faq
    - action_faq

## Pizza form affirm
* make_own_pizza
    - make_own_pizza_form
    - form{"name": "make_own_pizza_form"}
    - form{"name": "null"}
    - utter_order_confirmation
* affirm
    - action_order_confirmation

## Pizza form deny
* make_own_pizza
    - make_own_pizza_form
    - form{"name": "make_own_pizza_form"}
    - form{"name": "null"}
    - utter_order_confirmation
* deny
    - action_order_confirmation

## Story 4
* greet
    - utter_greet
* bot_functions_faq OR agent_age_faq OR agent_identity_faq OR agent_health_faq
    - action_faq
* make_own_pizza
    - make_own_pizza_form
    - form{"name": "make_own_pizza_form"}
    - form{"name": "null"}
    - utter_order_confirmation
* affirm
    - action_order_confirmation
* goodbye
    - utter_goodbye

## Story 5
* greet
    - utter_greet
* bot_functions_faq OR agent_age_faq OR agent_identity_faq OR agent_health_faq
    - action_faq
* make_own_pizza
    - make_own_pizza_form
    - form{"name": "make_own_pizza_form"}
    - form{"name": "null"}
    - utter_order_confirmation
* deny
    - action_order_confirmation
* goodbye
    - utter_goodbye

## Story 6
* greet
    - utter_greet
* make_own_pizza
    - make_own_pizza_form
    - form{"name": "make_own_pizza_form"}
    - form{"name": "null"}
    - utter_order_confirmation
* deny
    - action_order_confirmation
* goodbye
    - utter_goodbye

## Story 7
* greet
    - utter_greet
* make_own_pizza
    - make_own_pizza_form
    - form{"name": "make_own_pizza_form"}
    - form{"name": "null"}
    - utter_order_confirmation
* affirm
    - action_order_confirmation
* goodbye
    - utter_goodbye

## curse_bot
* curse_bot
    - utter_curse_bot

## Story 8
* bot_functions_faq OR agent_age_faq OR agent_identity_faq OR agent_health_faq
    - action_faq
* affirm
    - utter_affirm

## Stop while ordering
* make_own_pizza
    - make_own_pizza_form
    - form{"name": "make_own_pizza_form"}
* bot_functions_faq OR agent_age_faq OR agent_identity_faq OR agent_health_faq
    - action_faq
    - make_own_pizza_form
    - form{"name": "null"}
    - utter_order_confirmation
* affirm
    - action_order_confirmation

## Stop while ordering 2
* make_own_pizza
    - make_own_pizza_form
    - form{"name": "make_own_pizza_form"}
* bot_functions_faq OR agent_age_faq OR agent_identity_faq OR agent_health_faq
    - action_faq
    - make_own_pizza_form
    - form{"name": "null"}
    - utter_order_confirmation
* deny
    - action_order_confirmation

## Stop while ordering
* make_own_pizza
    - make_own_pizza_form
    - form{"name": "make_own_pizza_form"}
* stop
    - utter_ask_stop
* affirm
    - action_deactivate_form
    - form{"name": "null"}
    - action_slots_reset
    - utter_stop

## Stop while ordering 2
* make_own_pizza
    - make_own_pizza_form
    - form{"name": "make_own_pizza_form"}
* stop
    - utter_ask_stop
* deny
    - make_own_pizza_form
    - form{"name": "null"}
    - utter_order_confirmation
* affirm
    - action_order_confirmation

## Stop while ordering 3
* make_own_pizza
    - make_own_pizza_form
    - form{"name": "make_own_pizza_form"}
* stop
    - utter_ask_stop
* deny
    - make_own_pizza_form
    - form{"name": "null"}
    - utter_order_confirmation
* deny
    - action_order_confirmation
