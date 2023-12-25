import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
from peft import PeftModel, LoraConfig

class ModelQueryService:
    def __init__(self, base_model_id="mistralai/Mixtral-8x7B-v0.1", fine_tuned_model_id="NPastrami15/PMSANLP"):
        self.base_model_id = base_model_id
        self.fine_tuned_model_id = fine_tuned_model_id
        self.model = self.load_model_with_adapters()
        self.tokenizer = AutoTokenizer.from_pretrained(base_model_id)
        self.generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def load_model_with_adapters(self):
        # Configure LoRA
        lora_config = LoraConfig(
            r=8,
            lora_alpha=16,
            target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "w1", "w2", "w3", "lm_head"],
            bias="none",
            lora_dropout=0.05,
            task_type="CAUSAL_LM",
        )

        # Load the base model with Bits and Bytes quantization config
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16
        )
        base_model = AutoModelForCausalLM.from_pretrained(
            self.base_model_id,
            quantization_config=bnb_config,
            device_map="auto",
            trust_remote_code=True,
        )

        # Apply LoRA to the base model
        model_with_lora = get_peft_model(base_model, lora_config)

        # Overlay the fine-tuned weights
        ft_model = PeftModel.from_pretrained(model_with_lora, self.fine_tuned_model_id)

        return ft_model

    def query_model(self, prompt):
        try:
            responses = self.generator(prompt, max_length=50, num_return_sequences=1)
            return responses[0]['generated_text']
        except Exception as e:
            print(f"Error querying model: {e}")
            return "Error in generating response."