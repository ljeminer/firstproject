tasks = []

def add_task():
    print('Напишите задачу:')
    task = input()
    tasks.append(task)
    print()

def show_tasks():
    for i, k in enumerate(tasks):
        print(f'{i}. {k}')
        print()

def delete_task():
    len_tasks = len(tasks)
    num_delete = (input('Какой номер удаляем?'))

    if num_delete.isdigit():
        num_delete = int(num_delete)
        if num_delete >= len_tasks: 
            print('Такой задачи нету')
        else:
            tasks.pop(num_delete)
    else:
        print('Вы ввели не число')
    
def clear_task():
    answer = input('Вы уверены что хотите удалить список? (да/нет)')

    if answer == 'да':
        tasks.clear()
    
while True:
    print('Выберите команду:')
    print('№1 add')
    print('№2 list')
    print('№3 delete')
    print('№4 exit')
    print('№5 clear')

    answer = input('Сделайте выбор от 1-5:')

    if answer == '1':
        add_task()
    elif answer == '2':
        show_tasks()
    elif answer == '3':
        delete_task()
    elif answer == '4':
        print('Выход из программы...')
        break
    elif answer == '5':
        clear_task()
        print('Красава марат')
    else:
        print('Неверный ввод, попробуйте еще раз')