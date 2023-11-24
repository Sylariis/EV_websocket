#Written by Tsuki from NitsukoVT , as a program to run alongside VTSpog. VTSpog must be running.
#Setup instructions in the readme


from elevenlabs import generate, Voice, VoiceSettings, play, set_api_key, stream
from elevenlabs.api import History
import asyncio
import json
from websockets.sync.client import connect
import nikkohidden

def startTTS(audio):

    audiotext = audio

    voice = Voice(
        voice_id = nikkohidden.NikkoVoice,
        model_id = "eleven_monolingual_v2",
        settings=VoiceSettings(stability=0.60, similarity_boost=1.0, style=0.1, use_speaker_boost=True)
    )

    audio_stream = generate(text=audiotext, voice=voice)
    play(audio_stream)


def stopTTS():
    #stop TTS later
    print("TTS stopping \n")

def hello():
    set_api_key(nikkohidden.apikey)

    with connect("ws://localhost:3800/api") as websocket:
        websocket.send('{"type":"client","data":"asdasda"}')
        message = websocket.recv()

        while(1):
            message = websocket.recv()

            message = json.loads(message)
            if message["type"] == "mouth":
                pass
            elif message["type"] == "startTTS":
                text = str((message["data"]))
                print(text)
                text=text.split("'text':")
                text2 = text[1]
                text2 = text2.split("'user':")
                text3 = text2[0]
                print("text3",text3)

                print(message)

                startTTS(str(text3))

            elif message["type"] == "stopTTS":
                stopTTS()

hello()
