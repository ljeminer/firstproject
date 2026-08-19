tasks = []
def add_task(name):
    tasks.append(name)
def show_tasks():
    for i, k in enumerate(tasks):
        print(f"{i+1} . {k}")
add_task("Купить хлеб")
add_task("Сделать ДЗ")
show_tasks()