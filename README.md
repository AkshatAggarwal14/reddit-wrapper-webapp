# Reddit Wrapper WebApp

This is a simple web application that fetches articles from a Reddit subreddit using the Reddit API and displays them on a webpage.

## How to Run the Application

1. Clone this repository to your local machine:

```sh
git clone https://github.com/AkshatAggarwal14/reddit-wrapper-webapp.git
cd reddit-wrapper-webapp
```

2. Install the required Python packages by running:
```sh
pip install -r requirements.txt
```

3. Run the FastAPI backend:
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

The backend will be accessible at `http://0.0.0.0:8000`.

4. Open the `index.html` file in your web browser. You can simply open the file using your browser or host it on a local server.

## Third-Party Libraries

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast, web framework for building APIs with Python.
- [aiohttp](https://docs.aiohttp.org/en/stable/): Asynchronous HTTP client/server framework for asyncio.

## Frontend Design

The frontend is designed to be simple and responsive. It allows you to enter a subreddit name, fetch articles from that subreddit, and display them on the page.