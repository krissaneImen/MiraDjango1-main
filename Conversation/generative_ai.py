import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# Setup your API key
GOOGLE_API_KEY = 'AIzaSyC1JbzQw2TB2SVyLPKxPQZxuqWFig6gsXY'
genai.configure(api_key=GOOGLE_API_KEY)

def generate_response(message):
    """
    Generates a response to the given message using the generative AI model.

    Parameters:
    message (str): The input message for the AI model.

    Returns:
    str: The generated response.
    """
    # Generate text from text input
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("What is the meaning of life?")
    print(to_markdown(response.text))
    return to_markdown(response.text)
    
    
    
    # Collect the response
    
    for chunk in response:
        print(chunk.text)
        print("_"*80)

