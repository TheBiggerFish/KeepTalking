from simulation import Simulation


def main():
    sim = Simulation(num_modules=1,minutes=2)
    while sim.pass_time():
        # module = int(input('There are {} modules, which to work on? '.format(len(sim.bomb.modules))))
        sim.take_action(module_index=0)
        print(sim.bomb.timer)

    if sim.bomb.is_solved():
        print("CONGRATS!")
    else:
        print("BOOM")


if __name__ == "__main__":
    main()