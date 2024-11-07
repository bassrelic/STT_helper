from RealtimeSTT import AudioToTextRecorder
import pyautogui

def process_text(text):
    if "senden" in text.lower():
        text.replace("senden","")
        pyautogui.typewrite(text + " ")
        pyautogui.press("enter")
    else:
        pyautogui.typewrite(text + " ")

if __name__ == '__main__':
    recorder = AudioToTextRecorder(language="de", wake_words="hey google", compute_type="int8_float32", realtime_model_type="large-v1", post_speech_silence_duration=1)

    while True:
        recorder.text(process_text)
        
