from co2mpas_driver import dsp
import matplotlib.pyplot as plt
import numpy as np


def simple_run():
    """
        parameters of the simulation
    :return:
    """
    veh_ids = [47844]
    v_des = 124/3.6
    v_start = 0
    dt = 0.1
    times = np.arange(10, 100, dt)

    vehicles = [dsp(dict(vehicle_id=i,
                         inputs=dict(inputs={'gear_shifting_style': 0.9,
                                             'driver_style': 0.2})))
                ['outputs']['driver_simulation_model'] for i in veh_ids]
    res = {}
    for myt in times:
        # print("******************")
        for my_veh in vehicles:
            if myt == times[0]:
                my_veh.reset(v_start)
                res[my_veh] = {'accel': [0], 'speed': [v_start], 'position': [0], 'gear': [0]}
                continue

            gear, next_velocity, position, acc = my_veh(dt, v_des)
            res[my_veh]['accel'].append(acc)
            res[my_veh]['speed'].append(next_velocity)
            res[my_veh]['gear'].append(gear)
            res[my_veh]['position'].append(position)

    for my_veh in vehicles:
        plt.figure('Acceleration-Speed')
        plt.plot(res[my_veh]['speed'], res[my_veh]['accel'])
        plt.show()
    return 0


simple_run()