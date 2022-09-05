import enum
import threading
from time import sleep


class States(enum.Enum):
    DYING = 1  # 初期値
    DEAD = 2
    # ALIVE = # この定義は禁止


class Morieru(threading.Thread):
    def __init__(self):
        super().__init__()
        self.state = States.DYING
        self.event = threading.Event()

    def run(self):
        print("もりえるの仕事が始まる……")
        self.event.clear()

        while self.state == States.DYING:
            print("もりえるは穴を掘っては埋めています。")
            self.event.wait(1.0)

        print("もりえるは自分で掘った穴に埋葬されました。")

    def kill(self):
        print("……エンッ!")
        self.state = States.DEAD
        self.event.set()


if __name__ == "__main__":
    morieru = Morieru()
    morieru.start()
    sleep(5)
    morieru.kill()
