from openai import AzureOpenAI
from pathlib import Path

# Create an AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=YOUR_FOUNDRY_ENDPOINT,
    api_key=YOUR_FOUNDRY_KEY,
    api_version="2025-03-01-preview"
)

# Get the audio file
file_path = Path("speech.mp3")
audio_file = open(file_path, "rb")

# Use the model to transcribe the audio file
transcription = client.audio.transcriptions.create(
    model=YOUR_MODEL_DEPLOYMENT,
    file=audio_file,
    response_format="text"
)

print(transcription)
