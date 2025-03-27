import os
import sys
from pathlib import Path

# Ensure we're running from the project root
project_root = Path(__file__).parent
os.chdir(project_root)

try:
    import uvicorn
    from dotenv import load_dotenv
    from loguru import logger
except ImportError as e:
    print(f"ERROR: Missing required package - {e}")
    print("Please run: poetry install")
    sys.exit(1)

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    try:
        # Configure settings from environment variables with defaults
        port = int(3000)
        host = "localhost"
        log_level = os.getenv("LOG_LEVEL", "info").lower()
        reload_mode = os.getenv("RELOAD", "true").lower() == "true"
        
        print(f"Starting server on {host}:{port}")
        print(f"Log level: {log_level}")
        print(f"Reload mode: {'enabled' if reload_mode else 'disabled'}")
        print("Press CTRL+C to stop the server")
        
        # Check if main.py exists
        if not Path("main.py").exists():
            print("ERROR: main.py not found in current directory")
            print(f"Current directory: {os.getcwd()}")
            sys.exit(1)
        
        uvicorn.run(
            "main:app",
            host=host,
            port=port,
            reload=reload_mode,
            log_level=log_level
        )
    except Exception as e:
        print(f"Failed to start server: {e}")
        sys.exit(1)