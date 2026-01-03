"""
Main CLI entry point for BONSAI TODO APP.

This module initializes and runs the main application loop.
"""
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.master_agent import TodoCLI_MasterAgent


def main() -> None:
    """Main entry point for the CLI application."""
    print("BONSAI TODO APP")
    print("Initializing...")
    master_agent = TodoCLI_MasterAgent()
    master_agent.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        sys.exit(0)
