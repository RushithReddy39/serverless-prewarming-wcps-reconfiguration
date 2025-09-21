# config.py

WINDOW_SIZE = 5  # Time window for calculating invocation trend (in minutes)
MAX_CONTAINERS = 10  # Max containers that can be pre-warmed
PREWARM_COUNT = 2  # Number of containers to prewarm when rising
TERMINATE_COUNT = 2  # Number of containers to terminate when falling
