import pokebase as pb #pokemon data urls
import requests #access the url
import json #convert url data to json

def get_poke_json(pokename):
    api_input1 = pb.pokemon_species(str(pokename)).url
    response1 = requests.get(api_input1).json()
    input1 = response1['varieties']['is_default'==True]['pokemon']['url']
    response2 = requests.get(input1).json()
    return response2

         

def poke_stats_dict(response):
    stat_dict = {"hp":0,"attack":0,"defense":0,"special-attack":0,"special-defense":0,"speed":0}
    try:    
        for i in response['stats']:
            stat_dict[i['stat']['name']] = i['base_stat']
        total_stat = sum(stat_dict.values())
        stat_dict['base stat total'] = total_stat
        return stat_dict
    except:
        pass

def poke_sprite_response(response):
    sprite_url = response['sprites']['front_default']
    sprite_response = requests.get(sprite_url)
    return sprite_response

def poke_type(response):
    try:
        ret=[]
        for i in response['types']:
            ret.append(i['type']['name'])
        final=" & ".join(ret)
        return final
    except:
        pass

get_poke_json('deoxys')
