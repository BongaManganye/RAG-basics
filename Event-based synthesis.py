import azure.cognitiveservices.speech as speech_sdk
from playsound3 import playsound

# Configure translation
source_language, target_language = "en-US", "fr"
output_file = "translation.wav"
translation_cfg = speech_sdk.translation.SpeechTranslationConfig(subscription="FOUNDRY_KEY",
                                                                 endpoint="FOUNDRY_ENDPOINT")
translation_cfg.speech_recognition_language = source_language
translation_cfg.add_target_language(target_language)
translation_cfg.voice_name = "fr-FR-HenriNeural"
audio_cfg = speech_sdk.AudioConfig(use_default_microphone=True)
translator = speech_sdk.translation.TranslationRecognizer(translation_config=translation_cfg,
                                                          audio_config=audio_cfg)

# Event handler function to save the synthesized audio to a file
def synthesis_callback(evt):
    size = len(evt.result.audio)
    print(f'Audio synthesized: {size} byte(s) {"(COMPLETED)" if size == 0 else ""}')

    if size > 0:
        file = open(output_file, 'wb+')
        file.write(evt.result.audio)
        file.close()

# Connect the event handler function
translator.synthesizing.connect(synthesis_callback)

# Get input from mic and translate it
print(f"Speak now (in {source_language})...")
translation_results = translator.recognize_once()
print(f"Translating '{translation_results.text}'")

# Print and play the translation results
print(translation_results.translations[target_language])
playsound(output_file)
