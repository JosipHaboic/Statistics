import random
import numpy
import requests
import json
from binarytree import tree, show, convert
from quantitative_sample import QuantitativeSample
from quantitative_population import QuantitativePopulation
from qualitative_population import QualitativePopulation
from pprint import pprint
from matplotlib import pyplot



def playground1():
    # Lets see stats we get for two outfits from Miller world, one Terran and one Vanu.
    from outfit import Outfit

    REST_ENDPOINT = 'http://census.daybreakgames.com/s:ps2serviceid/get/ps2:v2'
    OUTFIT_QUERY = 'outfit/?alias_lower={}&c:resolve=member_character,member,member_online_status'
    OUTFIT_300S = Outfit(**json.loads(requests.get('{}/{}'.format(REST_ENDPOINT, OUTFIT_QUERY.format('300s'))).text)['outfit_list'][0])
    OUTFIT_DIG = Outfit(**json.loads(requests.get('{}/{}'.format(REST_ENDPOINT, OUTFIT_QUERY.format('dig'))).text)['outfit_list'][0])

    BATTLE_RANKS_300S = [member.battle_rank.value for member in OUTFIT_300S.members]
    BATTLE_RANKS_DIG = [member.battle_rank.value for member in OUTFIT_DIG.members]
    
    QP_300S = QuantitativePopulation(BATTLE_RANKS_300S)
    QP_DIG = QuantitativePopulation(BATTLE_RANKS_DIG)

    pprint(QP_300S.summary)
    pprint(QP_DIG.summary)

# playground1()
