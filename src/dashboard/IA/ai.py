def gerar_resumo(webtoon):
    titulo = webtoon["titulo"]
    genero = webtoon["genero"]
    likes = webtoon["likes"]

    if genero.lower() == "action":
        estilo = "ação intensa e cheia de adrenalina"
    elif genero.lower() == "fantasy":
        estilo = "fantasia envolvente com mundos incríveis"
    elif genero.lower() == "sci-fi":
        estilo = "ficção científica com conceitos futuristas"
    else:
        estilo = "uma história envolvente"

    if likes > 1000000:
        popularidade = "um verdadeiro sucesso entre os leitores"
    elif likes > 100000:
        popularidade = "bastante popular"
    else:
        popularidade = "uma boa opção para descobrir"

    resumo = f"{titulo} é um webtoon de {estilo}. Com {likes} likes, é {popularidade} e vale muito a pena conferir!"

    return resumo