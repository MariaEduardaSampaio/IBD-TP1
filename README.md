# TP: Introdução a Banco de Dados (DCC011)

Saúde reprodutiva e planejamento familiar das mulheres, a partir da base LivWell (Kaggle).

## Estrutura

```
TP_IBD.ipynb            Relatório da entrega final (seções 1 a 8); a Seção 3 recria o banco do zero
TP_IBD_parcial.ipynb    Relatório da entrega parcial (seções 1 a 5)
data/raw/               Dados originais do Kaggle (livwell.csv e indicators.csv)
data/processed/         filtered_indicators.csv, com os 100 indicadores selecionados pelo grupo
diagramas/              Diagrama ER (diagrama_er_v2.png) e diagrama relacional (diagrama_relacional_v2.png),
                        junto com as versões anteriores
docs/                   Enunciado, proposta da 1ª entrega, documentação do modelo de dados (v2) e das consultas
ibd012-eda/             Atividade de análise exploratória em SQL (IBD012) com os mesmos dados
```

## Como executar

Abra `TP_IBD.ipynb` na raiz do repositório e execute todas as células (requer `pandas` e `matplotlib`).
O banco `saudefeminina.db` é gerado pelo notebook na raiz e não é versionado. Antes de executar de novo,
feche qualquer outro programa que esteja com o banco aberto, porque o notebook apaga e recria o arquivo.

O notebook `ibd012-eda/IBD012-eda.ipynb` lê os mesmos CSVs (`../data/`), gera o seu próprio banco
(`saudefeminina_eda.db`) e requer também `seaborn`.
