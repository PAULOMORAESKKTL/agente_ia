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
- API Anthropic (via `.env`)
- Arquivos `.csv` e `.txt` como base de dados

## 📁 Estrutura

```plaintext
agente_ia/
├── dados/
│   ├── avaliacoes/
│   └── lista_de_consumo/
├── analisador_de_sentimentos.py
├── categorizador.py
├── identificador_de_perfil.py
├── helpers.py
├── base.py
├── main.py
├── requirements.txt
├── .gitignore


 📦 Como instalar e executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/PAULOMORAESKKTL/agente_ia.git
   cd agente_ia
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
ANTHROPIC_API_KEY="sua-chave-aqui"
python main.py

---

## 🔒 Segurança

```markdown
## 🔒 Segurança

Este projeto utiliza um arquivo `.env` para armazenar informações sensíveis, como a chave da API da Anthropic. Para manter segurança:

- `.env` está no `.gitignore` e **não será versionado**
- Cada colaborador deve criar o seu próprio `.env` local
- Para uso colaborativo, recomenda-se incluir um `.env.example` com a estrutura:

```env
ANTHROPIC_API_KEY=your_api_key_here

---

## ✍️ Autor e Licença

```markdown
## ✍️ Autor

Projeto desenvolvido por **Paulo Moraes** como parte dos estudos em Inteligência Artificial aplicada ao comportamento de consumo.

## 📄 Licença

Distribuído sob os termos da [MIT License](LICENSE.md).






