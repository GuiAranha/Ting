def exists_word(word, instance):
    data = instance.data
    result = []
    occurences = []
    for i in data:
        for index, line in enumerate(i['linhas_do_arquivo']):
            if word.lower() in line.lower():
                occurences.append({'linha': index + 1})
        if len(occurences) > 0:
            result.append({
                'palavra': word,
                'arquivo': i['nome_do_arquivo'],
                'ocorrencias': occurences
            })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
