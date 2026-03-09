是一份專為 GIS 工程師 打造的 uv Workspace 標準作業程序（SOP）。這套命令能幫你快速建構出「多專案、多共用庫」的開發環境。1. 初始化工作區 (Workspace Root)首先建立大本營，並將其轉化為管理中心。PowerShell# 建立並進入根目錄
mkdir myworkspace
cd myworkspace

# 初始化為虛擬專案 (不含 build-system，純管理用)
uv init --lib

# 建立子目錄結構
mkdir apps
mkdir packages

# 編輯 pyproject.toml 加入以下內容：
# [tool.uv.workspace]
# members = ["apps/*", "packages/*"]
2. 建立共用庫 (Shared Packages)共用庫放在 packages/ 下，建議使用 src-layout。PowerShell# 建立共用設定庫 (例如你剛才做的 config-base)
uv init --lib packages/config-base

# 建立 GIS 核心運算庫 (未來可以放 PostGIS, Shapely 邏輯)
uv init --lib packages/gis-core
命名慣例： 資料夾用 config-base (kebab-case)，程式碼導入用 import config_base (snake_case)。3. 建立個別專案 (Individual Apps)個別應用程式放在 apps/ 下，它們會引用上面的共用庫。PowerShell# 建立第一個 GIS 應用專案
uv init --app apps/a01

# 建立第二個數據處理專案
uv init --app apps/data-processor
4. 建立專案間的連結 (Linking)這是最關鍵的一步。你需要進入每個 apps 的目錄修改其 pyproject.toml。以 apps/a01/pyproject.toml 為例：Ini, TOML[project]
name = "a01"
dependencies = [
    "config-base",  # 宣告要用共用庫
    "gis-core",     # 宣告要用 GIS 核心
]

[tool.uv.sources]
config-base = { workspace = true } # 指向工作區成員
gis-core = { workspace = true }
5. 日常管理常用命令表這套命令能幫你在 Windows 環境下流暢開發。功能命令說明同步全域環境uv sync在根目錄執行，會更新 uv.lock 並安裝所有成員依賴。執行特定專案uv run --package a01 python apps/a01/main.py無論在何處，皆能正確載入工作區環境執行。新增外部套件uv add --package a01 geopandas將 geopandas 只安裝給 a01 專案。新增共用套件uv add --package config-base pydantic-settings讓共用庫具備讀取環境變數的能力。清理環境uv clean移除不再需要的快取與遺留檔案。6. GIS 工程師的實戰技巧VS Code 設定：請務必開啟 myworkspace（根目錄），並選擇 .venv/Scripts/python.exe 作為解析器，紅字才會消失。.env 定位：如前所述，在 AppSettings 中使用 Path(__file__).resolve().parent.parent 來鎖定 .env 絕對路徑，解決不同目錄執行時的 ValidationError。這套 SOP 應該能讓你的 GeoAI 專案有個完美的開始。你想試著把 PostGIS 的連線邏輯封裝進新的 packages/gis-core 嗎？