#Author-Alex Anderson
#Description-FILL THIS SECTION OUT

import adsk.core, adsk.fusion, adsk.cam, traceback

#general variables
_keyword = ''
_newWord = ''

#rename all sketch text variables with specific string
def rename():
    app = adsk.core.Application.get()
    ui = app.userInterface
    product = app.activeProduct
    design = adsk.fusion.Design.cast(product)

    _keyword = ui.inputBox('Current phrase:')
    _newWord = ui.inputBox('Rename keyword to:')
    
    childComps = design.allComponents

    sketchList = []
    sketchTextList = []

    #gets all sketches
    for comp in childComps:
        for sketch in comp.sketches:
            sketchList.append(sketch)

    ui.messageBox(str(len(sketchList)))

    #gets all sketchTexts
    for sketch in sketchList:
        if sketch.sketchTexts.count > 0:
            tempSketchTexts = sketch.sketchTexts
            for text in tempSketchTexts:
                sketchTextList.append(text)

    ui.messageBox(str(len(sketchTextList)))
            
    for sketchText in sketchTextList:
        if _keyword[0] in sketchText.text:
            #ui.messageBox('current text: ' + sketchText.text)
            sketchText.text = _newWord[0]

def run(context):
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        rename()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

#prevents code from running when imported into other plugins/scripts
#if __name__ == '__main__':
    #run()
