# quantization.py
from llama_cpp import Llama

llm = Llama(
    model_path="deepseek-70b.Q4_K_M.gguf",
    n_ctx=4096,
    n_gpu_layers=40
)