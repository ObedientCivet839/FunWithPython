import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key_path = './.env'

def request(text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.6,
    )
    return response
