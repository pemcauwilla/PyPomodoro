from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class AppColors():
    BG_COLOR: str = "#001233"
    SECOND_BG_COLOR: str = "#001845"
    THIRD_BG_COLOR: str = "#002855"

    PRIMARY_TXT_COLOR: str = "#f5f3f4"
    SECONDARY_TXT_COLOR: str = "#eef4ed"
    DARKER_TXT_COLOR: str = "#134074"

    PRIMARY_BORDER_COLOR: str = "#82a4c7"
    SECONDARY_BORDER_COLOR: str = "rgba(191, 219, 247, 0.1)"

    PRESSED_BORDER_COLOR: str = "#3d5a80"

    DROP_SHADOW_COLOR: str = "#ffffff"

@dataclass(frozen=True)
class FontSize():
    X_SMALL_FONT_SIZE: str = "12px"
    SMALL_FONT_SIZE: str = "16px"
    NORMAL_FONT_SIZE: str = "20px"
    SUBTITLE_FONT_SIZE: str = "24px"
    TITLE_FONT_SIZE:  str = "32px"
    
    TIMER_FONT_SIZE: str = "96px"

class StyleManager():
    @staticmethod
    def get_complete_stylesheet() -> str:
        complete_qss_file : str = ""
        # The order of the files matter, so each qss file should have a number prefix according to its specificity 
        # (More general files first)
        for qss_file in Path("assets/").glob('*.qss'):
            with qss_file.open() as qss:
                complete_qss_file = complete_qss_file + StyleManager._parse_qss(qss.read()) + '\n'

        return complete_qss_file

    @staticmethod
    def _parse_qss(qss_txt : str) -> str:
        new_qss_txt : str = qss_txt
        for key, value in AppColors.__dataclass_fields__.items():
            new_qss_txt = new_qss_txt.replace(f"@{key}", value.default)

        for key, value in FontSize.__dataclass_fields__.items():
            new_qss_txt = new_qss_txt.replace(f"@{key}", value.default)

        return new_qss_txt


if __name__ == "__main__":
    qss = StyleManager.get_complete_stylesheet()

    print(qss)