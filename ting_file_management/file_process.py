from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)

    for i in instance.data:
        if i['nome_do_arquivo'] == path_file:
            return None

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    instance.enqueue(result)
    print(result)


def remove(instance):
    if not instance:
        return print('Não há elementos')
    file = instance.dequeue()
    print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        print(result)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
