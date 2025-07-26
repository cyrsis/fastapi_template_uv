import sys
from pathlib import Path

# Add project root to path only if needed (won't interfere with PyCharm)
if __name__ == "__main__":
    project_root = Path(__file__).parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

import uvicorn
from loguru import logger
from services.logs import configure_logger, get_uvicorn_log_config


def main() -> None:
    configure_logger()
    logger.info("Starting app...")

    uvicorn.run(
        "app.app:app",
        log_config=get_uvicorn_log_config(),
        port=8080,
        host="0.0.0.0",
        reload=True
    )


if __name__ == "__main__":
    main()