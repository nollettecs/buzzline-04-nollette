"""
project_consumer_nollette.py

Consumes messages from Kafka and updates a real-time pie chart displaying 
the frequency of action words in the messages.
"""

#####################################
# Import Modules
#####################################

import json
import os
import time
import random
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
from dotenv import load_dotenv

# Import Kafka only if available
try:
    from kafka import KafkaConsumer
    KAFKA_AVAILABLE = True
except ImportError:
    KAFKA_AVAILABLE = False

# Import logging utility
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

load_dotenv()

#####################################
# Define Constants
#####################################

ACTIONS = ["found", "saw", "tried", "shared", "loved"]
action_counts = defaultdict(int)

COLORS = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33A8"]  # Bright colors

#####################################
# Configure Matplotlib for Dark Theme
#####################################

mplstyle.use("dark_background")

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor("#121212")  # Dark background

#####################################
# Kafka Consumer Setup
#####################################

def get_kafka_topic() -> str:
    return os.getenv("PROJECT_TOPIC", "buzzline-topic")

def get_kafka_server() -> str:
    return os.getenv("KAFKA_SERVER", "localhost:9092")

topic = get_kafka_topic()
kafka_server = get_kafka_server()

consumer = None
if KAFKA_AVAILABLE:
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=kafka_server,
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
            auto_offset_reset="earliest",
            group_id="action-consumer-group"
        )
        logger.info(f"Kafka consumer connected to {kafka_server}, listening on topic '{topic}'")
    except Exception as e:
        logger.error(f"Kafka connection failed: {e}")
        consumer = None
else:
    logger.warning("Kafka is not available. Running in local mode.")

#####################################
# Update Chart Function
#####################################

def update_chart(_):
    """
    Fetch messages from Kafka, update action word counts, and refresh the pie chart.
    """
    global action_counts

    # Consume messages
    if consumer:
        for message in consumer:
            data = message.value
            text = data.get("message", "")

            # Update counts for each action word found
            for action in ACTIONS:
                if action in text:
                    action_counts[action] += 1
                    logger.info(f"Updated count for '{action}': {action_counts[action]}")

            break  # Process only one message per update to avoid delays

    # Ensure there is at least one non-zero value (to prevent NaN errors)
    if all(value == 0 for value in action_counts.values()):
        labels = ["Waiting for data..."]
        sizes = [1]  # Placeholder size
        colors = ["gray"]
    else:
        labels = action_counts.keys()
        sizes = action_counts.values()
        colors = COLORS

    # Update the pie chart
    ax.clear()
    ax.set_title("Cole Nollette Real-Time Action Word Frequency", fontsize=18, color="white")

    patches, texts, autotexts = ax.pie(
        sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140
    )

    # Style text elements
    for text in texts + autotexts:
        text.set_color("white")

#####################################
# Main Function
#####################################

def main():
    logger.info("START consumer...")
    
    if not consumer:
        logger.error("Kafka consumer is not available. Exiting...")
        return

    try:
        import matplotlib.animation as animation
        ani = animation.FuncAnimation(fig, update_chart, interval=2000)
        plt.show()
    except KeyboardInterrupt:
        logger.warning("Consumer interrupted by user.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
    finally:
        if consumer:
            consumer.close()
            logger.info("Kafka consumer closed.")
        logger.info("Consumer shutting down.")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()
