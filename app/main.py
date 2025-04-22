import requests

def main():
    prompt = "Era uma vez um mundo onde"
    response = requests.post("http://llm:8000/generate", json={"prompt": prompt})
    print("Resposta gerada pelo modelo:")
    print(response.json().get("result"))

if __name__ == "__main__":
    main()
