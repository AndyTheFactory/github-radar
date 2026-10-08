---
repository: "ysharma3501/LuxTTS"
github_id: 1140828984
url: "https://github.com/ysharma3501/LuxTTS"
description: "A high-quality rapid TTS voice cloning model that reaches speeds of 150x realtime."
starred_at: "2026-10-08T20:14:53Z"
language: "Python"
topics: []
homepage: ""
license: "Apache-2.0"
archived: false
---

# ysharma3501/LuxTTS

A high-quality rapid TTS voice cloning model that reaches speeds of 150x realtime.

**GitHub:** https://github.com/ysharma3501/LuxTTS

## README excerpt

> # LuxTTS
>
> &nbsp;
> &nbsp;
>
> LuxTTS is an lightweight zipvoice based text-to-speech model designed for high quality voice cloning and realistic generation at speeds exceeding 150x realtime.
> https://github.com/user-attachments/assets/a3b57152-8d97-43ce-bd99-26dc9a145c29
> ### The main features are
> - Voice cloning: SOTA voice cloning on par with models 10x larger.
> - Clarity: Clear 48khz speech generation unlike most TTS models which are limited to 24khz.
> - Speed: Reaches speeds of 150x realtime on a single GPU and faster then realtime on CPU's as well.
> - Efficiency: Fits within 1gb vram meaning it can fit in any local gpu.
> ## Usage
> You can try it locally, colab, or spaces.
> #### Simple installation:
> git clone https://github.com/ysharma3501/LuxTTS.git
> cd LuxTTS
> pip install -r requirements.txt
> #### Load model:
> from zipvoice.luxvoice import LuxTTS
> # load model on GPU
> lux_tts = LuxTTS('YatharthS/LuxTTS', device='cuda')
> # load model on CPU
> # lux_tts = LuxTTS('YatharthS/LuxTTS', device='cpu', threads=2)
> # load model on MPS for macs
> # lux_tts = LuxTTS('YatharthS/LuxTTS', device='mps')
> #### Simple inference
> import soundfile as sf
> from IPython.display import Audio
> text = "Hey, what's up? I'm feeling really great if you ask me honestly!"
> ## change this to your reference file path, can be wav/mp3
> prompt_audio = 'audio_file.wav'
> ## encode audio(takes 10s to init because of librosa first time)
> encoded_prompt = lux_tts.encode_prompt(prompt_audio, rms=0.01)
> ## generate speech
> final_wav = lux_tts.generate_speech(text, encoded_prompt, num_steps=4)
> ## save audio
> final_wav = final_wav.numpy().squeeze()
> sf.write('output.wav', final_wav, 48000)
> ## display speech
> if display is not None:
> display(Audio(final_wav, rate=48000))
> #### Inference with sampling params:
> import soundfile as sf
> from IPython.display import Audio
> text = "Hey, what's up? I'm feeling really great if you ask me honestly!"
> ## change this to your reference file path, can be wav/mp3
> prompt_audio = 'audio_file.wav'
> rms = 0.01 ## higher makes it sound louder(0.01 or so recommended)
> t_shift = 0.9 ## sampling param, higher can sound better but worse WER
> num_steps = 4 ## sampling param, higher sounds better but takes longer(3-4 is best for efficiency)
> speed = 1.0 ## sampling param, controls speed of audio(lower=slower)
> return_smooth = False ## sampling param, makes it sound smoother possibly but less cleaner
> ref_duration = 5 ## Setting it lower can speedup inference, set to 1000 if you find artifacts.
> ## encode audio(takes 10s

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->


<!-- github-radar:enrichment:start -->

## AI-generated catalog summary

LuxTTS is a lightweight zipvoice-based text-to-speech model for voice cloning and speech generation at 48kHz. The README documents CUDA, CPU, and MPS device support and a Python API that encodes a reference audio prompt and generates speech from text.

### Classification

```json
{
  "enrichment": {
    "version": 1,
    "model": "claude-haiku-5.5",
    "source_sha256": "e67fd6aa257915b6f844d2150fcb2f5681e86cf07792900a51e53a066e5fa806"
  },
  "primary_domain": "ai-ml",
  "secondary_domains": [
    "vision-media"
  ],
  "repository_type": "library",
  "capabilities": [
    "audio-generation",
    "speech-synthesis",
    "inference-serving"
  ],
  "technologies": [
    "Python",
    "PyTorch",
    "ZipVoice",
    "soundfile",
    "librosa",
    "IPython"
  ],
  "summary": "LuxTTS is a lightweight zipvoice-based text-to-speech model for voice cloning and speech generation at 48kHz. The README documents CUDA, CPU, and MPS device support and a Python API that encodes a reference audio prompt and generates speech from text.",
  "use_cases": [
    "Cloning a speaker's voice from a short reference audio file to synthesize new speech",
    "Generating high-quality 48kHz speech on local GPUs or CPUs",
    "Running text-to-speech inference in Python notebooks"
  ],
  "limitations": [
    "Performance claims such as 150x realtime and 1GB VRAM are README claims and are not independently verified here",
    "Requires a reference audio file for voice cloning",
    "Documentation excerpt is truncated and lists no explicit license terms beyond the metadata"
  ],
  "suggested_terms": [
    "text-to-speech",
    "voice cloning",
    "zipvoice",
    "speech synthesis",
    "TTS model"
  ],
  "confidence": "high"
}
```

<!-- github-radar:enrichment:end -->
