import time

import mujoco
import mujoco.viewer

m = mujoco.MjModel.from_xml_path("cfd_tests/quadrotor_plus.xml")
d = mujoco.MjData(m)

mujoco.viewer.launch(m, d)
exit
with mujoco.viewer.launch_passive(m, d) as viewer:
    # Close the viewer automatically after 30 seconds.
    start = time.time()
    while viewer.is_running() and time.time() - start < 30:
        step_start = time.time()

        # The mj_step call can be replaced with a user-defined function that evaluates
        # a policy, applies a control signal, and steps an environment.
        mujoco.mj_step(m, d)
        # Example of modifying a viewer option: toggle contact points every second.
        with viewer.lock():
            viewer.opt.flags[mujoco.mjtVisFlag.mjVIS_CONTACTPOINT] = int(d.time % 2)

        # Synchronize so that the viewer picks up changes to the physics state.
        viewer.sync()

        # Rudimentary time keeping, doesn't attempt to catch up if physics stepping
        # takes too long.
        time_until_next_step = m.opt.timestep - (time.time() - step_start)
        if time_until_next_step > 0:
            time.sleep(time_until_next_step)

        # round all accelerations to 2 decimal places
        acel = [round(x, 2) for x in d.qacc_smooth]
        print("Lift force: ", acel)
