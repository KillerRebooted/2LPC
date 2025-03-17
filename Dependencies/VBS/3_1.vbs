option explicit
dim c,d,e,wshshell, objFSO, scriptDir, scriptPath, objWMI, objProcess, strProcess

Set wshshell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")
scriptDir = objFSO.GetParentFolderName(WScript.ScriptFullName)

scriptPath = """" & scriptDir & "\VBS Dependencies\Video Transparency.py" & """"
wshShell.Run scriptPath, 0, False
c=msgbox ("With this Treasure! I Summon...",48+0,"MAHORAGAAA")
if c=vbOk then
scriptPath = """" & scriptDir & "\VBS Dependencies\Block Keyboard.py" & """"
wshShell.Run scriptPath, 0, False
WshShell.run "cmd"
WScript.sleep 2000
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "U"
WScript.sleep 100
WshShell.Sendkeys "h"
WScript.sleep 100
WshShell.Sendkeys ","
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "V"
WScript.sleep 100
WshShell.Sendkeys "B"
WScript.sleep 100
WshShell.Sendkeys "S"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "J"
WScript.sleep 100
WshShell.Sendkeys "u"
WScript.sleep 100
WshShell.Sendkeys "s"
WScript.sleep 100
WshShell.Sendkeys "t"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "S"
WScript.sleep 100
WshShell.Sendkeys "t"
WScript.sleep 100
WshShell.Sendkeys "a"
WScript.sleep 100
WshShell.Sendkeys "r"
WScript.sleep 100
WshShell.Sendkeys "t"
WScript.sleep 100
WshShell.Sendkeys "e"
WScript.sleep 100
WshShell.Sendkeys "d"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "m"
WScript.sleep 100
WshShell.Sendkeys "e"
WScript.sleep 100
WshShell.Sendkeys "."
WScript.sleep 100
WshShell.Sendkeys "."
WScript.sleep 100
WshShell.Sendkeys "."
WScript.sleep 700
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "M"
WScript.sleep 100
WshShell.Sendkeys "a"
WScript.sleep 100
WshShell.Sendkeys "y"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "I"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "A"
WScript.sleep 100
WshShell.Sendkeys "s"
WScript.sleep 100
WshShell.Sendkeys "k"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "W"
WScript.sleep 100
WshShell.Sendkeys "h"
WScript.sleep 100
WshShell.Sendkeys "y"
WScript.sleep 100
WshShell.Sendkeys "?"
WScript.sleep 1000
wshshell.sendkeys "{ENTER}"
wshshell.sendkeys "exit"
wshshell.sendkeys "{ENTER}"
strProcess = "python.exe"
Set objWMI = GetObject("winmgmts:\\.\root\cimv2")
For Each objProcess In objWMI.ExecQuery("SELECT * FROM Win32_Process WHERE Name = '" & strProcess & "'")
    objProcess.Terminate
Next
end if

d=msgbox ("Yeah, so Python here is being very rude to me!. Am I right?",48+4,"Support me")
if d=vbYes then
msgbox "As I said! Python is very weird... I suggest you close it right this moment.",64+0,"Thank you"

scriptPath = """" & scriptDir & "\VBS Dependencies\Block Keyboard.py" & """"
wshShell.Run scriptPath, 0, False
WshShell.run "cmd"
WScript.sleep 1000
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "W"
WScript.sleep 100
WshShell.Sendkeys "e"
WScript.sleep 100
WshShell.Sendkeys "l"
WScript.sleep 100
WshShell.Sendkeys "l"
WScript.sleep 100
WshShell.Sendkeys ","
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "I"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "n"
WScript.sleep 100
WshShell.Sendkeys "e"
WScript.sleep 100
WshShell.Sendkeys "e"
WScript.sleep 100
WshShell.Sendkeys "d"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "t"
WScript.sleep 100
WshShell.Sendkeys "o"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "h"
WScript.sleep 100
WshShell.Sendkeys "e"
WScript.sleep 100
WshShell.Sendkeys "a"
WScript.sleep 100
WshShell.Sendkeys "r"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "P"
WScript.sleep 100
WshShell.Sendkeys "y"
WScript.sleep 100
WshShell.Sendkeys "t"
WScript.sleep 100
WshShell.Sendkeys "h"
WScript.sleep 100
WshShell.Sendkeys "o"
WScript.sleep 100
WshShell.Sendkeys "n"
WScript.sleep 100
WshShell.Sendkeys "'"
WScript.sleep 100
WshShell.Sendkeys "s"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "s"
WScript.sleep 100
WshShell.Sendkeys "i"
WScript.sleep 100
WshShell.Sendkeys "d"
WScript.sleep 100
WshShell.Sendkeys "e"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "t"
WScript.sleep 100
WshShell.Sendkeys "o"
WScript.sleep 100
WshShell.Sendkeys "o"
WScript.sleep 100
WshShell.Sendkeys "."
WScript.sleep 100
WshShell.Sendkeys "."
WScript.sleep 100
WshShell.Sendkeys "."
WScript.sleep 900
wshshell.sendkeys "{ENTER}"
wshshell.sendkeys "exit"
wshshell.sendkeys "{ENTER}"
strProcess = "python.exe"
Set objWMI = GetObject("winmgmts:\\.\root\cimv2")
For Each objProcess In objWMI.ExecQuery("SELECT * FROM Win32_Process WHERE Name = '" & strProcess & "'")
    objProcess.Terminate
