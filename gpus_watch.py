#!/usr/bin/env python3

import os
import wandb
import time
import logging

# Configure logging
logging.basicConfig(
    filename='watch.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

def main():
    # Initialize wandb
    wandb.init(
        project="gpus",  # Project name
        name="test",  # Run name
        config={
            "description": "Background GPU monitoring script",
            # Add more configuration parameters if needed
        }
    )

    logging.info("GPU's Watch started.")

    try:
        while True:
            # Replace this with your actual monitoring logic
            metric = 42  # Example metric
            wandb.log({"metric": metric})
            logging.info(f"Logged metric: {metric}")
            time.sleep(60)  # Sleep for 60 seconds
    except KeyboardInterrupt:
        logging.info("Monitoring script interrupted by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        wandb.finish()
        logging.info("Wandb run finished.")

if __name__ == "__main__":
    main()
