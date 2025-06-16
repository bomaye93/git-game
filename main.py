import os
import subprocess

def pause():
    input("➡️  Appuie sur Entrée quand tu as terminé...")

def check_git_initialized():
    return os.path.isdir(".git")

def check_file_staged(filename):
    result = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True)
    return filename in result.stdout.strip().split('\n')

def check_commit_made():
    result = subprocess.run(["git", "log", "--oneline"], capture_output=True, text=True)
    return result.stdout.strip() != ""

def level_1():
    print("🎯 Niveau 1 : Initialise un dépôt Git avec `git init`")
    pause()
    if check_git_initialized():
        print("✅ Dépôt Git initialisé !\n")
        return True
    print("❌ Ce dossier n’est pas encore un dépôt Git.\n")
    return False

def level_2():
    print("🎯 Niveau 2 : Crée un fichier `note.txt`, écris un mot dedans, puis ajoute-le avec `git add note.txt`")
    pause()
    if check_file_staged("note.txt"):
        print("✅ Fichier ajouté à l’index !\n")
        return True
    print("❌ `note.txt` n’est pas encore ajouté.\n")
    return False

def level_3():
    print("🎯 Niveau 3 : Fais un commit avec `git commit -m \"Ajout de note.txt\"`")
    pause()
    if check_commit_made():
        print("✅ Bravo, tu as fait ton premier commit !\n")
        return True
    print("❌ Aucun commit détecté.\n")
    return False

def main():
    print("🎮 Bienvenue dans Git Game !\n")
    if not level_1():
        return
    if not level_2():
        return
    if not level_3():
        return
    print("🎉 Félicitations, tu maîtrises les bases de Git ! 🔥")

if __name__ == "__main__":
    main()
