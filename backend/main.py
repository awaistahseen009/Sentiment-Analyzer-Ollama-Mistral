from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

app = FastAPI()

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm = Ollama(model="mistral")
prompt_template = PromptTemplate(
    input_variables=["text"],
    template="""What is the sentiment of this text? Respond with Positive, Negative, or Neutral:\n\n{text}"""
)

@app.post("/analyze/")
def analyze_sentiment(text: str = Form(...)):
    prompt = prompt_template.format(text=text)
    response = llm.invoke(prompt)
    sentiment = response.strip()
    return {"sentiment": sentiment} 