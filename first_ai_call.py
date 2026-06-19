# Run from virtual environment with command: 
# python3 first_ai_call.py
# Prerequisites: 
# - Running LLM
# - API key

from openai import OpenAI

# Create a client
client = OpenAI(api_key="INDSÆT_API_NØGLE_HER") # Connect to API with the API key

# Send a message
response = client.chat.completions.create(  # calls the model response.choices[0].message.content is the LLM generating the output
    model="gpt-4o",
    temperature=1 # temperature=0 gives the same answer every time, temperature=1 gives a different answer every run
    messages=[
        {"role": "system","content": "You are a helpful assistant. Be concise."},
        {"role": "user", "content": "Write a one-sentence story about a robot"}
    ]
)

# Print the response
print(response.choices[0].message.content) # choices[0] is the first and usually only reply. message.conent is the actual text string
