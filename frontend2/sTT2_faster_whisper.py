from faster_whisper import WhisperModel
import json
import datetime

# Get date from user input
input_date = input("Enter date (DD/MM/YYYY): ").strip()

# Load Whisper model (use "tiny", "base", etc.)
model = WhisperModel("tiny", device="cpu")

# Transcribe audio file
segments, info = model.transcribe("/Users/dikshitamustoori/Desktop/voice1.mp3")

# Combine all segments into one summary string
full_text = " ".join([segment.text.strip() for segment in segments])

# Create the final JSON structure
output = {
    "date": input_date,
    "user": "dikshita",
    "summary": full_text
}

# Save JSON file
with open("day12.json", "w") as f:
    json.dump(output, f, indent=2)

print("✅ Saved transcription to 'transcription_output.json'")
