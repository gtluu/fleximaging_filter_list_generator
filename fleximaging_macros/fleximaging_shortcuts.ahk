#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#Persistent
SetTimer,Tab,500
Return

Tab:
Send,{Right}
Return

Pause::Pause
Return

F2::
Send,^m
Send,{Tab}
Send,{Tab}
Send,{Tab}
Send,{Tab}
Send,{Tab}
Send,^c
Send,+{Tab}
Send,+{Tab}
Send,+{Tab}
Send,+{Tab}
Send,+{Tab}
Send,^v
Send,{Enter}
Return