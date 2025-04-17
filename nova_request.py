from google import genai
import user_config

client = genai.Client(api_key= user_config.gemini_key)
def send_request(query):

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=query
    )
    return response.text

def send_request2(query):

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=query
    )
    return response.text