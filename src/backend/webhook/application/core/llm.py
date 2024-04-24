import openai
import toml
import logging 

# Load the API key from the config.toml file
config = toml.load("config/config.toml")
openai.api_key = config["openai"]["api_key"]

def analyze_error_with_openai(error_message):
    try:
        # Provide the error message as context to GPT-3 and generate responses
        prompt = "A developer encounters the following error message: '{}'. Please provide a detailed explanation of possible reasons causing this error with a code example, also how me the fix with code example".format(error_message)
        response = openai.Completion.create(
            engine=config["engine"]["name"],
            prompt=prompt,
            temperature=0.5,
            max_tokens=1000,
            n=1,
            stop=None,
            echo=True
        )
        # Extract and process the model output
        logging.info(f"promt from the user: {prompt}, responce given by the model: {response}")
        if (response.choices[0].text) == "":
            return "No response from the model"
        else:
            return response.choices[0].text
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return "An error occurred while processing: {}".format(str(e))
