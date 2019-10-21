"""
Test functionality of Native Calculator Application on Ubuntu 17.04
"""
import logging
import sys
import os
import subprocess as subp
import unittest

calculator = "/usr/bin/gnome-calculator"

# to execute an os command
def exec_proc(cmd,shell=True):
    try:
        if shell:
            process = subp.Popen(cmd, shell=True, stdout=subp.PIPE, stderr=subp.PIPE)
        else:
            process = subp.Popen(cmd, shell=False, stdout=subp.PIPE, stderr=subp.PIPE)
        retcode=process.wait()
        if retcode:
            return None
        else:
            output=process.communicate()
            res=" ".join(str(line) for line in output)
            return res
    except Exception, e:
        print("Problem executing command: ", cmd)
        return 3


# 1. Run calculator 
def run_calculator(calculator):
    # Find Calculator application and run it.
    try:
        if os.path.isfile(calculator):
            display=os.environ['DISPLAY']
            print "Running calculator: ", calculator, "Display: " , display
            bg_calculator=calculator + "&"
            res=exec_proc(calculator)
            print "Ended process"
        else:
            print "Couldn't find calculator :", calculator
    except Exception, e:
        logging.error('Error find_calculator :%s' %e)


# 2. unittest for operation results
def execute_operation(cmdrun):
    res=exec_proc(cmdrun)
    return 0

class ValidaSumTestCase(unittest.TestCase):
    def test_is_four(self):
        # Verify sum: 2 + 2 = 4.
        operation="2+2"
        cmdrun=calculator + " -s " + operation
        res=exec_proc(cmdrun)
        self.assertEqual(int(res), 4)

def verify_addition():
    unittest.main()
    return 0

# 3. Change mode of calculator
def change_mode():
    # Switch Calculator from Basic to Advanced mode.
    # Switch Calculator from Advanced to Financial mode.
    curMode="/usr/bin/gsettings get org.gnome.calculator button-mode ;"
    resMode=exec_proc(curMode)
    desMode=resMode
    print "Current mode is:",resMode,"-"
    answerMode='N'
    if str(resMode).rstrip('\r\n') == 'basic':
       answerMode = raw_input("Change Basic to Advanced mode Y/N? ")
       desMode = 'advanced'
    elif str(resMode).rstrip('\r\n')  == 'advanced':
       answerMode = raw_input("Change Advanced to Financial mode Y/N? ")
       desMode = 'financial'
    if answerMode == 'Y':
        print "Changing settings to ", desMode
        newMode="/usr/bin/gsettings set org.gnome.calculator button-mode ", desMode
        res=exec_proc(newMode)
    print "Updated Current mode is: ", resMode
    # add unittest to validate.... - pending 
    return 0

# 4. Set options
def set_preferences():
    # Verify Options
    # Open Preferences Menu for Calculator. 
    # Verify the following options exist:
    # Number formats: Automatic, Fixed, Scientific, Engineering
    # Show Decimal Places: Verify you can change decimal places unit.
    # Show trailing zeroes & Show thousands of separators: Verify you can check and uncheck these options.
    # Angle Units: Degrees, Radians, Gradians
    # Word size: 8, 16, 32, 64 bits.
    # Verify you can close the Preferences menu. 
    return 0


def menu():
    print "Options ->"
    choice = 0
    choice = int(raw_input("1:ran calculator   2:verify operation 3:change mode 4:verify preferences  99:quit -> "))
    while True:
        if choice == 1:
            run_calculator(calculator)
            break
        elif choice == 2:
            verify_addition()
            break
        elif choice == 3:
            change_mode()
            break
        elif choice == 4:
            set_preferences()
            break
        else:
            break
    return 0


menu()