Next

msgbox "But...",16+0,":("
elseif d=vbNo then
msgbox "Uhh, Mr. Command Prompt... I guess no one witnessed this event, Python was being really rude with me. I can prove it...",16+0,"I am angry with ya"
end if

scriptPath = """" & scriptDir & "\VBS Dependencies\Block Keyboard.py" & """"
wshShell.Run scriptPath, 0, False
WshShell.run "cmd"
WScript.sleep 1000
WshShell.Sendkeys "COLOR 40"
wshshell.sendkeys "{ENTER}"
WshShell.Sendkeys "cls"
wshshell.sendkeys "{ENTER}"
WshShell.Sendkeys " "
WshShell.Sendkeys "S"
WScript.sleep 20
WshShell.Sendkeys "I"
WScript.sleep 20
WshShell.Sendkeys "L"
WScript.sleep 20
WshShell.Sendkeys "E"
WScript.sleep 20
WshShell.Sendkeys "N"
WScript.sleep 20
WshShell.Sendkeys "C"
WScript.sleep 20
WshShell.Sendkeys "E"
WScript.sleep 20
WshShell.Sendkeys "!"
WScript.sleep 2000
wshshell.sendkeys "{ENTER}"
WshShell.Sendkeys "COLOR 07"
wshshell.sendkeys "{ENTER}"
WshShell.Sendkeys "cls"
wshshell.sendkeys "{ENTER}"
WshShell.Sendkeys " "
WScript.sleep 20
WshShell.Sendkeys "W"
WScript.sleep 100
WshShell.Sendkeys "e"
WScript.sleep 100
WshShell.Sendkeys "l"
WScript.sleep 100
WshShell.Sendkeys "l"
WScript.sleep 100
WshShell.Sendkeys ","
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "J"
WScript.sleep 100
WshShell.Sendkeys "u"
WScript.sleep 100
WshShell.Sendkeys "s"
WScript.sleep 100
WshShell.Sendkeys "t"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "s"
WScript.sleep 100
WshShell.Sendkeys "a"
WScript.sleep 100
WshShell.Sendkeys "v"
WScript.sleep 100
WshShell.Sendkeys "e"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "i"
WScript.sleep 100
WshShell.Sendkeys "t"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "V"
WScript.sleep 100
WshShell.Sendkeys "B"
WScript.sleep 100
WshShell.Sendkeys "S"
WScript.sleep 100
WshShell.Sendkeys "!"
WScript.sleep 1000
wshshell.sendkeys "{ENTER}"
wshshell.sendkeys "exit"
wshshell.sendkeys "{ENTER}"
WScript.sleep 2000
WshShell.run "cmd"
WScript.sleep 1000
WshShell.Sendkeys " "
WScript.sleep 20
WshShell.Sendkeys "Y"
WScript.sleep 100
WshShell.Sendkeys "e"
WScript.sleep 100
WshShell.Sendkeys "s"
WScript.sleep 100
WshShell.Sendkeys ","
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "y"
WScript.sleep 100
WshShell.Sendkeys "o"
WScript.sleep 100
WshShell.Sendkeys "u"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "m"
WScript.sleep 100
WshShell.Sendkeys "a"
WScript.sleep 100
WshShell.Sendkeys "y"
WScript.sleep 100
WshShell.Sendkeys " "
WScript.sleep 100
WshShell.Sendkeys "c"
WScript.sleep 100
WshShell.Sendkeys "o"
WScript.sleep 100
WshShell.Sendkeys "n"
WScript.sleep 100
WshShell.Sendkeys "t"
WScript.sleep 100
WshShell.Sendkeys "i"
WScript.sleep 100
WshShell.Sendkeys "n"
WScript.sleep 100
WshShell.Sendkeys "u"
WScript.sleep 100
WshShell.Sendkeys "e"
WScript.sleep 100
WshShell.Sendkeys "."
WScript.sleep 100
WshShell.Sendkeys "."
WScript.sleep 100
WshShell.Sendkeys "."
WScript.sleep 1000
wshshell.sendkeys "{ENTER}"
wshshell.sendkeys "exit"
wshshell.sendkeys "{ENTER}"

strProcess = "python.exe"
Set objWMI = GetObject("winmgmts:\\.\root\cimv2")
For Each objProcess In objWMI.ExecQuery("SELECT * FROM Win32_Process WHERE Name = '" & strProcess & "'")
    objProcess.Terminate
Next