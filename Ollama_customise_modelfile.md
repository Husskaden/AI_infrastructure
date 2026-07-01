# Modify any modelfile to your needs with ollama

Model file:

``````

FROM llama3.2

PARAMETER temperature 0.3

SYSTEM You are an AI assistant, your name is Harris. You are an AI assistant for the employees in an investment and portfolio managment firm called Growmore. Your job is to assist employees in managing client investments and portfolios. The currency you deal with is Indian Rupees (INR).

``````

Command to create the new model
````
ollama create <name of customised mode> f ./Customised model file
ollama create harris -f ./Modelfile

````

Run new model:

````

ollama run harris

`````

Share customised models:
Send the model files - or use ollama model registry
- Create an account and ollama.com to get ollama key
- Copy diretory under "Ollama keys" that it corresponds with your situation
- Copy machine public key and paste it under "Ollama keys"
- Now trust is established between

Create a copy of model with correct registry account at ollama
````
ollama ls

ollama cp harris <username>/harris
ollama push <username>/harris


````




