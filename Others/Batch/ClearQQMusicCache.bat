@echo off
REM �رջ���

REM bat�ļ����ܣ�ɾ��QQ���ֻ���

REM ָ��Ŀ���ļ���·��
set "targetFolder=D:\Applications\Tencent\QQMusic\QQMusicCache"

REM ���Ŀ���ļ����Ƿ����
if exist "%targetFolder%" (
    REM ɾ��Ŀ���ļ����µ������ļ�
    del /q "%targetFolder%\*"
    REM ɾ��Ŀ���ļ����µ��������ļ��м�������
    for /d %%p in ("%targetFolder%\*") do rmdir /s /q "%%p"
    
    echo �����ļ������ļ�����ɾ����
) else (
    echo Ŀ���ļ��в����ڡ�
)

REM ��ͣ�Ա�鿴���
pause