# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

import ctypes

if win_client():
    WM_SYSCOMMAND = 274
    HWND_BROADCAST = 65535
    SC_MONITORPOWER = 61808
    success = "[+] Command successfully executed.\n"
    ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
    send(client_socket,success)
if osx_client():
    #('echo \'tell application "Finder" to sleep\' | osascript')
    resp=run_command('pmset displaysleepnow')
    send(client_socket,resp)
if lnx_client():
    resp=run_command('xset dpms force off')
    send(client_socket,resp)
