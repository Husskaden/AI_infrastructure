"Run LLMs with Docker Model Runner (No Python, Pytorch, or DUCA Required"

Without docker: Check 
	- CUDA is there to be able to use GPU on machine
	- Check that python version is compatible with the LLMs arhcitecture
	- Check that python libraries and dependencies are there and up to date

To run inference engine directly on docker:

docker run -d --name ollama \
	--gpus all \
	-p 11434:11434
	-v ollama:/root/.ollama \
	ollama/ollama \
	
	
Then immediately pull a configured model:

docker exec -it ollama ollama pull qwen3

docker exec -it ollama ollama run qwen3


Example:
sudo apt-get update
sudp apt-get install docker-model-plugin -y

To verify:
docker model version

Pull an AI Model as an OCI artifact (are stored in layers like container images):
docker model pull smollm2:latest

Verify it is available:
docker model ls
	
Test model interactively:
docker model run smollm2:latest
Type a prompt like: "system check. Are you online" - may take 10-20 secs first run

Start the background inference service 
	- Docker model runner includes a background inference service that automatically exploses your models via n OpenAI-compatible API.
	- Models are automatically expsed on port 12434

Check if the runner is already active:
docker model status

Start model runner service:
docker model start-runner

Verify the runner is active
docker model status

Check which models are loaded
docker model ps
	
Query via OpenAPI
	- Open API format allows you to swap models without rewriting code

Send a JSON payload to the api and format the output with jq:

curl -s http://localhost:12434/engines/v1/chat/completions \
	- H "Content-Type: application/json" \
	- d @/root/code/payload.json | jq 
	
Extract just the AI's response

curl -s http://localhost:12434/engines/v1/chat/completions \
	- H "Content-Type: application/json" \
	- d @/root/code/payload.json | jq -r '.choices[0].message.content'

Create custom persona with system prompt:
	- Open the fil linux_export.json and replace th ___ placeholder with a system prompt:
"You are an export Linux and Devops assistant. Only answer questions about…"

Content of persona "linux-expert.json":


{
    "model": "smollm2:latest",
    "messages": [
        {"role": "system","content": "You are a Linux expert. Only answer questions about linux. Be concise."}, 
        {"role": "user", "content": "How do I check disk space?"}
    ],
    "temperature": 0.7, 
    "max_tokens": 500
}


Start a chat with linux export:

bash /root/code/chat.sh

Type "exit" when done

Packaging for offline environments

With Docker Model Runner, you separate WHAT (the model) from HOW (the configuration)
	- Model: Pulled from your private registry (mirrored from Docker Hub)
	- Config + Chat: your linux-exert.json and chat.sh travel with your code
	- Note: An OCI artifact is conpletely self-contained with runtime, withs and config frozen inside, so no need to worry about the model downloading python drivers etc from external sources.

In real world
	- Mirror smollm2:lates to private registry (Harbor, Artifactory)
	- Configure Docker to pull from private registry
	- Deploy you packager with linux-expert.json and chat.sh

	1. Package your configuration for the "Red Room":

mkdir -p red-room-package
cp ~/linux-expert.json ~/red-room-package
chmod +x chat.sh

	2. Verify your package in Code Server. You should see the red-room-package folder

	3. Test the deployment - start a chat from the package:
cd red-room-package
bash chat.sh ./linux-expert.json

4 Chat with your linux expert
