# from PIL import Image
# from google import genai
# import user_config

# client = genai.Client(api_key=user_config.gemini_key)

# image = Image.open("/path/to/organ.png")
# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="A elephant watching taj mahal"
# )
# print(response.text)

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
import user_config

client = genai.Client(api_key=user_config.gemini_key)

def generate_image(contents):
   response = client.models.generate_content(
     model="gemini-2.0-flash-exp-image-generation",
     contents=contents,
     config=types.GenerateContentConfig(
       response_modalities=['Text', 'Image']
    )
   )
   for part in response.candidates[0].content.parts:
    if part.text is not None:
       print(part.text)
    elif part.inline_data is not None:
       image = Image.open(BytesIO((part.inline_data.data)))
       image.save('nova-native-image.png')
       image.show()

#generate_image("create a image of lord shiva having naag vasuki in his hand .")