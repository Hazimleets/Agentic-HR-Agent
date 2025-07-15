# model.py

from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM

def load_model(model_name="google/flan-t5-small"):
    print(f"[INFO] Loading model: {model_name}")
    if "t5" in model_name.lower() or "flan" in model_name.lower():
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    else:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
    return pipe

# Load the model once
pipe = load_model()

def query_llm(prompt):
    try:
        print("[LOG] Local LLM inference started")
        result = pipe(prompt, max_new_tokens=200)[0]["generated_text"]
        return result
    except Exception as e:
        print("[ERROR] Local model error:", str(e))
        return f"Local Model Error: {str(e)}"
