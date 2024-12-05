import requests
import json
import tkinter as tk
from tkinter import messagebox


# blocklist-ipsets
def get_repo_info(reosit_imja):
    url = f'github.com/firehol/{}'
    response = requests.get(url)

    if response.status_code == 200:
        repo_data = response.json()
        repo_info = {
            'company': None,
            'created at': repo_data.get('created_at'),
            'email': None,
            'id': repo_data.get('id'),
            'name': repo_data.get('name'),
            'url': repo_data.get('html_url')
        }
        return repo_info
    else:
        messagebox.showerror('Ошибка', 'Репозиторий не найден')


def button_click():
    reosit_imja = entry.get()
    if reosit_imja:
        repo_info = get_repo_info(reosit_imja)
        if repo_info:
            with open(f'{reosit_imja}_info.json', 'w') as json_file:
                json.dump(repo_info, json_file, indent=4)
            messagebox.showinfo("Отлично", f"Информация о репозитории сохранена в файл '{reosit_imja}_info.json'")
    else:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите имя репозитория.")


root = tk.Tk()
root.title('repo info')

tk.Label(root, text='Введите имя репозитория:', ).pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Получить информацию", command=button_click)
button.pack(pady=20)

root.mainloop()