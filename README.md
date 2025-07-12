Fine-tuning LLaMA 2 7B on Agricultural Data
🎯 Objective
Fine-tune the LLaMA 2 7B language model to understand and respond to agricultural instructions and questions, using a dataset specifically curated for farming and agricultural tasks.

🌾 Domain
Field: Agriculture / Agricultural AI

Data type: Instruction-based examples for farming, crops, pests, irrigation, fertilizers, etc.

🧠 Base Model
meta-llama/Llama-2-7b-hf

Loaded in 4-bit quantization for memory efficiency

Fine-tuned using LoRA (Low-Rank Adaptation) from the PEFT library

📊 Dataset Format
The dataset contains fields like:

json
Copy
Edit
{
  "instruction": "How to protect tomato plants from whiteflies?",
  "input": "",
  "output": "You can use yellow sticky traps and neem oil spray weekly."
}
Prompt template during training:


⚙️ Fine-tuning Overview

Libraries used:

transformers

peft (for LoRA)

datasets

bitsandbytes

accelerate

LoRA Configuration:

r=8, alpha=16, dropout=0.1

Target modules: q_proj, v_proj, k_proj, o_proj

Training Parameters:

1 epoch

Batch size: 4

Learning rate: 2e-4

Mixed precision: bf16

Model loaded with load_in_4bit=True for efficiency

