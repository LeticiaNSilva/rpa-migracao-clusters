import yaml
import subprocess
import os
from scripts.insert_nodepool.load_yamls import load_repos,load_branch_and_commit


caminho_repos = "scripts/insert-nodepool/config/configuration.yaml"
def git_operations():
    """ This function will be used to perform git operations such as checkout and commit. """
    repositories = load_repos(caminho_repos)
    branch, commit_mensage = load_branch_and_commit(caminho_repos)

    for repo in repositories:
        repo_nome = repo.split("/")[-1]

        print(f"\nRepositório atual: {repo}")

        # 1. Clonar
        if not os.path.exists(repo_nome):
            subprocess.run(f"gh repo clone {repo}")
            print("clone OK")
        else:
            print(f"Repositório {repo} já foi clonado.")

        # 2. Criar nova branch
        subprocess.run(f"git checkout -b {branch}", cwd=repo_nome)

        # 3. Add tudo
        subprocess.run("git add .", cwd=repo_nome)

        # 4. Commit
        subprocess.run(f'git commit -m "{commit_mensage}"', cwd=repo_nome)

        # 5. (Opcional) Push e abrir PR
        

        print(f"- Repo {repo_nome} processado com sucesso!")
