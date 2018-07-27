from state_machine import State, Event, acts_as_state_machine, after, before, InvalidStateTransition


@acts_as_state_machine
class Process:
    # 状态机的状态
    created = State(initial=True)  # 创建
    waiting = State()  # 等待
    running = State()  # 运行
    terminated = State()  #终止
    blocked = State()  # 阻塞
    swapped_out_waiting = State()  # 切换到等待
    swapped_out_blocked = State()  # 切换到阻塞

    # 定义 状态 之间的关系
    wait = Event(from_states=(created, running, blocked,
                              swapped_out_waiting), to_state=waiting)
    run = Event(from_states=waiting, to_state=running)
    terminate = Event(from_states=running, to_state=terminated)
    block = Event(from_states=(running, swapped_out_blocked),
                  to_state=blocked)
    swap_wait = Event(from_states=waiting, to_state=swapped_out_waiting)
    swap_block = Event(from_states=blocked, to_state=swapped_out_blocked)

    def __init__(self, name):
        self.name = name

    @after('wait')  # 之后
    def wait_info(self):
        print('{} entered waiting mode'.format(self.name))  # {} 进入等待模式.

    @after('run')
    def run_info(self):
        print('{} is running'.format(self.name))  # {} 正在运行.

    @before('terminate')  # 之前
    def terminate_info(self):
        print('{} terminated'.format(self.name))  # {} 终止.

    @after('block')
    def block_info(self):
        print('{} is blocked'.format(self.name))  # {} 被阻塞.

    @after('swap_wait')
    def swap_wait_info(self):
        print('{} is swapped out and waiting'.format(self.name))  # {} 被切换到等待

    @after('swap_block')
    def swap_block_info(self):
        print('{} is swapped out and blocked'.format(self.name))  # {} 被切换到阻塞


def transition(process, event, event_name):  # 转换(状态机 的切换)
    try:
        event()
    except InvalidStateTransition as err:  # InvalidStateTransition::失败的状态切换
        print('Error: transition of {} from {} to {} failed'.format(process.name,
                                                                    process.current_state, event_name))


def state_info(process):  # 状态_信息
    print('state of {}: {}'.format(process.name, process.current_state))


def main():
    RUNNING = 'running'  # 运行
    WAITING = 'waiting'  # 等待
    BLOCKED = 'blocked'  # 阻塞
    TERMINATED = 'terminated'  # 终止

    p1, p2 = Process('process1'), Process('process2')
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.wait, WAITING)
    transition(p2, p2.terminate, TERMINATED)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.run, RUNNING)
    transition(p2, p2.wait, WAITING)
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p2, p2.run, RUNNING)
    [state_info(p) for p in (p1, p2)]

    print()
    [transition(p, p.block, BLOCKED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]

    print()
    [transition(p, p.terminate, TERMINATED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]

if __name__ == '__main__':
    main()
