import speech_recognition as audio

def convert_audio_to_text(audio_file_path):
    recognizer = audio.Recognizer()

    # Load the audio file
    with audio.AudioFile(audio_file_path) as audio_file:
        # Read the entire audio file
        audio = recognizer.record(audio_file)

    try:
        # Use the default speech recognition engine (Google Speech Recognition)
        text = recognizer.recognize_google(audio)
        return text
    except audio.UnknownValueError:
        print("Not able to convert audio")
    except audio.RequestError as e:
        print("Error_Code {0}".format(e))

    return None

# Example usage
audio_file_path = "path/to/your/audio/file.wav"
text = convert_audio_to_text(audio_file_path)
if text:
    print("Converted Text:")
    print(text)
