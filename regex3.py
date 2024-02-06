

import re

text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''

pattern = 'FY(\d{4} Q[1-4])'

matches = re.findall(pattern,text)

print(matches)

