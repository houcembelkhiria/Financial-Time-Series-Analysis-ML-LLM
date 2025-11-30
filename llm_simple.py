#!/usr/bin/env python3
"""
LLM Simple - Version allégée utilisant Flan-T5-Large
Plus rapide et moins gourmand en ressources
"""

import sys
import json
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class SimpleLLM:
    def __init__(self):
        """Initialise Flan-T5-Large (780M paramètres - plus léger que Phi-3)"""
        model_name = "google/flan-t5-large"
        # Écrire les messages informatifs sur stderr (pas stdout pour ne pas polluer le JSON)
        print(f"🤖 Chargement de {model_name}...", file=sys.stderr)
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Charger le modèle sans device_map (ne nécessite pas accelerate)
        try:
            # Essayer d'abord avec le nouveau paramètre dtype
            self.model = AutoModelForSeq2SeqLM.from_pretrained(
                model_name,
                low_cpu_mem_usage=True
            )
        except Exception as e:
            print(f"Tentative de chargement alternative...", file=sys.stderr)
            # Fallback simple
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        
        # Déplacer sur GPU si disponible
        if torch.cuda.is_available():
            print("🎮 GPU détecté, utilisation du GPU", file=sys.stderr)
            self.model = self.model.cuda()
        else:
            print("💻 Utilisation du CPU", file=sys.stderr)
        
        print("✅ Modèle chargé!", file=sys.stderr)
    
    def generate(self, prompt, max_tokens=250):
        """Génère une réponse"""
        inputs = self.tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
        
        # Déplacer les inputs sur le même device que le modèle
        device = next(self.model.parameters()).device
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                temperature=1.0,  # Standard
                do_sample=True,
                top_p=0.9
            )
        
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    def generate_hypotheses(self, aapl_mean, aapl_vol, aapl_skew, btc_mean, btc_vol, btc_skew):
        """Génère des hypothèses de modélisation"""
        prompt = f"""Q: AAPL stock has volatility {aapl_vol:.4f} and skewness {aapl_skew:.2f}. Bitcoin has volatility {btc_vol:.4f} and skewness {btc_skew:.2f}. Recommend forecasting models (ARIMA, GARCH, LSTM, VAR).
A:"""
        
        return self.generate(prompt, max_tokens=200)
    
    def vulgarize(self, aapl_rmse, btc_rmse, aapl_model, btc_model):
        """Vulgarise les résultats"""
        prompt = f"""Explain to a beginner investor:

Apple stock: forecast accuracy {(1-aapl_rmse)*100:.1f}%, using {aapl_model} model
Bitcoin: forecast accuracy {(1-btc_rmse)*100:.1f}%, using {btc_model} model

Simple explanation:"""
        
        return self.generate(prompt, max_tokens=250)
    
    def recommend(self, risk_level="moderate"):
        """Génère des recommandations d'investissement"""
        prompt = f"""You are a financial advisor. For a {risk_level}-risk investor with $10,000:

Question: How to split investment between Apple stock and Bitcoin?

Answer: I recommend"""
        
        return self.generate(prompt, max_tokens=300)


def main():
    if len(sys.argv) < 2:
        print("Usage: python llm_simple.py <command> [json_file]", file=sys.stderr)
        sys.exit(1)
    
    command = sys.argv[1]
    llm = SimpleLLM()
    
    if command == "json":
        # Lire JSON depuis stdin ou fichier
        if len(sys.argv) > 2:
            with open(sys.argv[2], 'r') as f:
                data = json.load(f)
        else:
            data = json.load(sys.stdin)
        
        result = {}
        
        try:
            if data['action'] == 'hypotheses':
                result['response'] = llm.generate_hypotheses(
                    data['aapl_mean'], data['aapl_vol'], data['aapl_skew'],
                    data['btc_mean'], data['btc_vol'], data['btc_skew']
                )
            elif data['action'] == 'vulgarize':
                result['response'] = llm.vulgarize(
                    data['aapl_rmse'], data['btc_rmse'],
                    data['aapl_model'], data['btc_model']
                )
            elif data['action'] == 'recommend':
                result['response'] = llm.recommend(data.get('risk_level', 'moderate'))
            
            print(json.dumps(result, ensure_ascii=False, indent=2))
        
        except Exception as e:
            print(json.dumps({"error": str(e)}), file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()

