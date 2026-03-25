def converter_likes(valor):
    try:
        valor = valor.replace(",", "").strip()

        if valor.endswith("M"):
            return float(valor[:-1]) * 1_000_000
        elif valor.endswith("K"):
            return float(valor[:-1]) * 1_000
        else:
            return int(valor)
    except:
        return 0


def transformar(dados):
    for item in dados:
        item["likes"] = converter_likes(item["likes"])

    dados = sorted(dados, key=lambda x: x["likes"], reverse=True)

    return dados