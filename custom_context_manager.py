import time


class TimerContextManager:
    def __enter__(self):
        self.start_time = time.time()
        return self  # Мы можем вернуть любой объект, который будет связан с as

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Time elapsed: {elapsed_time} seconds")


a = 0
# Используем контекстный менеджер
with TimerContextManager() as timer:
    # Ваш код, время выполнения которого мы хотим замерить
    for _ in range(100):
        time.sleep(0.2)
        a += 1

print(a)
