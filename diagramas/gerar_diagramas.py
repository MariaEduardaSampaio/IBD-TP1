"""Gera diagramas/er.png (notação de Chen) e diagramas/relacional.png.

Uso (na raiz do repositório): python diagramas/gerar_diagramas.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch, Polygon, Rectangle

PASTA = Path(__file__).parent
FONTE = "DejaVu Sans"


# ---------------------------------------------------------------- Diagrama ER

ENT_W, ENT_H = 2.8, 0.9
REL_W, REL_H = 2.5, 1.2


def caixa_texto(ax, texto, xy, tamanho, peso="normal"):
    return ax.text(*xy, texto, ha="center", va="center", fontsize=tamanho,
                   fontweight=peso, family=FONTE, zorder=5)


def entidade(ax, nome, xy, fraca=False):
    x, y = xy
    ax.add_patch(Rectangle((x - ENT_W / 2, y - ENT_H / 2), ENT_W, ENT_H,
                           fc="#dbe9f6", ec="black", lw=1.4, zorder=3))
    if fraca:
        d = 0.1
        ax.add_patch(Rectangle((x - ENT_W / 2 + d, y - ENT_H / 2 + d), ENT_W - 2 * d,
                               ENT_H - 2 * d, fc="none", ec="black", lw=1.2, zorder=4))
    caixa_texto(ax, nome, xy, 11, "bold")


def relacionamento(ax, nome, xy, identificador=False, largura=REL_W):
    x, y = xy
    w, h = largura / 2, REL_H / 2
    ax.add_patch(Polygon([(x - w, y), (x, y + h), (x + w, y), (x, y - h)],
                         fc="#fbe3c6", ec="black", lw=1.4, zorder=3))
    if identificador:
        s = 0.78
        ax.add_patch(Polygon([(x - w * s, y), (x, y + h * s), (x + w * s, y), (x, y - h * s)],
                             fc="none", ec="black", lw=1.2, zorder=4))
    caixa_texto(ax, nome, xy, 9, "bold")


def atributo(ax, nome, xy, dono, chave=None, derivado=False):
    """chave: None, 'total' (sublinhado) ou 'parcial' (sublinhado tracejado)."""
    largura = 0.105 * len(nome) + 0.6
    ax.plot([dono[0], xy[0]], [dono[1], xy[1]], color="black", lw=0.9, zorder=1)
    ax.add_patch(Ellipse(xy, largura, 0.62, fc="white", ec="black", lw=1.1,
                         ls="--" if derivado else "-", zorder=3))
    t = caixa_texto(ax, nome, xy, 8.5)
    if chave:
        ax.figure.canvas.draw()
        caixa = t.get_window_extent().transformed(ax.transData.inverted())
        ax.plot([caixa.x0, caixa.x1], [caixa.y0 - 0.02] * 2, color="black", lw=0.9,
                ls="--" if chave == "parcial" else "-", zorder=5)


def ligacao(ax, entidade_xy, rel_xy, card, total=False):
    (x1, y1), (x2, y2) = entidade_xy, rel_xy
    if total:
        dx, dy = x2 - x1, y2 - y1
        n = (dx ** 2 + dy ** 2) ** 0.5
        ox, oy = -dy / n * 0.05, dx / n * 0.05
        for s in (1, -1):
            ax.plot([x1 + s * ox, x2 + s * ox], [y1 + s * oy, y2 + s * oy], color="black", lw=1, zorder=1)
    else:
        ax.plot([x1, x2], [y1, y2], color="black", lw=1, zorder=1)
    # Cardinalidade perto da entidade, deslocada para o lado da linha
    dx, dy = x2 - x1, y2 - y1
    n = (dx ** 2 + dy ** 2) ** 0.5
    d = 1.75 if abs(dx) > abs(dy) else 0.85
    px, py = x1 + dx / n * d - dy / n * 0.25, y1 + dy / n * d + dx / n * 0.25
    ax.text(px, py, card, ha="center", va="center", fontsize=11, fontweight="bold",
            color="#b03a2e", family=FONTE, zorder=6)


def diagrama_er():
    fig, ax = plt.subplots(figsize=(19, 11.5))
    ax.set_xlim(-0.5, 19.8)
    ax.set_ylim(-0.4, 11.2)
    ax.set_aspect("equal")
    ax.axis("off")

    cat, ind = (2.5, 9.0), (2.5, 4.5)
    pes, reg, pai = (9.5, 8.0), (9.5, 1.5), (16.0, 4.75)
    pert, med, abr = (2.5, 6.75), (6.0, 4.75), (9.5, 4.75)
    real, loc = (13.5, 8.0), (13.5, 1.5)

    # Ligações entidade-relacionamento (desenhadas primeiro, ficam por baixo)
    ligacao(ax, cat, pert, "1")
    ligacao(ax, ind, pert, "N", total=True)
    ligacao(ax, ind, med, "P")
    ligacao(ax, pes, med, "M")
    ligacao(ax, reg, med, "N")
    ligacao(ax, pes, abr, "M", total=True)
    ligacao(ax, reg, abr, "N", total=True)
    ligacao(ax, pes, real, "N", total=True)
    ligacao(ax, pai, real, "1")
    ligacao(ax, reg, loc, "N", total=True)
    ligacao(ax, pai, loc, "1")

    # Atributos
    atributo(ax, "category_id", (0.6, 10.5), cat, chave="total")
    atributo(ax, "category_name", (2.9, 10.7), cat)
    atributo(ax, "category_name_pt", (5.4, 10.3), cat)
    atributo(ax, "category_area", (5.6, 9.0), cat)
    atributo(ax, "indicator_code", (0.9, 3.0), ind, chave="total")
    atributo(ax, "indicator_description", (2.6, 2.2), ind)
    atributo(ax, "indicator_type", (4.6, 3.1), ind)
    atributo(ax, "value", (4.4, 6.0), med)
    atributo(ax, "standard_error", (6.1, 6.9), med)
    atributo(ax, "SurveyId", (7.9, 9.8), pes, chave="total")
    atributo(ax, "year", (9.9, 10.4), pes)
    atributo(ax, "CMC_interview_mean", (12.1, 9.7), pes, derivado=True)
    atributo(ax, "interview_year_mean", (12.9, 5.85), abr)
    atributo(ax, "interview_month_mean", (13.1, 4.75), abr)
    atributo(ax, "CMC_interview_mean", (12.9, 3.65), abr)
    atributo(ax, "region_num_harmonized", (7.1, 0.3), reg, chave="parcial")
    atributo(ax, "region_name_harmonized", (11.4, 0.3), reg)
    atributo(ax, "country_code", (17.5, 6.4), pai, chave="total")
    atributo(ax, "country_name", (18.6, 4.75), pai)
    atributo(ax, "continent", (17.5, 3.1), pai)

    # Relacionamentos e entidades (por cima das linhas)
    relacionamento(ax, "Pertence", pert)
    relacionamento(ax, "Medição", med)
    relacionamento(ax, "ColetaPesquisaRegiao", abr, largura=3.6)
    relacionamento(ax, "Realizada_em", real)
    relacionamento(ax, "Localizada_em", loc, identificador=True)
    entidade(ax, "CategoriaIndicador", cat)
    entidade(ax, "Indicador", ind)
    entidade(ax, "Pesquisa", pes)
    entidade(ax, "Região", reg, fraca=True)
    entidade(ax, "País", pai)

    fig.savefig(PASTA / "er.png", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------- Diagrama relacional

ROW_H, TAB_W = 0.42, 4.6

# (nome, posição do canto superior esquerdo, colunas como (nome, é_pk, é_fk))
TABELAS = {
    "Pais": ((0.0, 10.0), [("country_code", 1, 0), ("country_name", 0, 0),
                           ("continent", 0, 0)]),
    "CategoriaIndicador": ((0.0, 3.6), [("category_id", 1, 0), ("category_name", 0, 0),
                                        ("category_name_pt", 0, 0), ("category_area", 0, 0)]),
    "Regiao": ((6.4, 11.0), [("country_code", 1, 1), ("region_num_harmonized", 1, 0),
                             ("region_name_harmonized", 0, 0)]),
    "Pesquisa": ((6.4, 7.6), [("SurveyId", 1, 0), ("country_code", 0, 1), ("year", 0, 0),
                              ("CMC_interview_mean", 0, 0)]),
    "Indicador": ((6.4, 3.4), [("indicator_code", 1, 0), ("indicator_description", 0, 0),
                               ("indicator_type", 0, 0), ("category_id", 0, 1)]),
    "ColetaPesquisaRegiao": ((12.8, 11.0), [("SurveyId", 1, 1), ("country_code", 1, 1),
                               ("region_num_harmonized", 1, 1), ("interview_year_mean", 0, 0),
                               ("interview_month_mean", 0, 0), ("CMC_interview_mean", 0, 0)]),
    "Medicao": ((12.8, 6.0), [("measurement_id", 1, 0), ("SurveyId", 0, 1), ("country_code", 0, 1),
                              ("region_num_harmonized", 0, 1), ("indicator_code", 0, 1),
                              ("value", 0, 0), ("standard_error", 0, 0)]),
}

# (tabela origem, coluna origem, tabela destino, coluna destino, curvatura, cor)
FKS = [
    ("Regiao", "country_code", "Pais", "country_code", 0.15, "#1f77b4"),
    ("Pesquisa", "country_code", "Pais", "country_code", -0.15, "#1f77b4"),
    ("Indicador", "category_id", "CategoriaIndicador", "category_id", -0.2, "#2ca02c"),
    ("ColetaPesquisaRegiao", "SurveyId", "Pesquisa", "SurveyId", 0.0, "#d62728"),
    ("ColetaPesquisaRegiao", "country_code", "Regiao", "country_code", 0.0, "#9467bd"),
    ("Medicao", "SurveyId", "Pesquisa", "SurveyId", 0.0, "#d62728"),
    ("Medicao", "country_code", "Regiao", "region_num_harmonized", 0.0, "#9467bd"),
    ("Medicao", "indicator_code", "Indicador", "indicator_code", 0.15, "#ff7f0e"),
]


def linha_y(tabela, coluna):
    (_, topo), colunas = TABELAS[tabela]
    i = [c[0] for c in colunas].index(coluna)
    return topo - ROW_H * (i + 1.5)


def diagrama_relacional():
    fig, ax = plt.subplots(figsize=(17, 11))
    ax.set_xlim(-0.3, 17.7)
    ax.set_ylim(1.0, 11.3)
    ax.set_aspect("equal")
    ax.axis("off")

    for nome, ((x, topo), colunas) in TABELAS.items():
        ax.add_patch(Rectangle((x, topo - ROW_H), TAB_W, ROW_H, fc="#2f5d8a", ec="black", zorder=2))
        ax.text(x + TAB_W / 2, topo - ROW_H / 2, nome, ha="center", va="center", color="white",
                fontsize=11, fontweight="bold", family=FONTE, zorder=3)
        for i, (col, pk, fk) in enumerate(colunas):
            y = topo - ROW_H * (i + 2)
            ax.add_patch(Rectangle((x, y), TAB_W, ROW_H, fc="#eef3f8" if pk else "white",
                                   ec="#888", lw=0.8, zorder=2))
            marca = ("PK " if pk else "") + ("FK" if fk else "")
            ax.text(x + 0.12, y + ROW_H / 2, marca.strip(), ha="left", va="center", fontsize=7.5,
                    color="#b03a2e", fontweight="bold", family=FONTE, zorder=3)
            t = ax.text(x + 1.05, y + ROW_H / 2, col, ha="left", va="center", fontsize=9.5,
                        family=FONTE, fontweight="bold" if pk else "normal",
                        fontstyle="italic" if fk else "normal", zorder=3)
            if pk:
                fig.canvas.draw()
                caixa = t.get_window_extent().transformed(ax.transData.inverted())
                ax.plot([caixa.x0, caixa.x1], [caixa.y0 - 0.01] * 2, color="black", lw=0.9, zorder=3)
        ax.add_patch(Rectangle((x, topo - ROW_H * (len(colunas) + 1)), TAB_W,
                               ROW_H * (len(colunas) + 1), fc="none", ec="black", lw=1.4, zorder=4))

    for origem, col_o, destino, col_d, rad, cor in FKS:
        xo = TABELAS[origem][0][0]
        xd = TABELAS[destino][0][0] + TAB_W
        ax.add_patch(FancyArrowPatch((xo, linha_y(origem, col_o)), (xd, linha_y(destino, col_d)),
                                     connectionstyle=f"arc3,rad={rad}", arrowstyle="-|>",
                                     mutation_scale=14, color=cor, lw=1.4, zorder=1))

    fig.savefig(PASTA / "relacional.png", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    diagrama_er()
    diagrama_relacional()
    print("Gerados:", PASTA / "er.png", PASTA / "relacional.png")
