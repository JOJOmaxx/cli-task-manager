import sys
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "task": description, "done": False})
    save_tasks(tasks)
    print(f"[+] Tâche ajoutée : {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Aucune tâche enregistrée.")
        return
    for t in tasks:
        status = "✔" if t["done"] else " "
        print(f"[{status}] {t['id']}. {t['task']}")

def complete_task(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"[✔] Tâche {task_id} marquée comme terminée.")
            return
    print(f"Erreur : tâche {task_id} introuvable.")

def main():
    if len(sys.argv) < 2:
        print("Usage : python task.py [add|list|done] [argument]")
        return

    command = sys.argv[1]
    if command == "add" and len(sys.argv) >= 3:
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "done" and len(sys.argv) >= 3:
        complete_task(int(sys.argv[2]))
    else:
        print("Commande invalide.")

if __name__ == "__main__":
    main()
