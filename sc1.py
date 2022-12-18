from scamp import *

s = Session()

instr = s.new_part("Saxophone")

s.start_transcribing()

melody = [
  (55, 0.75),
  (50, 0.75),
  (48, 0.5),
  (None, 0.25),
  (55, 0.5),
  (53, 0.25),
  (50, 0.5),
  (None, 0.25),
  (55, 1),
  (50, 0.75),
  (48, 0.75),
  (45, 0.5),
  (None, 0.25),
  (50, 0.5),
  (48, 0.25),
  (45, 0.5),
  (None, 0.25),
  (50, 1)
]

for pitch, dur in melody:
	instr.play_note(pitch, 0.8, dur)

s.stop_transcribing().to_score(time_signature="4/4", title='Jazzy Tune', composer='OpenAI').show()
