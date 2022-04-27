import time

from pypaq.mpython.mptools import ExSubprocess, Que


def demo_kill():

    class SubP(ExSubprocess):

        def __init__(self, **kwargs):
            self.que = Que()
            ExSubprocess.__init__(self, **kwargs)

        def subprocess_method(self):
            #for _ in range(3):
            while True:
                msg = 'running subprocess method'
                print(msg)

                time.sleep(2)

                qm = {'type':'info','data':msg}
                self.oque.put(qm)
                self.que.put(qm)


    in_que = Que()
    out_que = Que()

    sbp = SubP(
        ique=   in_que,
        oque=   out_que,
        verb=   1)
    print(f'@@@ after init: {sbp.get_info()}')

    sbp.start()
    print(f'@@@ after start: {sbp.get_info()}')

    time.sleep(6)

    sbp.kill()
    print(f'@@@ after kill: {sbp.get_info()}')

    sbp.terminate()
    print(f'@@@ after terminate: {sbp.get_info()}')

    sbp.join()
    print(f'@@@ after join: {sbp.get_info()}')

    sbp.close()
    print(f'@@@ after close: {sbp.get_info()}')


if __name__ == '__main__':

    demo_kill()