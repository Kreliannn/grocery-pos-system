import google.generativeai as genai 


genai.configure(api_key="AIzaSyBdrJMVA-cG86Dj3dJIskhB0DsCbo7CwFk")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("What's the date today?")

print(response.text)