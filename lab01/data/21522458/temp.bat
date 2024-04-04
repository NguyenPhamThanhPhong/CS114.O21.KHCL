
for /l %%i in (0,1,10) do (
    echo Copying from "%%i\%%i.jpg" to "%%i\%%i.1.jpg"
    copy "%%i\%%i.jpg" "%%i\%%i.1.jpg"
)

pause