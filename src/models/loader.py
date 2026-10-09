import torch
from qwen_tts import Qwen3TTSModel


def load_qwen_model(model_id: str) -> Qwen3TTSModel:
    if not torch.cuda.is_available():
        raise RuntimeError(
            "CUDA GPU is not available. "
            "Enable GPU in the Colab runtime."
        )

    return Qwen3TTSModel.from_pretrained(
        model_id,
        device_map="cuda:0",
        dtype=torch.float16,
    )