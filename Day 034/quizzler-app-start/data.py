import requests  # → Import the requests library to make HTTP requests

parameters = {
    "amount": 10,  # → Number of questions to fetch
    "type": "boolean",  # → Type of questions (True/False)
}

response = requests.get(
    "https://opentdb.com/api.php?amount=10&type=boolean", params=parameters
)  # → Send GET request with parameters
response.raise_for_status()  # ! Ensure the request was successful, otherwise raise an exception
data = response.json()  # → Parse the response JSON into a Python dictionary
question_data = data["results"]  # → Extract the list of questions from the API response
