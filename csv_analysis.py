import openai
import csv
import pandas as pd

openai.api_key = "YOUR_KEY"

prompt = (
    """Extract the following information from the title and text: 
    The tone of the text
    The main lesson, point or advice
    How clickbait it is by looking at the title and comparing it to the contents of the text and 
    giving it a clickbait score from 0 to 3, where 0 is not clickbait and 3 is extremely clickbait"""
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

df = pd.read_csv('articles.csv')
df = df[:5]

titles = df['title']
articles = df['text']

apa1 = []
apa2 = []
apa3 = []
for di in range(len(df)):
    title = titles[di]
    abstract = articles[di]
    additional_params = extract_info('Title: '+str(title) + '\n\n' + 'Text: ' + str(abstract))
    try:
        result = additional_params.split("\n\n")
    except:
        result = {} 

    try:
        apa1.append(result[0])
    except Exception as e:
        apa1.append('No result')
    try:
        apa2.append(result[1])
    except Exception as e:
        apa2.append('No result')
    try:
        apa3.append(result[2])
    except Exception as e:
        apa3.append('No result')

df = df.assign(Tone=apa1)
df = df.assign(Main_lesson_point=apa2)
df = df.assign(Clickbait_score=apa3)

df.to_csv("data.csv", index=False)
