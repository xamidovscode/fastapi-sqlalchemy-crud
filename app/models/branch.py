from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Time, DateTime, Date, Text, Boolean
from app.core.database import Base

class Branch(Base):
    __tablename__ = "branches"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    start_time: Mapped[str] = mapped_column(Time(timezone=True), nullable=False)
    end_time: Mapped[str] = mapped_column(Time(timezone=True), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
