# TP — Introdução a Banco de Dados (DCC011)

Saúde reprodutiva e planejamento familiar das mulheres, a partir da base LivWell (Kaggle).

## Estrutura

```
TP_IBD.ipynb        Relatório de entrega (seções 1–7); a Seção 3 recria o banco do zero
data/raw/           Dados originais do Kaggle (livwell.csv, indicators.csv)
data/processed/     filtered_indicators.csv — os 100 indicadores selecionados pelo grupo
diagramas/          Diagramas ER e relacional (a fazer; ver docs/doc_modelo_de_dados_v2.pdf)
docs/               Enunciado e proposta
exploratorio/       Notebooks antigos de exploração (não fazem parte da entrega)
```

## Como executar

Abra `TP_IBD.ipynb` na raiz do repositório e execute todas as células (requer `pandas`).
O banco `saudefeminina.db` é gerado pelo notebook e não é versionado.
