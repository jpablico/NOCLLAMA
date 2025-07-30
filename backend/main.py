from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag_assistant import query_engine
from fastapi.responses import StreamingResponse
from rag_assistant import stream_query_response

app = FastAPI()

# CORS (allow React dev server to talk to FastAPI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to ["http://localhost:5173"]
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.post("/query-stream")
async def stream_query(data: dict):
    question = data.get("question")
    response = stream_query_response(question)

    async def event_generator():
        for token in response.response_gen:
            yield f"data: {token}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

@app.post("/query")
def query(request: QueryRequest):
    prompt = f"Respond in Markdown format.\n\n{request.question}"
    result = query_engine.query(prompt)
    return {"response": str(result)}