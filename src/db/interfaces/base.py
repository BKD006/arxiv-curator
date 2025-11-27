from abc import ABC, abstractmethod
from typing import Any, ContextManager, Dict, List, Optional

from sqlalchemy.orm import Session

class BaseDatabase(ABC):
    """Base class for database interactions."""

    @abstractmethod
    def startup(self) -> None:
        """Initialize the database connection."""
        pass

    @abstractmethod
    def shutdown(self) -> None:
        """Close the database connection."""
        pass

    @abstractmethod
    def get_session(self) -> ContextManager[Session]:
        """Get a database connection"""
        pass


class BaseRepository(ABC):
    """Base repository pattern for data access"""

    def __init__(self, session: Session) -> None:
        self.session = session

    @abstractmethod
    def create(self, data: Dict[str, Any]) -> Any:
        """Create a new record in the database."""
        pass

    @abstractmethod
    def get_by_id(self, record_id: Any) -> Optional[Any]:
        """Retrieve a record by its ID."""
        pass

    @abstractmethod
    def update(self, record_id: Any, data: Dict[str, Any]) -> Optional[Any]:
        """Update an existing record by its ID."""
        pass

    @abstractmethod
    def delete(self, record_id: Any) -> bool:
        """Delete a record by its ID."""
        pass

    @abstractmethod
    def list(self, skip: int = 100, offset: int = 0) -> List[Any]:
        """List records with pagination."""
        pass