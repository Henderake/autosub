@echo off
set package_name=autosub
IF "%~1"=="" GOTO :STOP

@echo on
%~d0
cd %~dp0%
.\%package_name% -S en-US -hsp -i "%~1"

:STOP
pause