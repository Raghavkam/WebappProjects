# sourced from https://www.geeksforgeeks.org/read-json-file-using-python/ 
import json
 
# READ THE FILE
f = open('data.json')
data = json.load(f)
f.close()

# GET NEW VALUES
new_shortstring = "w1w1"
new_redirect = "https://www.fcps.edu"

# APPEND TO JSON OBJECT
data['redirects'].append(
	{new_shortstring : new_redirect}
	)

# CONVERT PYTHON DICTIONARY TO JSON
as_json = json.dumps(data)

with open("data.json", "w") as fileout:
    fileout.write(as_json)