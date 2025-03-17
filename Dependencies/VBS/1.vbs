option explicit
dim x,y,z,a,wshshell,loopState,askName
Set WshShell = WScript.CreateObject("WScript.Shell")

Sub main
    
    x=msgbox ("Just wait there Python. Let me talk now.",16+0,"Yes")
    if x=vbOk then
    msgbox "Yeah, let me introduce myself. I am VBS, and you are?",64+0,"?"
    end if
    
    askName = "Type Your Name Here"
    loopState = True
    do while loopState=True
    
    y=inputbox(askName, "Type Here")

    if not Len(Trim(y))=0 then
    loopState = False
    else
    askName = UCase(askName) & "!"
    end if

    loop

    select case LCase(y) 

    case "sanil"
    msgbox "Well, you know what will happen. I'll just go away...",16+0,"Good for me right?"
    exit sub

    case "shreyas"
    msgbox "Well, you too know what will happen, so I shall get going...",16+0,"Good for me again, right?"
    exit sub

    end select

    msgbox "Nice name you got there " & y & "!", 64+0, "Indeed!"

    z=msgbox ("Let me tell you one thing.",64+0,"?")
    if z=vbOk then
    msgbox "Yeah, so I think Python is pretty wierd...It is too demanding... It should learn to be grateful from me.",48+0,"It is"
    msgbox "Like, which language is even case sensitive nowadays...",64+0,"Super annoying tbh"
    end if
    a=msgbox ("Do you hate Python?",64+4,"What do you think?")
    if a=vbYes then
    msgbox "I knew it! nobody likes Python. (Laughs)",48+0,"HAHAHHA"
    elseif a=vbNo then
    msgbox "What no? You like it really?",64+0,":("
    end if

end Sub

main