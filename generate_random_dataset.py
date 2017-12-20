import random
import json

with open('example.dataset','w') as f:
    f.write(json.dumps([random.randint(0,100) for x in range(32)]))

