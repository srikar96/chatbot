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

## menu request
* request_menu
    - utter_request_menu

## story 2
* greet
    - utter_greet
* bot_functions_faq OR agent_age_faq OR agent_identity_faq OR agent_health_faq
    - action_faq
* goodbye
    - utter_goodbye

## story 3
* greet
    - utter_greet
* bot_functions_faq OR agent_age_faq OR agent_identity_faq OR agent_health_faq
    - action_faq
* request_menu
    - utter_request_menu
* goodbye
    - utter_goodbye

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
