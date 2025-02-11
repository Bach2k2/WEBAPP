from os.path import exists, dirname, join
# from pathlib import Path

import environ

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = dirname(dirname(dirname(__file__)))
print('bb',BASE_DIR)
# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = join(BASE_DIR, "config.env")
if not exists(env_file):
    env_file = "/etc/backend/config.env"

if exists(env_file):
    environ.Env.read_env(str(env_file))
