import streamlit as st
from transformers import BarkModel, AutoProcessor
import torch
import scipy

def text_to_audio(bark_model='suno/bark', voice_preset='v2/ru_speaker_3'):
    model = BarkModel.from_pretrained(bark_model)
    #device = 'cuda' if torch.cuda.is_available() else 'cpu'

    st.header(f"> test <", divider="rainbow")
    st.write(device)
    # model = model.to(device)
    # processor = AutoProcessor.from_pretrained(bark_model)
    #
    # text = 'Сайт рыба текст поможет дизайнеру'
    # inputs = processor(text, voice_preset=voice_preset.to(device))
    # audio_array = model.generate(**inputs)
    # audio_array = audio_array.cpu().numpy().squeeze()
    #
    # sample = model.generation_config.samle_rate
    # scipy.io.wavfile.write(f'{voice_preset.split("/")[1]}.wav', rate=sample_rate, data=audio_array)
def main():
    text_to_audio()

if __name__ == '__main__':
    main()