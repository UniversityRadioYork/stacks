import yaml
import sys
import os

if len(sys.argv) < 5:
    print("Usage: update-stack.py <stack-name> <environment-name> <image> <tag>")
    sys.exit(1)

_, STACK, ENV, IMG, TAG = sys.argv
IMG = IMG.lower()

compose_file = f"{STACK}/{ENV}-docker-compose.yml"
with open(compose_file, "r") as fd:
    compose = yaml.load(fd, yaml.SafeLoader)

for svc, data in compose["services"].items():
    if "image" in data and IMG in data["image"]:
        data["image"] = f"{IMG}:{TAG}"

with open(compose_file, "w") as fd:
    yaml.dump(compose, fd)

print(f"Updated {compose_file}.")
