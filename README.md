# agente_ia

Sistema de análise e categorização de perfis de consumidores com uso de inteligência artificial aplicada a avaliações textuais.

## 🚀 Objetivo

Este projeto foi desenvolvido como parte do curso de programação orientado à aplicação de IA. Seu objetivo principal é:

- Coletar e interpretar **avaliações de restaurantes**
- Analisar os textos usando técnicas de **Processamento de Linguagem Natural (NLP)**
- Detectar **sentimentos**, **categorias de consumo** e **perfil de clientes**
- Gerar insights para recomendação personalizada ou estratégias de mercado

## 🛠️ Tecnologias

- Python 3
- Pandas, NumPy
- NLTK ou spaCy (dependendo da análise)
- APIs externas (como Anthropic, via `.env`)
- Arquivos `.csv` e `.txt` como base de dados

## 📁 Estrutura

```plaintext
├── dados/
│   ├── avaliacoes/
│   └── lista_de_consumo/
├── analisador_de_sentimentos.py
├── categorizador.py
├── identificador_de_perfil.py
├── main.py
├── requirements.txt
## 📦 Como instalar e executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/PAULOMORAESKKTL/agente_ia.git
   cd agente_ia
