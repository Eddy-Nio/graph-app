from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class AppConfig:
    """Application configuration"""
    DEBUG: bool = False
    MAX_RETRIES: int = 3
    DEFAULT_MATRIX_PATH: str = "./data/matrix.txt"
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'AppConfig':
        return cls(**{
            k: v for k, v in config_dict.items() 
            if k in cls.__annotations__
        })