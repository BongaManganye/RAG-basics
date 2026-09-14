import azure.cognitiveservices.speech as speech_sdk

# Speech config encapsulates the connection to the resource
speech_config = speech_sdk.SpeechConfig(subscription="YOUR_FOUNDRY_KEY",
                                       endpoint="YOUR_FOUNDRY_ENDPOINT")

# Audio config determines the audio stream source (defaults to system mic)
file_path = "audio.wav"
audio_config = speech_sdk.audio.AudioConfig(filename=file_path)

# Use a speech recognizer to transcribe the audio
speech_recognizer = speech_sdk.SpeechRecognizer(speech_config=speech_config,
                                               audio_config=audio_config)

result = speech_recognizer.recognize_once_async().get()

# Did it succeeed
if result.reason == speech_sdk.ResultReason.RecognizedSpeech:
    # Yes!
    print(f"Transcription:\n{result.text}")
else:
    # No. Try to determine why.
    print("Error transcribing message: {}".format(result.reason))
