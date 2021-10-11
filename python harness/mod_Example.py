'''
This example code module implements two actions:
- "hello world", which creates a report line saying "hello world"
- "check sort order", which verifies the sorting order in a table

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

import cv2

# import the functions of TestArchitect
from lib_abt import *
# import image processing function
from image_lib import *

# set module name
moduleName = "example"

# declare the actions for the module
def SetActions():
    LIBRARY.SetActionScript("hello world", moduleName, 1)
    LIBRARY.SetActionScript("check sort order", moduleName, 1)
    LIBRARY.SetActionScript("convert image to grayscale", moduleName, 1)
    LIBRARY.SetActionScript("clear identical pagagraph in images", moduleName, 1)
    LIBRARY.SetActionScript("clear word in image", moduleName, 1)
    
# map an action to its function
# note: this function is called by ta_main's DivertToModule function, it should return:
# - True to tell DivertToModule that the custom action has been consumed
# - False if it cannot handle the action
def Divert(actionName):
    result = True
    if actionName == "hello world":
        action_helloWorld()
    elif actionName == "check sort order":
        action_checkSortOrder()
    elif actionName == "convert image to grayscale":
        action_convertToGrayscale()
    elif actionName == "clear identical pagagraph in images":
        action_clearIdenticalParagraph()
    else:
        result = False
        LIBRARY.ReportError("Don't know action: " + actionName)
        
    return result

# "hello world" action implementation
def action_helloWorld():
    LIBRARY.Report("hello world")

# check sort order <window> <table> <column>
# loop through rows of a table and verify that the values order in a given column are ascending
def action_checkSortOrder():
    # get the arguments and assign a label for the check
    windowName = LIBRARY.NamedArgument("window")
    tableName = LIBRARY.NamedArgument("table")
    columnName = LIBRARY.NamedArgument("column")
    checkLabel = "sort order"

    # bring window into view
    window = ABT.OpenEntity(windowName)
    if window == None:
        LIBRARY.ReportError("Cannot find window " + windowName + ".")
    else :
        window.BringToTop()

        # identify the window and the table on screen
        table = ABT.OpenElement(windowName, tableName)
        if table == None:
            LIBRARY.ReportError("could not identify table '" + tableName + "'")
            return
        
        # determine the column and the number of rows
        column = table.GetColumnIndex(columnName)
        rowCount = table.GetRowCount()
        if rowCount <= 0 :
            LIBRARY.AdministerCheck(checkLabel, "sorted", "no rows", 1)
            return
        
        # check the sort order
        previous = table.GetCellText(0, column)
        for i in range(1, rowCount):
            if table.GetCellText(i, column) < previous :
                LIBRARY.AdministerCheck(checkLabel, "sorted", "fails in row " + str(i+1), 0)
                return
            previous = table.GetCellText(i, column)
            
        LIBRARY.AdministerCheck(checkLabel, "sorted", "all rows are in order", 1)       

# convert images to grayscale
def action_convertToGrayscale():
    # get the arguments and assign a label for the check
    input_file = LIBRARY.NamedArgument("input image")
    output_file = LIBRARY.NamedArgument("output image")

    # convert to grayscale image and save 
    image = cv2.imread(input_file)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_file, grayscale)

# clear identical paragraph in two images
def action_clearIdenticalParagraph():
    # get the arguments and assign a label for the check
    base_input_image = LIBRARY.NamedArgument("base input image")
    target_input_image = LIBRARY.NamedArgument("target input image")
    base_output_image = LIBRARY.NamedArgument("base output image")
    target_output_image = LIBRARY.NamedArgument("target output image")
    indent = int(LIBRARY.NamedArgument("indent"))
    text_color = int(LIBRARY.NamedArgument("text color"))
    match_percent = int(LIBRARY.NamedArgument("match percent"))
    LIBRARY.Report(str(match_percent))
    # clear identical paragraphs in two images and save
    replace_identical_paragraph_pictures(base_input_image, target_input_image, base_output_image, target_output_image, indent, text_color, match_percent)