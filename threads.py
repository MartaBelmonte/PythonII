import threading
import time


def print_message_without_newline(message):
    print(message, end='', flush=True)


def thread_task(message, delay):
    time.sleep(delay)
    print_message_without_newline(message)


def concurrency_with_coffee():
    print("- I'm tired, Bob! ", end='', flush=True)


    thread1 = threading.Thread(
        target=thread_task, args=("are made of coffee? ", 0))
    thread2 = threading.Thread(target=thread_task, args=("Do you know ", 1))
    thread3 = threading.Thread(target=thread_task, args=("it! ", 2))
    thread4 = threading.Thread(
        target=thread_task, args=(" that our bodies ", 3))
    thread5 = threading.Thread(target=thread_task, args=("-Try drinking ", 4))

    # Iniciar threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    # Esperar threads terminados
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    # Mensaje final
    print("- You're right!")


concurrency_with_coffee()
