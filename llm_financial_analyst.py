#!/usr/bin/env python3
"""
LLM Financial Analyst - Script pour génération de texte financier
Utilise un modèle LLM open source pour analyser des données financières
"""

import sys
import json
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class FinancialLLM:
    def __init__(self, model_name="microsoft/Phi-3-mini-4k-instruct"):
        """
        Initialise le LLM pour l'analyse financière
        
        Args:
            model_name: Nom du modèle Hugging Face à utiliser
        """
        print(f"🤖 Chargement du modèle {model_name}...")
        print("(Ceci peut prendre quelques minutes au premier chargement)")
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto",
            trust_remote_code=True
        )
        
        print("✅ Modèle chargé avec succès!")
    
    def generate(self, prompt, max_tokens=300, temperature=0.7):
        """
        Génère une réponse à partir d'un prompt
        
        Args:
            prompt: Question ou instruction pour le LLM
            max_tokens: Nombre maximum de tokens à générer
            temperature: Contrôle la créativité (0.0 = déterministe, 1.0 = créatif)
        
        Returns:
            Texte généré par le LLM
        """
        # Format Phi-3
        formatted_prompt = f"<|user|>\n{prompt}<|end|>\n<|assistant|>"
        
        inputs = self.tokenizer(formatted_prompt, return_tensors="pt", return_attention_mask=True)
        
        if torch.cuda.is_available():
            inputs = {k: v.cuda() for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = self.model.generate(
                inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_new_tokens=max_tokens,
                temperature=temperature,
                do_sample=True,
                top_p=0.95,
                pad_token_id=self.tokenizer.eos_token_id
            )
        
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extraire seulement la réponse de l'assistant
        if "<|assistant|>" in generated_text:
            response = generated_text.split("<|assistant|>")[-1]
            response = response.split("<|end|>")[0]
        else:
            response = generated_text
        
        return response.strip()
    
    def generate_model_hypotheses(self, stats):
        """
        Génère des hypothèses de modélisation basées sur les statistiques
        
        Args:
            stats: Dictionnaire avec les statistiques (mean, vol, skew, etc.)
        
        Returns:
            Texte avec les hypothèses de modélisation
        """
        prompt = f"""Based on these financial time series statistics, suggest which statistical models would be most appropriate:

Asset 1 (AAPL - Tech Stock):
- Average price: ${stats['aapl_mean']:.2f}
- Volatility (std): {stats['aapl_vol']:.4f}
- Skewness: {stats['aapl_skew']:.2f}
- Type: Large-cap technology stock

Asset 2 (BTC - Cryptocurrency):
- Average price: ${stats['btc_mean']:.2f}
- Volatility (std): {stats['btc_vol']:.4f}
- Skewness: {stats['btc_skew']:.2f}
- Type: Volatile cryptocurrency

Provide specific model recommendations (ARIMA, GARCH, LSTM, VAR, etc.) for each asset and explain why. Be concise and technical."""
        
        return self.generate(prompt, max_tokens=400)
    
    def vulgarize_results(self, results):
        """
        Vulgarise des résultats techniques pour le grand public
        
        Args:
            results: Dictionnaire avec les résultats des modèles
        
        Returns:
            Explication vulgarisée
        """
        prompt = f"""Explain these financial modeling results in simple terms that a non-technical investor can understand:

AAPL (Apple Stock):
- Best model: {results.get('aapl_best_model', 'VAR')}
- Forecast accuracy (RMSE): {results.get('aapl_rmse', 0.015):.4f}
- Volatility: {results.get('aapl_vol', 'Moderate')}

BTC (Bitcoin):
- Best model: {results.get('btc_best_model', 'LSTM')}
- Forecast accuracy (RMSE): {results.get('btc_rmse', 0.022):.4f}
- Volatility: {results.get('btc_vol', 'High')}

Key findings:
- {results.get('key_finding_1', 'Bitcoin is 2x more volatile than Apple')}
- {results.get('key_finding_2', 'Apple shows more predictable patterns')}

Write a clear, simple explanation for non-experts. Avoid jargon."""
        
        return self.generate(prompt, max_tokens=350)
    
    def generate_investment_recommendations(self, analysis):
        """
        Génère des recommandations d'investissement avec limites et risques
        
        Args:
            analysis: Dictionnaire avec l'analyse des actifs
        
        Returns:
            Recommandations avec avertissements
        """
        prompt = f"""Based on this financial analysis, provide investment recommendations with clear risk warnings:

Analysis Summary:
- AAPL: Stable, moderate volatility, good predictability
- BTC: Volatile, high risk, potential high returns
- Correlation: Moderate positive correlation

Portfolio allocation for a {analysis.get('risk_profile', 'moderate risk')} investor:
Provide:
1. Recommended allocation (% in each asset)
2. Risk level assessment
3. Important limitations and warnings
4. Market conditions to watch

Be professional and emphasize risks. This is for educational purposes only."""
        
        return self.generate(prompt, max_tokens=400)


def main():
    """Fonction principale pour tester le module"""
    if len(sys.argv) < 2:
        print("Usage: python llm_financial_analyst.py <command> [args]")
        print("Commands: test, generate_hypotheses, vulgarize, recommend")
        sys.exit(1)
    
    command = sys.argv[1]
    
    # Initialiser le LLM
    llm = FinancialLLM()
    
    if command == "test":
        response = llm.generate("What is time series forecasting?", max_tokens=100)
        print("\n" + "="*50)
        print("TEST RESPONSE:")
        print("="*50)
        print(response)
    
    elif command == "generate_hypotheses":
        # Exemple de statistiques
        stats = {
            'aapl_mean': 127.29,
            'aapl_vol': 0.0231,
            'aapl_skew': -0.233,
            'btc_mean': 23456.78,
            'btc_vol': 0.0416,
            'btc_skew': -2.02
        }
        response = llm.generate_model_hypotheses(stats)
        print("\n" + "="*50)
        print("MODEL HYPOTHESES:")
        print("="*50)
        print(response)
    
    elif command == "json_input":
        # Lire JSON depuis stdin
        data = json.load(sys.stdin)
        
        if 'command' not in data:
            print(json.dumps({"error": "Missing 'command' field"}))
            sys.exit(1)
        
        cmd = data['command']
        result = {}
        
        try:
            if cmd == "hypotheses":
                result['response'] = llm.generate_model_hypotheses(data['stats'])
            elif cmd == "vulgarize":
                result['response'] = llm.vulgarize_results(data['results'])
            elif cmd == "recommend":
                result['response'] = llm.generate_investment_recommendations(data['analysis'])
            else:
                result['error'] = f"Unknown command: {cmd}"
            
            print(json.dumps(result, ensure_ascii=False))
        
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.exit(1)


if __name__ == "__main__":
    main()

