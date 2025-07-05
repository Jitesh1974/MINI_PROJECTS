import google.generativeai as genai

genai.configure(api_key="paste your api key here")

model = genai.GenerativeModel("api model name")

while True:
  prompt = input("How may I help you Sir: ")

  response = model.generate_content(prompt)

  print(response.text)

  print('')
  msg = input('Any further assistance required? (yes/no/exit): ')
  if msg.lower() == ('no' or 'exit'):
    print("Thank you for using our service!")
    break
  elif msg.lower() == 'yes': 

    prompt2 = input("Please enter your next query: ")
    response2 = model.generate_content(prompt2)
    print(response2.text)
    print('')
    continue
