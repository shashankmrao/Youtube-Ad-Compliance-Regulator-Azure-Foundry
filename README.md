1. Add Azure Resources extention on VS Code and sign in to azure account through VS Code
2. Add azure-identity-broker package

3. Add return as below for upload_video function in video_indexer.py
return response.json().get("id")

4. URL for wait_for_processing function in video_indexer.py
url = f"https://api.videoindexer.ai/{self.location}/Accounts/{self.account_id}/Videos/{video_id}/Index"

5. Add this in auditor node in nodes.py
    llm= AzureChatOpenAI(
        temperature=0.0,
        api_key = os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
        api_version= os.getenv("AZURE_OPENAI_API_VERSION")  
    )
    embeddings= AzureOpenAIEmbeddings(
        azure_deployment = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT","text-embbedding-3-small"),
        api_version = os.getenv("AZURE_OPENAI_API_VERSION","2024-02-01"),
        api_key = os.getenv("AZURE_OPENAI_EMBEDDING_API_KEY"),
        azure_endpoint = os.getenv("AZURE_OPENAI_EMBEDDING_ENDPOINT")
    )

6. Removed regex part of the code from nodes.py and add this:
match = re.search(r"```json\s*(.*?)\s*```", content.strip(), re.DOTALL)
        if match:
            content = match.group(1)

7. Below two env variables added to .env:
AZURE_OPENAI_EMBEDDING_ENDPOINT=""
AZURE_OPENAI_EMBEDDING_API_KEY=""


