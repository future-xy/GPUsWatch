#!/usr/bin/env python3

import wandb
import time
import datetime
import logging

# Configure logging
logging.basicConfig(
    filename='watch.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

def main():
    # Generate run name based on timestamp
    run_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Initialize wandb
    wandb.init(
        project="gpus",  # Project name
        name=run_name,  # Run name
        config={
            "description": "Background GPU monitoring script",
            # Add more configuration parameters if needed
        }
    )

    logging.info("GPU's Watch started.")

    try:
        while True:
            time.sleep(6)  # Sleep for 6 seconds
    except KeyboardInterrupt:
        logging.info("Monitoring script interrupted by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        wandb.finish()
        logging.info("Wandb run finished.")

if __name__ == "__main__":
    main()
