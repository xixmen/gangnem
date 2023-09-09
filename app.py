from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Set your OpenAI API key
openai_api_key = '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'
proxies = {
              "http"  : "http://xixmen:HcqtiySXaFZ76Pdt@proxy.packetstream.io:31111",
              "https" : "https://xixmen:HcqtiySXaFZ76Pdt@proxy.packetstream.io:31111",
            }

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']

    # Construct the request payload
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"{user_message}"}],
        "temperature": 1.0,
        "top_p": 1.0,
        "n": 1,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    # Make a POST request to the OpenAI API with the gpt-3.5-turbo engine
    response = requests.post('https://api.openai.com/v1/chat/completions', json=data, headers=headers, proxies=proxies)

    if response.status_code == 200:
        response_data = response.json()
        assistant_response = response_data['choices'][0]['message']['content']
        return assistant_response
    else:
        print(response.text)
        return "Error: Unable to generate a response."


if __name__ == '__main__':
    app.run(debug=True)
