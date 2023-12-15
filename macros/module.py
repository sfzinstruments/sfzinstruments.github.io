import os

def define_env(env):
  @env.macro
  def path_exists(path):
    return os.path.exists(path)
