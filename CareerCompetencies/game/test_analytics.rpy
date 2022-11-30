init python in test_analytics:
    #import requests
    from ga4mp import GtagMP
    from typing import *
    credentials = {"API_SECRET" : "EX72bIC7To2jjCff1cOp4Q", "MEASUREMENT_ID" : "G-LB2EXTGGNZ", "CLIENT_ID" : "118135719013870375861"}
    ga = GtagMP(measurement_id = "MEASUREMENT_ID", api_secret = "API_SECRET", client_id="CLIENT_ID")
    events = [ ]
    test = ""

    def test_event():
        example_event = ga.create_new_event(name="custom_event")
        # Event parameters can be set one at a time...
        example_event.set_event_param(name="game_start", value="1")
        #my_dict = {"clicked" : "button"}
        # ...or via a loop.
        #for key, value in my_dict.items():
            #example_event.set_event_param(name=key, value=value)
        event_type = 'new_custom_event'
        event_parameters = {'parameter_key_1': 'parameter_1', 'parameter_key_2': 'parameter_2'}
        event = {'name': event_type, 'params': event_parameters }
        print(f"first : {events}" )
        events.append(event)
        print(f"second : {events}" )
        test = list[dict]
        print(type(test))
        print(type(events))
        ga.send(events)

        # player = example_event.create_new_item(item_id="p_1", item_name="New Player 1")
        # player.set_parameter("test", 5)

        # example_event.add_item_to_event(player)
        # ga.store.set_user_property(name ="First Player", value="yes")

        # event_list = [example_event]
    
        # ga.send(events=event_list)
  
