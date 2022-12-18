import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a melody in the form of a list of (pitch, duration) pairs in Python syntax, where the pitch uses the MIDI pitch standard, and the duration represents the number of quarter notes. Use a pitch of None to represent a rest. The tune should be a slow jazz piece in G Minor for saxophone. The duration of the notes should vary, and be between 0.25 and 1. Use breaks too. Go!\n\nHere is a slow jazz melody in G Minor for saxophone, written in the form of a list of (pitch, duration) pairs:\n\nmelody = [\n  (55, 0.75),\n  (50, 0.75),\n  (48, 0.5),\n  (None, 0.25),\n  (55, 0.5),\n  (53, 0.25),\n  (50, 0.5),\n  (None, 0.25),\n  (55, 1),\n  (50, 0.75),\n  (48, 0.75),\n  (45, 0.5),\n  (None, 0.25),\n  (50, 0.5),\n  (48, 0.25),\n  (45, 0.5),\n  (None, 0.25),\n  (50, 1)\n]",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
