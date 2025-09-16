# sourced from https://www.geeksforgeeks.org/read-json-file-using-python/ 
import json
 
# OPEN THE FILE
f = open('data.json')

# READ THE CONTENTS
data = json.load(f)

# CLOSE THE FILE
f.close()

print('------------------')
print(data)
print('------------------')
print(data['redirects'])
print('------------------')
print(data['redirects'][0])