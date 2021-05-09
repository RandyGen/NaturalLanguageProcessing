import json
import re
import pprint

path = 'eu.json'

data= ''
result = {}

with open(path, 'r') as f:
    for line in f:
        data += line

pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
templete = re.findall(pattern, data, re.MULTILINE + re.DOTALL)

pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
result = dict(re.findall(pattern, templete[0], re.MULTILINE + re.DOTALL))

pattern = r'\'{2,5}'
result_rm = {k: re.sub(pattern, '', v) for k, v in result.items()}

pattern = r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]'
result_rm2 = {k: re.sub(pattern, r'\1', v) for k, v in result_rm.items()}

pattern = r'https?://[\w!?/\+\-_~=;\.,*&@#$%\(\)\'\[\]]+'
result_rm3 = {k: re.sub(pattern, '', v) for k, v in result_rm2.items()}

pattern = r'<.+?>' 
result_rm4 = {k: re.sub(pattern, '', v) for k, v in result_rm3.items()}

pattern = r'\{\{(?:lang|仮リンク)(?:[^|]*?\|)*?([^|]*?)\}\}' 
result_rm5 = {k: re.sub(pattern, r'\1', v) for k, v in result_rm4.items()}
pprint.pprint(result_rm5)
