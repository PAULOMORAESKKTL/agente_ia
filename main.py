import anthropic
import os
import dotenv

dotenv.load_dotenv()

client = anthropic.Anthropic(
    
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=20000,
    temperature=1,
    system="Listar apenas os nomes dos alimentos, sem adicionar descrição.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "3 Alimentos com brócolis"
                }
            ]
        }
    ]
)
resposta = message.content[0].text
print(resposta)