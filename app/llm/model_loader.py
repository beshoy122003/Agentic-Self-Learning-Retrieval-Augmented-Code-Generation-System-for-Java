from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

_model = None
_tokenizer = None


def get_llm():

    global _model, _tokenizer

    if _model is None:

        print("Loading LLM model...")

        model_name = "deepseek-ai/deepseek-coder-1.3b-instruct"

        _tokenizer = AutoTokenizer.from_pretrained(model_name)

        _model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            torch_dtype=torch.float16
        )

    return _model, _tokenizer