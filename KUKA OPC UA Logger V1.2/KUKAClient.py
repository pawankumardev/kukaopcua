from opcua import Client
import time
import csv


def startLogging(ip,username,password,rate,path):



                print("Starting")
                print(ip)
                print(username)
                print(password)
                print(rate)
                print(path)
                url = "opc.tcp://192.168.1.20:4840" 
                
                client = Client(url)
                
                #KUKA_OPC_UA_Logger_GUI.gui.setEntry("Logging Status","Logging Started")
                #KUKA_OPC_UA_Logger_GUI.startbutton = "Logging Active"
                
                print("try session connect")
                
                client.set_user("opcuaoperator")
                
                client.set_password("kuka")
                
                
                print("session success")
                
                
                client.connect()
                
                print("Client Connected to KUKA OPC Server")
                
                
                lograte = 0.1
                
                
                
                while True:
                        
                        
                        now = time.strftime('%d-%m-%Y %H:%M:%S')
                        
                        
                        # Force in X Direction
                        
                        variablename = "ForceinX"
                        variableid = client.get_node("ns=5;s=MotionDeviceSystem.ProcessData.R1.System.$config.FX_FT")
                        variabledata = variableid.get_value()
                        print(variablename)
                        print(variabledata)
                     
                        
                        myFile = open("E:/test.csv", 'w')
                        
                        
                        with myFile:
                         writer = csv.writer(myFile)
                         writer.writerows([now,now])
                         with open("E:/"+variablename+".csv", "a") as log:
                             log.write("{0},{1}\n".format(now,str(variabledata)))
                        
                        
                        
                        
                        
                         # Force in Y Direction
                        
                         variablename = "ForceinY"
                        variableid = client.get_node("ns=5;s=MotionDeviceSystem.ProcessData.R1.System.$config.FY_FT")
                        variabledata = variableid.get_value()
                        print(variablename)
                        print(variabledata)
                     
                        
                        myFile = open("E:/test.csv", 'w')
                        
                        
                        with myFile:
                         writer = csv.writer(myFile)
                         writer.writerows([now,now])
                         with open("E:/"+variablename+".csv", "a") as log:
                             log.write("{0},{1}\n".format(now,str(variabledata)))
                        
                        
                        
                        
                        
                        
                        
                        
                         # Force in Z Direction
                        
                        
                        
                         variablename = "ForceinZ"
                        variableid = client.get_node("ns=5;s=MotionDeviceSystem.ProcessData.R1.System.$config.FZ_FT")
                        variabledata = variableid.get_value()
                        print(variablename)
                        print(variabledata)
                     
                        
                        myFile = open("E:/test.csv", 'w')
                        
                        
                        with myFile:
                         writer = csv.writer(myFile)
                         writer.writerows([now,now])
                         with open("E:/"+variablename+".csv", "a") as log:
                             log.write("{0},{1}\n".format(now,str(variabledata)))
                        
                        
                        
                         # Torque in X Direction
                        
                         variablename = "TorqueinX"
                        variableid = client.get_node("ns=5;s=MotionDeviceSystem.ProcessData.R1.System.$config.TX_FT")
                        variabledata = variableid.get_value()
                        
                        print(variablename)
                        print(variabledata)
                     
                        
                        myFile = open("E:/test.csv", 'w')
                        
                        
                        with myFile:
                         writer = csv.writer(myFile)
                         writer.writerows([now,now])
                         with open("E:/"+variablename+".csv", "a") as log:
                             log.write("{0},{1}\n".format(now,str(variabledata)))
                        
                        
                                # Torque in X Direction
                        
                         variablename = "TorqueinY"
                        variableid = client.get_node("ns=5;s=MotionDeviceSystem.ProcessData.R1.System.$config.TY_FT")
                        variabledata = variableid.get_value()
                        print(variablename)
                        print(variabledata)
                     
                        
                        myFile = open("E:/test.csv", 'w')
                        
                        
                        with myFile:
                         writer = csv.writer(myFile)
                         writer.writerows([now,now])
                         with open("E:/"+variablename+".csv", "a") as log:
                             log.write("{0},{1}\n".format(now,str(variabledata)))
                        
                                # Torque in X Direction
                        
                         variablename = "TorqueinZ"
                        variableid = client.get_node("ns=5;s=MotionDeviceSystem.ProcessData.R1.System.$config.TZ_FT")
                        variabledata = variableid.get_value()
                        print(variablename)
                        print(variabledata)
                     
                        
                        myFile = open("E:/test.csv", 'w')
                        
                        
                        with myFile:
                         writer = csv.writer(myFile)
                         writer.writerows([now,now])
                         with open("E:/"+variablename+".csv", "a") as log:
                             log.write("{0},{1}\n".format(now,str(variabledata)))
                        
                        
                        
                        
                        
                        
                        time.sleep(lograte)