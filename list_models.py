import google.generativeai as genai

# Configure your API key
genai.configure(api_key="AIzaSyDoy7rClDEw434tZEfsiC2y-9BFpNLPJKQ")

# Loop through and print available models
for model in genai.list_models():
    print(f"Model ID: {model.name}")
    print(f"Supported methods: {model.supported_generation_methods}\n")
