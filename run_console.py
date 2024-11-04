import os
import sys

# Set the PYTHONPATH to the src directory
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.append(src_path)

# Import and run the main script
from app.cli.main import main  # noqa: E402

if __name__ == "__main__":
    main()
