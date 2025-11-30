#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LLM Réel avec Flan-T5-Large Fine-tuned
Génère des analyses financières avec un vrai modèle de langage
"""

import sys
import json
import io

# Forcer l'encodage UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Variable globale pour le modèle (chargé une seule fois)
_model = None
_tokenizer = None

def load_model():
    """Charge Flan-T5-Large une seule fois"""
    global _model, _tokenizer
    
    if _model is not None:
        return _model, _tokenizer
    
    try:
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        import torch
        
        print("🤖 Chargement de Flan-T5-Large...", file=sys.stderr)
        print("   (Premier chargement : 2-5 min, ~3 GB)", file=sys.stderr)
        
        model_name = "google/flan-t5-large"
        
        # Charger le tokenizer
        _tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        # Charger le modèle avec optimisations
        device = "cuda" if torch.cuda.is_available() else "cpu"
        dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        
        _model = AutoModelForSeq2SeqLM.from_pretrained(
            model_name,
            torch_dtype=dtype,
            low_cpu_mem_usage=True
        )
        _model = _model.to(device)
        _model.eval()
        
        print(f"✅ Modèle chargé sur {device}", file=sys.stderr)
        
        return _model, _tokenizer
        
    except ImportError:
        print("❌ Erreur : transformers ou torch non installé", file=sys.stderr)
        print("💡 Installez avec : pip install transformers torch", file=sys.stderr)
        return None, None
    except Exception as e:
        print(f"❌ Erreur de chargement : {e}", file=sys.stderr)
        return None, None


def generate_with_flan_t5(prompt, max_new_tokens=400, temperature=0.7):
    """Génère une réponse avec Flan-T5-Large"""
    model, tokenizer = load_model()
    
    if model is None or tokenizer is None:
        return None
    
    try:
        import torch
        
        # Tokenizer le prompt
        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            max_length=512,
            truncation=True
        )
        
        # Déplacer sur le bon device
        device = next(model.parameters()).device
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        # Générer
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                do_sample=True,
                top_p=0.95,
                top_k=50,
                repetition_penalty=1.2,
                no_repeat_ngram_size=3
            )
        
        # Décoder
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
        
    except Exception as e:
        print(f"❌ Erreur de génération : {e}", file=sys.stderr)
        return None


def generate_hypotheses_llm(data):
    """Génère des hypothèses avec Flan-T5-Large"""
    # Extraire les valeurs
    aapl_vol = data['aapl_vol'][0] if isinstance(data['aapl_vol'], list) else data['aapl_vol']
    btc_vol = data['btc_vol'][0] if isinstance(data['btc_vol'], list) else data['btc_vol']
    aapl_skew = data['aapl_skew'][0] if isinstance(data['aapl_skew'], list) else data['aapl_skew']
    btc_skew = data['btc_skew'][0] if isinstance(data['btc_skew'], list) else data['btc_skew']
    
    # Prompt optimisé pour Flan-T5
    prompt = f"""You are a quantitative financial analyst. Analyze these statistics and recommend time series models.

AAPL (Apple Stock):
- Volatility: {aapl_vol:.4f} ({aapl_vol*100:.2f}%)
- Skewness: {aapl_skew:.2f}
- Type: Large-cap tech stock

BTC (Bitcoin):
- Volatility: {btc_vol:.4f} ({btc_vol*100:.2f}%)
- Skewness: {btc_skew:.2f}
- Type: Cryptocurrency

Task: For each asset, recommend which models to use (ARIMA, SARIMA, GARCH, LSTM, VAR) and explain why based on these statistics. Be specific and detailed.

Analysis:"""

    print("🔄 Génération avec Flan-T5-Large (30-60s)...", file=sys.stderr)
    response = generate_with_flan_t5(prompt, max_new_tokens=500, temperature=0.7)
    
    if response:
        # Enrichir la réponse avec les statistiques
        enriched = f"""ANALYSE STATISTIQUE ET RECOMMANDATIONS DE MODELES (Flan-T5-Large)

=== Statistiques Observees ===

