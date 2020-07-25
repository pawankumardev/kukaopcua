from appJar import gui

import KUKAClient
#Read Saved Configuration

startbutton = "Start Logging"


def StartedLogging():
                     
                     app.setBg("green")





f = open("savedip.txt", "r")
savedip = (f.readline())

f.close()
f = open("savedusername.txt", "r")
savedusername = (f.readline())

f.close()

f = open("savedpassword.txt", "r")
savedpassword = (f.readline())

f.close()
f = open("savedrate.txt", "r")
savedrate = (f.readline())

f.close()
f = open("savedpath.txt", "r")
savedpath = (f.readline())

f.close()
# handle button events
def press(button):
    
    f = open("savedip.txt", "w")
    
    f.write(app.getEntry("Robot IP"))
    f.close()
     
    f = open("savedusername.txt", "w")
    
    f.write(app.getEntry("Username"))
    f.close()
      
    f = open("savedpassword.txt", "w")
    
    f.write(app.getEntry("Password"))
    f.close()
     
     
    f = open("savedrate.txt", "w")
    
    f.write(app.getEntry("Sampling Rate"))
    f.close()
     
    f = open("savedpath.txt", "w")
    
    f.write(app.getEntry("Selected Directory"))
    f.close()
     
     
     
     
     
 
    
    
    
    
    
    
    
    if button == "Choose Logging Directory":
        path = app.directoryBox(title="Folder to save into", dirName=None)
        print("Selected Folder Path"+path)
        app.setEntry("Selected Directory",path)

    
    
    if button == "Save & Exit":
        app.stop()
        
    if button == "Start Logging":
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)

        startbutton = "Logging Started with"+ savedrate
        
       
        
        
        
        
        
        KUKAClient.startLogging(savedip,savedusername,savedpassword,savedrate,savedpath)










# create a GUI variable called app
app = gui("Login Window", "1200x600")
app.setBg("orange")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addImage("simple", "kuka.gif")

app.addLabel("title", "KUKA OPC UA CSV Logger V1.0")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")

app.addLabelEntry("Robot IP")
app.addLabelEntry("Username")

app.addLabelEntry("Password")

app.addLabelEntry("Sampling Rate")



#Restore Saved Data
app.setEntry("Robot IP", savedip)
app.setEntry("Username", savedusername)
app.setEntry("Password", savedpassword)
app.setEntry("Sampling Rate", savedrate)






# link the buttons to the function called press
app.addButtons(["Choose Logging Directory",startbutton, "Save & Exit"], press)
app.addLabelEntry("Selected Directory")

app.setEntry("Selected Directory",savedpath)
# start the GUI

app.addLabelEntry("Logging Status")
app.setEntry("Logging Status","Logging Stopped")

app.go()
