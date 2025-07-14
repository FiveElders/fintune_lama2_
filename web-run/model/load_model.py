from transformers import AutoTokenizer, AutoModelForCausalLM

def load_model():
    tokenizer = AutoTokenizer.from_pretrained("ibrainf/Llama-2-7b-agri-finetune")
    model = AutoModelForCausalLM.from_pretrained(
        "ibrainf/Llama-2-7b-agri-finetune",
        torch_dtype="auto",
        device_map="auto"
    )
    return model, tokenizer
