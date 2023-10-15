from gym_multirotor.envs.mujoco.quadrotor_plus_hover import QuadrotorPlusHoverEnv
import gymnasium as gym
import os
from stable_baselines3 import PPO


env = QuadrotorPlusHoverEnv()

model = PPO("MlpPolicy", env, verbose=1)
if os.path.isfile("temp.model"):
    model.load("temp.model")
# model.learn(total_timesteps=100000)

model.save("temp.model")

num_steps = 1500

obs = env.reset()

# vec_env = model.get_env()
for i in range(num_steps):
    action, _states = model.predict(obs[0], deterministic=True)
    obs, reward, done, truncs, info = env.step(action)
    env.render()
    # VecEnv resets automatically
    # if done:
    #   obs = env.reset()

env.close()
