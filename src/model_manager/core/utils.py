import sys
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def is_frozen() -> bool:
    return getattr(sys, "frozen", False)

def resource_path(rel_path: str, internal=False, relative=False) -> Path:
    """
    Works for:
    - normal python
    - pyinstaller --onefile
    - pyinstaller --onedir (_internal)
    """
    # dev mode
    path = Path(rel_path)
    if not is_frozen():
        logger.debug(f"Resource Dev - Not frozen: {path}")
        return path
    
    # one file or one dir mode 
    exe_dir = Path(sys.executable).parent
    if internal:
        if hasattr(sys, "_MEIPASS"):
            logger.debug(f"Resource internal _MEIPASS: {path}")
            path = Path(sys._MEIPASS) / rel_path
            return path
        
        _internal = exe_dir / "_internal"
        if not _internal.exists():
            logger.exception("Ordner _internal nicht gefunden!")
            raise FileNotFoundError("Ordner _internal nicht gefunden!")
        logger.debug(f"Resource internal: {path}")
        path = _internal / rel_path
        return path
    
    if relative:
        path = exe_dir / rel_path
        logger.debug(f"Resource relative: {path}")
        return path
    
    # relative to shortcut
    logger.debug(f"Resource shortcut: {path}")
    return Path(path)

    



def rreplace(s:str, old:str, new:str, occurrence:int=-1):
        """
        Replace substring in a string from the right
        
        :param s: string to replace from the right
        :type s: str
        :param old: substring to be replaced
        :type old: str
        :param new: substring to replace
        :type new: str
        :param occurrence: number of occurences
        :type occurrence: int
        """
        li = s.rsplit(old, occurrence)
        return new.join(li)