@echo off
REM 关闭回显

REM bat文件功能：删除QQ音乐缓存

REM 指定目标文件夹路径
set "targetFolder=D:\Applications\Tencent\QQMusic\QQMusicCache"

REM 检查目标文件夹是否存在
if exist "%targetFolder%" (
    REM 删除目标文件夹下的所有文件
    del /q "%targetFolder%\*"
    REM 删除目标文件夹下的所有子文件夹及其内容
    for /d %%p in ("%targetFolder%\*") do rmdir /s /q "%%p"
    
    echo 所有文件和子文件夹已删除。
) else (
    echo 目标文件夹不存在。
)

REM 暂停以便查看结果
pause