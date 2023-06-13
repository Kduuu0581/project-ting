from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if any(item["nome_do_arquivo"] == path_file for item in instance.queue):
        print("[!] O arquivo %s já foi processado anteriormente" % path_file)
        return
    lines = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    instance.enqueue(data)
    return print(f"{data}\n")


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    path_file = instance.dequeue()['nome_do_arquivo']
    return sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
