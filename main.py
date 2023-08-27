from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import aiohttp

BASE_URL = 'https://www.reddit.com'
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

class RedditAPIException(HTTPException):
    def __init__(self, status_code: int = 500, detail: str = "Reddit API Error"):
        super().__init__(status_code=status_code, detail=detail)

async def fetch_subreddit_threads(subreddit_name):
    async with aiohttp.ClientSession() as session:
        url = f"{BASE_URL}/r/{subreddit_name}/new.json?limit=10"
        async with session.get(url) as response:            
            if response.status != 200:
                raise RedditAPIException()

            data = await response.json()

            print(data)

        threads = []
        for post in data["data"]["children"]:
            thread = post["data"]
            threads.append({
                "title": thread["title"],
                "author": thread["author"],
                "created_utc": int(thread["created_utc"]),
                "url": f"{BASE_URL}{thread['permalink']}",
                "score": thread["score"],
            })
        
        return threads

@app.exception_handler(RedditAPIException)
async def handle_reddit_api_exception(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.get("/subreddit/{subreddit_name}")
async def get_subreddit_threads(subreddit_name: str):
    threads = await fetch_subreddit_threads(subreddit_name)
    return threads

@app.get("/health")
async def health_check():
    async with aiohttp.ClientSession() as session:
        url = f"{BASE_URL}/api/v1/me"

        async with session.get(url) as response:
            if response.status != 200:
                raise RedditAPIException()
    return {"status": "healthy"}