AAPL: Volatilite {aapl_vol*100:.2f}%, Asymetrie {aapl_skew:.2f}
BTC:  Volatilite {btc_vol*100:.2f}%, Asymetrie {btc_skew:.2f} (soit {btc_vol/aapl_vol:.1f}x celle d'AAPL)

=== Recommandations du Modele ===

{response}

=== Conclusion Technique ===

La volatilite de BTC ({btc_vol*100:.2f}%) est {btc_vol/aapl_vol:.1f}x superieure a celle d'AAPL.
L'asymetrie forte de BTC ({btc_skew:.2f}) suggere des dynamiques non-lineaires necessitant
des modeles avances (LSTM/GARCH). AAPL, plus stable, est adapte aux modeles classiques (ARIMA/GARCH)."""
        
        return enriched
    
    return None


def generate_vulgarization_llm(data):
    """Vulgarise les résultats avec Flan-T5-Large"""
    aapl_rmse = data.get('aapl_rmse', 0.025)
    aapl_rmse = aapl_rmse[0] if isinstance(aapl_rmse, list) else aapl_rmse
    
    btc_rmse = data.get('btc_rmse', 0.055)
    btc_rmse = btc_rmse[0] if isinstance(btc_rmse, list) else btc_rmse
    
    aapl_model = data.get('aapl_model', 'ARIMA')
    aapl_model = aapl_model[0] if isinstance(aapl_model, list) else aapl_model
    
    btc_model = data.get('btc_model', 'LSTM')
    btc_model = btc_model[0] if isinstance(btc_model, list) else btc_model
    
    prompt = f"""Explain these financial forecasting results to a non-expert investor in simple terms.

Results:
- Apple (AAPL): Best model is {aapl_model}, prediction error {aapl_rmse*100:.2f}%
- Bitcoin (BTC): Best model is {btc_model}, prediction error {btc_rmse*100:.2f}%

Task: Explain what these results mean for someone considering investing. Use simple language, analogies, and practical implications. Avoid technical jargon.

Explanation:"""

    print("🔄 Vulgarisation avec Flan-T5-Large...", file=sys.stderr)
    response = generate_with_flan_t5(prompt, max_new_tokens=400, temperature=0.7)
    
    if response:
        enriched = f"""EXPLICATIONS SIMPLIFIEES POUR INVESTISSEURS (Flan-T5-Large)

=== Resultats de nos Modeles ===

Apple (AAPL) : {aapl_model} avec {aapl_rmse*100:.2f}% d'erreur
Bitcoin (BTC) : {btc_model} avec {btc_rmse*100:.2f}% d'erreur

=== Explication du Modele ===

{response}

=== Comparaison Rapide ===

                    Apple           Bitcoin
Previsibilite       Elevee          Faible
Stabilite           Stable          Volatile
Risque              Faible          Eleve
Pour qui ?          Debutants       Experimentes"""
        
        return enriched
    
    return None


def generate_recommendations_llm(data):
    """Génère des recommandations avec Flan-T5-Large"""
    risk_level = data.get('risk_level', 'modere')
    risk_level = risk_level[0] if isinstance(risk_level, list) else risk_level
    
    prompt = f"""You are a financial advisor. A client with {risk_level} risk tolerance asks about portfolio allocation between Apple stock and Bitcoin.

Context:
- Apple: Stable, lower volatility (2.3%), predictable returns
- Bitcoin: Volatile, higher volatility (4.8%), higher risk and potential returns

Task: Provide a detailed investment recommendation including:
1. Portfolio allocation percentages (Apple/Bitcoin/Cash)
2. Justification for each allocation
3. Risk management strategies (stop-loss, rebalancing)
4. Key risks for each investment
5. Important warnings and limitations

Recommendation:"""

    print("🔄 Recommandations avec Flan-T5-Large...", file=sys.stderr)
    response = generate_with_flan_t5(prompt, max_new_tokens=600, temperature=0.7)
    
    if response:
        enriched = f"""RECOMMANDATIONS D'INVESTISSEMENT (Flan-T5-Large)

!!! AVERTISSEMENT LEGAL !!!
Ceci est une analyse pedagogique generee par IA a titre educatif UNIQUEMENT.
Ce n'est PAS un conseil financier personnalise.
Consultez un conseiller financier agree avant d'investir.

=== Analyse pour profil de risque {risk_level} ===

{response}

=== LIMITES CRITIQUES ===

1. Modele IA : Peut generer des informations incorrectes (hallucinations)
2. Donnees historiques : Basees sur 2020-2022, contexte peut etre different
3. Pas de garantie : Performances passees != resultats futurs
4. Situation personnelle : Ne considere PAS vos besoins specifiques
5. Fiscalite et frais : Non inclus dans l'analyse
6. Validation humaine : OBLIGATOIRE avant toute decision

=== CONSEILS FINAUX ===

* N'investissez QUE l'argent que vous pouvez perdre
* Horizon minimum : 3-5 ans
* Diversifiez davantage (autres secteurs)
* Consultez un professionnel agree
* Ne suivez JAMAIS une recommandation d'IA sans validation

REGLE D'OR : "Ne mettez jamais tous vos oeufs dans le meme panier"

---
Note : Recommandation generee par Flan-T5-Large (LLM open source).
Validation par expert humain OBLIGATOIRE."""
        
        return enriched
    
    return None


def generate_fallback(action, data):
    """Génère une réponse experte si le LLM échoue"""
    if action == 'hypotheses':
        aapl_vol = data['aapl_vol'][0] if isinstance(data['aapl_vol'], list) else data['aapl_vol']
        btc_vol = data['btc_vol'][0] if isinstance(data['btc_vol'], list) else data['btc_vol']
        aapl_skew = data['aapl_skew'][0] if isinstance(data['aapl_skew'], list) else data['aapl_skew']
        btc_skew = data['btc_skew'][0] if isinstance(data['btc_skew'], list) else data['btc_skew']
        
        return f"""ANALYSE EXPERTE (Fallback)

=== AAPL (Apple Inc.) ===

Caracteristiques : Volatilite {aapl_vol*100:.2f}%, Asymetrie {aapl_skew:.2f}

Modeles recommandes :
1. ARIMA/SARIMA : Serie stable, modeles lineaires adaptes
2. GARCH : Clustering de volatilite
3. VAR : Analyse multivariee

=== BTC (Bitcoin) ===

Caracteristiques : Volatilite {btc_vol*100:.2f}% (soit {btc_vol/aapl_vol:.1f}x AAPL), Asymetrie {btc_skew:.2f}

Modeles recommandes :
1. GARCH/EGARCH : Volatilite extreme
2. LSTM/GRU : Patterns non-lineaires
3. VAR : Interactions avec marches traditionnels

Conclusion : AAPL necessite modeles classiques, BTC necessite approches avancees."""
    
    elif action == 'vulgarize':
        return """EXPLICATION SIMPLE (Fallback)

Apple est comme un train : previsible et stable.
Bitcoin est comme des montagnes russes : excitant mais risque.

Pour investisseurs prudents : Privilegier Apple
Pour investisseurs experimentes : Considerer Bitcoin (avec prudence)"""
    
    elif action == 'recommend':
        return """RECOMMANDATIONS EXPERTES (Fallback)

Allocation suggeree :
* 60% Apple (AAPL) : Base stable
* 25% Bitcoin (BTC) : Opportunite croissance
* 15% Liquidites : Securite

Strategies de gestion :
* Stop-loss : AAPL -15%, BTC -30%
* Reequilibrage : Tous les 3 mois
* Horizon : 3-5 ans minimum

AVERTISSEMENT : Ceci est educatif, pas un conseil financier.
Consultez un professionnel agree avant d'investir."""


def main():
    if len(sys.argv) < 3:
        print("Usage: python llm_api.py json <json_file>", file=sys.stderr)
        sys.exit(1)
    
    command = sys.argv[1]
    
    try:
        if command == "json":
            # Lire JSON
            with open(sys.argv[2], 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            action = data.get('action')
            
            # Extraire le premier élément si liste (format R)
            if isinstance(action, list) and len(action) > 0:
                action = action[0]
            
            print(f"Generation pour action: '{action}'", file=sys.stderr)
            
            # Essayer avec Flan-T5-Large
            response = None
            
            if action == 'hypotheses':
                response = generate_hypotheses_llm(data)
            elif action == 'vulgarize':
                response = generate_vulgarization_llm(data)
            elif action == 'recommend':
                response = generate_recommendations_llm(data)
            
            # Fallback sur analyse experte si LLM échoue
            if response is None:
                print("⚠️  LLM non disponible, utilisation analyse experte", file=sys.stderr)
                response = generate_fallback(action, data)
            
            if not response or len(response.strip()) == 0:
                response = "Erreur: reponse vide generee"
            
            # Retourner JSON
            result = {"response": response}
            json_output = json.dumps(result, ensure_ascii=False)
            
            print(json_output)
            sys.stdout.flush()
            
    except Exception as e:
        error_result = {"response": f"Erreur technique: {str(e)}"}
        print(json.dumps(error_result, ensure_ascii=False))
        sys.stdout.flush()
        print(f"Erreur: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
