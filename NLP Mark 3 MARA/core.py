import yaml
import actions
import random

domain_file_address='./domain.yml'


def intent_extractor(data):
    intent=data['intent']['name']
    arr=[str(intent)]
    if len(data['entities'])!=0:
        entity_name=data['entities'][0]['entity']
        entity_value=data['entities'][0]['value']
        arr.append(entity_name)
        arr.append(entity_value)
    return arr

def domain_parse(address):
    with open(address,'r') as file_descriptor:
        domain=yaml.load(file_descriptor, Loader=yaml.FullLoader)    
    return domain
domain=domain_parse(domain_file_address)
actions.slot_data=domain['slots']

def get_response(parsed_message,arr):
    data=intent_extractor(parsed_message)
    intent=data[0]
    print(intent)
    if len(data)!=1 :
        actions.tracker.update_slot(data[1],data[2])
    elif intent in arr:
        print('Intent: '+intent)
    elif len(data)==1:
        list=domain['templates']['utter_ask_keywords']
        response=list[int(random.random()*(len(list)-1))]
        return response
    flag=0
    utter=''
    action=''
    for i in domain['intents']:
        if(i==intent): 
            utter='utter_'+intent
            action='action_'+intent
            break
        flag=1

   
    for i in domain['actions']:
        
        if(i==utter):
            list=domain['templates'][utter]
            response=list[int(random.random()*(len(list)-1))]
            return response
        elif(i==action):
            for j in actions.obj_arr:
                
                if(action==j.name()):
                    return j.run()
 
    
    
        



    
