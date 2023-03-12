import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 Astronomical events in 2023 "}])
print(completion.choices[0].message.content)

