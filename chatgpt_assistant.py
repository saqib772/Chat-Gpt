
import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")

while input != "quit()":
    message = input("What You want to Search for !!! ")
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
