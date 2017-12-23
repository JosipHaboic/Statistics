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
from outfit import Outfit











## LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST LAST
# REST_ENDPOINT = 'http://census.daybreakgames.com/s:ps2serviceid/get/ps2:v2'
# OUTFIT_QUERY = 'outfit/?alias_lower={}&c:resolve=member_character,member,member_online_status'
# # OUTFIT_300S = Outfit(**json.loads(requests.get('{}/{}'.format(REST_ENDPOINT, OUTFIT_QUERY.format('300s'))).text)['outfit_list'][0])
# OUTFIT_DIG = Outfit(**json.loads(requests.get('{}/{}'.format(REST_ENDPOINT, OUTFIT_QUERY.format('dig'))).text)['outfit_list'][0])

# # BATTLE_RANKS_300S = [member.battle_rank.value for member in OUTFIT_300S.members]
# BATTLE_RANKS_DIG = [member.battle_rank.value for member in OUTFIT_DIG.members]

# # QP_300S = sorted(QuantitativePopulation(BATTLE_RANKS_300S))
# QP_DIG = sorted(QuantitativePopulation(BATTLE_RANKS_DIG))

# pyplot.plot(QP_DIG, 'k-')
# pyplot.grid()
# pyplot.show()

