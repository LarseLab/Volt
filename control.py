#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
import serial

cmdAtual = 'p'
assinatura = 'chatter'
modo = "manual"

def publishMode():
	global modo
	print(modo)
	pub = rospy.Publisher('control_mode', String, queue_size=10)
	rate = rospy.Rate(10) # 10hz
	pub.publish(modo)

def escreveSerial(data):
    ser = serial.Serial("/dev/ttyACM0", 115200, timeout = 1)
    ser.write(str(data))
    ser.close()

def callbackManual(data):
    global cmdAtual
    global modo
    
    rospy.loginfo('  COMANDO: %s', data.data)
    cmd = data.data
    
    if cmd == 'r' and modo == "auto":
        modo = "manual"
        escreveSerial('PAR')
        cmdAtual = 'PAR'
        publishMode()
    elif cmd == 'r' and modo == "manual":
        modo = "auto"
        publishMode()
    elif modo == "manual":
        if (cmd=='w'):
            cmd = 'FREECTEMP140'
        elif (cmd=='a'):
            cmd = 'DIRECTEMP150'
        elif (cmd=='s'):
            cmd = 'TRAECTEMP140'
        elif (cmd=='d'):
            cmd = 'ESQECTEMP150'
        else:
            cmd = 'PAR' #Para servomotores basta P, para ponte H envie 'PARA'
        
        if cmd != cmdAtual:
            escreveSerial(cmd)
            cmdAtual = cmd

def callbackAuto(data):
    global modo
        
    if modo == "auto":
        rospy.loginfo('  COMANDO: %s', data.data)
        cmd = data.data
        l, c, d = traduzirString(cmd)
        global cmdAtual
        if d > 750:
            if (c == 2):
                vel = 100 + (d - 850) / 25
                if vel > 160:
                    vel = 160
                cmd = 'FREECTEMP' + str(vel)
            elif (c == 1):
                eixo = 'EC'
                if d > 1000:
                    eixo = 'EL'
                cmd = 'DIR' + eixo + 'TEMP160'
            elif (c == 3):
                eixo = 'EC'
                if d > 1000:
                    eixo = 'EL'
                cmd = 'ESQ' + eixo + 'TEMP160'
        elif (d <= 750 and d >= 600 and c == 2) or d == 0 or d == 2047:
            cmd = 'PAR' #Para servomotores basta P, para ponte H envie 'PARA'
        elif d <= 750 and d >= 600:
            if c == 1:
                cmd = 'DIRECTEMP160'
            elif c == 3:
				cmd = 'ESQECTEMP160'
        else:
            vel = 100 - (d - 750) / 25
            if vel > 160:
                vel = 160
            cmd = 'TRAECTEMP' + str(vel)
            
        if cmd != cmdAtual:
            print(cmd)
            escreveSerial(cmd)
            cmdAtual = cmd

def callbackRequest(data):
    publishMode()


def traduzirString(stringInfo):
    # Estrutura da string: LCDDDD
    # L - Linha
    # C - Coluna
    # D - Distancia
    # Exemplo: 211730

    linha = int(stringInfo[:1])
    coluna = int(stringInfo[1:2])
    dist = int(stringInfo[2:])
    
    print(linha, coluna, dist,)
    
    return linha, coluna, dist

#
#def callback(data):
#    rospy.loginfo('  COMANDO: %s', data.data)
#    cmd = data.data
 #   ser = serial.Serial("/dev/ttyACM0", 9600, timeout = 1)
  #  ser.write(str(cmd))
   # ser.close()

def listener():
    global modo
    rospy.init_node('controle', anonymous=True)
    rospy.Subscriber('manual_control', String, callbackManual)
    print("manual_control subscribed")
    rospy.Subscriber('object_info', String, callbackAuto)
    print("object_info subscribed")
    rospy.Subscriber('request_mode', String, callbackRequest)
    print("request_mode subscribed")
    publishMode()

    #ser = serial.Serial("/dev/ttyACM0", 9600, timeout = 1)
    #ser.write('a')
    #ser.close()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
