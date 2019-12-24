
# Pizza bot (RASA)
A simple chatbot which orders a Pizza for the user by taking their inputs. The bot can perform the usual chitchat and assist user in making their own pizza by asking for their choice crust, veggies, cheese type and meat. The bot then fetches this information from MongoDB and calculates the total amount for the order.

# Files
The trained model gets stored in the models directory.
* Domain.yml contains the intents, entities, actions and templates.
* nlu.md contains the nlu data used for training.
* stories.md contain the conversation flow of the bot. The bot can also handle unhappy paths where the user stops in between conversation.
* actions.py is the actions file where the custom actions are executed. This is where the bot connects to the outside world (MongoDB in this case).

# rasa versions used
rasa-core = 0.12.3
rasa-nlu = 0.13.7

# Train commands
python3 -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue -c policies.yml

python3 -m rasa_nlu.train -c configa.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose

## Run commands
python3 -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml --enable_api -o out.log

python3 -m rasa_core_sdk.endpoint --actions temp
