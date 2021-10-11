'''
Example "main" script for interpreting TestArchitect(tm) tests in Python.

A harness consists typically of a main module and one or more "script modules" that
host the functions to implement actions.
 
Recommended steps to create a new script module with actions:
- create a python script module
- add the following to the module:
    - a "setActions()" function that declares the actions to be implemented
    - a "divertAction" function that maps the actions to functions that implement them
    - a function for each action that the module needs to support, suggested name action_Something
- add an "import" statement here to import the module
- add a call in main() here to the module's "setActions" function.
- add a line in the divert() function here to direct actions to the new module

Disclaimer:
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND 
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS 
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, 
OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT 
OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import lib_interpret as Interpreter
import mod_Example as Example

# the entry point
def main():
    # initialize the TestArchitect interpreter
    Interpreter.Init()
    
    # register actions (add your "setActions" functions here)
    Example.SetActions()
    
    # interpret the test
    Interpreter.Interpret()
    
    # finish the test run
    Interpreter.End()

# divert the action to a script module
# note: this function is called by the interpreter, it should return:
# - True to tell the interpreter that the custom action has been consumed
# - False if it cannot handle action from the module
def DivertToModule(moduleName, actionName):
    if moduleName == Example.moduleName:
        return Example.Divert(actionName)
    else:
        Interpreter.LIBRARY.ReportError("Don't know action: " + actionName)
        return False
    
# start the Python program by executing the "main" function
Interpreter.divertFunction = DivertToModule # let the interpreter know what to call
main()
