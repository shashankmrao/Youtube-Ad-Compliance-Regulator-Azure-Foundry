import json
import re

text="""```json{"name":"Alice"}```"""

#m = re.match(r"^```json\s*(.*?)\s*```$", text, re.DOTALL)
match = re.search(r"```json\s*(.*?)\s*```", text.strip(), re.DOTALL)
if match:
    text = match.group(1)
    text = json.loads(text.strip())
    print(text)