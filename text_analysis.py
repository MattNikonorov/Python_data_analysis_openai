import openai
import pandas as pd

openai.api_key = "YOUR_KEY"

prompt = (
    """Extract the following information from the text: 
    Nvidia's revenue
    What Nvidia did this quarter
    Remarks about AI"""
)

def extract_info(text):
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "user", "content": prompt+"\n\n"+text}
        ],
        temperature=0.3,
    )
    message = completions.choices[0].message.content
    return message

f = open("transcript.txt", "r")
txt_data = f.read()

additional_params = extract_info(txt_data)
print(additional_params)
