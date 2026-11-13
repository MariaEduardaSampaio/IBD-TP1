# TP — Introdução a Banco de Dados (DCC011)

Saúde reprodutiva e planejamento familiar das mulheres, a partir da base LivWell (Kaggle).

## Estrutura

```
TP_IBD.ipynb  Relatório da entrega final (seções 1–7); a Seção 3 recria o banco do zero
TP_IBD_parcial.ipynb   Relatório da entrega parcial (seções 1–5)
ibd012-eda/         Atividade de análise exploratória em SQL (IBD012) com os mesmos dados
data/raw/           Dados originais do Kaggle (livwell.csv, indicators.csv)
data/processed/     filtered_indicators.csv — os 100 indicadores selecionados pelo grupo
diagramas/          Diagrama ER (diagrama_er.png) e diagrama relacional (diagrama_relacional.png)
docs/               Enunciado e proposta
exploratorio/       Notebooks antigos de exploração (não fazem parte da entrega)
```

## Como executar

Abra `TP_IBD.ipynb` na raiz do repositório e execute todas as células (requer `pandas` e `matplotlib`).
O banco `saudefeminina.db` é gerado pelo notebook e não é versionado.
