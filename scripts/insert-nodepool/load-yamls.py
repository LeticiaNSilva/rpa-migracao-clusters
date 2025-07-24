import yaml

def load_repos(caminho_repos):
    """Função utilizada para carregar os repositorios especificados em 
    /config/repos.yaml"""
    with open(caminho_repos, "r") as f:
        arquivo = yaml.safe_load(f)
        return arquivo.get("repos", [])
    
# TEST
# caminho_reposi = "scripts/insert-nodepool/config/configuration.yaml"
# teste = load_repos(caminho_reposi)
# print(teste)

def load_provider(caminho_provider):
    """Função utilizada para carregar o provedor nodepool do time de observabilidade"""
    with open(caminho_provider, "r") as f:
        arquivo = yaml.safe_load(f)
        return arquivo.get("provider", [])
    
# TEST
# caminho_provider = "scripts/insert-nodepool/config/configuration.yaml"
# teste_provider = load_provider(caminho_provider)
# print(teste_provider)

def load_branch_and_commit(caminho_git):
    """ Função para retornar as informações que serão utilizadas para operações GIT"""
    with open(caminho_git, "r") as f:
        arquivo= yaml.safe_load(f)
        return arquivo.get("git_branch", ""), arquivo.get("git_commit_mensage", "")
    
#TEST
# caminho_git = "scripts/insert-nodepool/config/configuration.yaml"
# git_branch, git_commit_menssage = load_branch_and_commit(caminho_git)
# print(git_branch)
# print(git_commit_menssage)
