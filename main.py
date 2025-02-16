from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google import genai
from pydantic import BaseModel

app = FastAPI()

client = genai.Client(api_key='AIzaSyBpfdkpkxV684ecVM2diOqbXTJbpLQLmZ4')

profile = {
    "name":"Angelina",
    "age":36,
}

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3002",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/profile')
def say_hello():
    return {
        "data":profile
    }

class Prompt(BaseModel):
    prompt:str

@app.post('/prompt')
def llm_response(prompt:Prompt):
    print('Profile recommendations  is**********',prompt.prompt)
    response =  client.models.generate_content(model="gemini-2.0-flash",contents=prompt.prompt)
    textResponse = response.text
    print('Here is Gen AI recommendations',textResponse)
    return {
           'response':textResponse
    }