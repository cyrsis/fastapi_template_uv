import uvicorn


def main():
    print("Hello from fastapi-template-uv!")


if __name__ == "__main__":
    uvicorn.run("src.app.app:app", host='0.0.0.0', port=9001, reload=True)
