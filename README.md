# Calculadora interativa em Python

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IamPriime/calculadora-python/blob/main/calculadora.ipynb)

Calculadora de terminal com quatro operações, menu contínuo e proteção contra divisão por zero.

Projeto de estudo de **Gabriel / [IamPriime](https://github.com/IamPriime)**, desenvolvido a partir de um notebook do Google Colab e organizado para portfólio. O foco é mostrar a lógica implementada e permitir que outra pessoa execute o projeto.

## O que o projeto faz

- Soma, subtrai, multiplica e divide.
- Mantém o menu aberto até a opção de saída.
- Trata divisão por zero e entradas numéricas inválidas.

## Tecnologias e conceitos

Python 3.10+ · funções · controle de fluxo · validação de entradas.

## Como executar

```bash
git clone https://github.com/IamPriime/calculadora-python.git
cd calculadora-python
python -m venv .venv
```

Ative o ambiente: no Windows PowerShell, `.venv\Scripts\Activate.ps1`; no macOS/Linux, `source .venv/bin/activate`.

```bash
python -m pip install -r requirements.txt
python calculadora.py
```

No Colab, use o botão no início deste README. Execute a célula e responda às entradas interativas.

## Exemplo e interpretação

Exemplo: escolha `1`, informe `10` e `5` e obtenha `Resultado: 15`. Escolha `0` para encerrar. Use ponto para separar casas decimais.

## Estrutura

| Arquivo | Função |
| --- | --- |
| `calculadora.ipynb` | Notebook para Colab/Jupyter, sem saídas antigas |
| `calculadora.py` | Versão executável localmente |
| `requirements.txt` | Indicação de que não há dependências externas |


## Origem e melhorias

Origem no Colab: `calculadora.ipynb`. O arquivo no Drive foi preservado. Organizadas as operações em funções, corrigida a apresentação da subtração e adicionada validação de entrada. As saídas de execução e os metadados pessoais do notebook foram removidos da versão publicada.

## Limitações

Projeto educacional executado no terminal. Não inclui banco de dados, interface web ou persistência.

## Próximos passos

- Adicionar persistência e ampliar a cobertura de cenários de entrada.
- Separar a interface de terminal da lógica para facilitar futuras interfaces.

## Autoria e uso

Organização de estudos de [IamPriime](https://github.com/IamPriime). Nenhuma licença de software foi escolhida para este repositório.
