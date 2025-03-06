from ollama import embed

response = embed(model='llama3.2', input=['The sky is blue because of rayleigh scattering', 'Grass is green because of chlorophyll'])

print(len(response['embeddings']))