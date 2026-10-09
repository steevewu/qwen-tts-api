import threading

from qwen_tts import Qwen3TTSModel

from models.loader import load_qwen_model


class TTSService:
    def __init__(self, model_id: str):
        self.model: Qwen3TTSModel = load_qwen_model(
            model_id
        )
        self._inference_lock = threading.Lock()

        speakers = self.model.get_supported_speakers()
        self._speakers = {
            speaker.lower() for speaker in (speakers or [])
        }

    def get_supported_speakers(self) -> list[str]:
        return sorted(self._speakers)

    def generate(
        self,
        text: str,
        language: str,
        speaker: str,
        instruct: str | None = None,
    ):
        if self._speakers and speaker.lower() not in self._speakers:
            raise ValueError(
                f"Unsupported speaker '{speaker}'. "
                f"Available speakers: "
                f"{', '.join(self.get_supported_speakers())}"
            )

        with self._inference_lock:
            wavs, sample_rate = self.model.generate_custom_voice(
                text=text,
                language=language,
                speaker=speaker,
                instruct=instruct,
            )

        return wavs[0], sample_rate