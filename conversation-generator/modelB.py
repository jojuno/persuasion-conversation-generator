import requests

token = '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' # TODO: check on token expiry 
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-3B"
headers = {"Authorization": "Bearer " + token}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def feed(input):
    response = query({'inputs': input})
    return response['generated_text']

'''
	usage example: 
		A: How long have you been enjoying your job?
		B: I've been working here for about a year and a half. It's a great place to work. 
		A: It's also very peaceful.
		B: < response from query > 
		... 
'''
# print(query({
# 	"inputs": {
# 		"past_user_inputs": ['How long have you been enjoying your job?'],
# 		"generated_responses": ['I\'ve been working here for about a year and a half. It\'s a great place to work.'],
# 		"text": 'It\'s also very peaceful.'
# 	},
# }))

# print(output)
