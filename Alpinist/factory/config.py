import json
from controller import Controller, ControllerFromDict
from controller import AdafruitFeathernRF52840Express



class Config:
    row_key_numbers: list
    columnSpacing: float
    rowSpacing: float
    switchHoleSize: float
    plateThickness: float
    screwHoleDiameter: float
    notched_keyhole: bool
    plateEdgeOffset: float
    
        
    caseHeight: float
    caseGap: float
    wallThickness: float
    floorThickness: float
    edgeFillet: float
    bottomFillet: float
        
    controller : Controller
    controllerYOffset : float
    controllerBoxThickness : float


        
    def __init__(self, row_key_numbers, 
                 name = None,
                 columnSpacing = 19, rowSpacing = 19, 
                 switchHoleSize = 14.0,
                 plateThickness = 1.8,
                 screwHoleDiamater = 2.4,
                 notched_keyhole = True,
                 plateEdgeOffset = -2.0,
                 
                 caseHeight = 22,
                 caseGap = 0.5,
                 wallThickness = 1.6,
                 floorThickness = 3.0,
                 edgeFillet = 4,
                 bottomFillet = 2,
                 
                 controller = AdafruitFeathernRF52840Express(),
                 controllerYOffset = 3,
                 controllerBoxThickness = 2,

                 
                 
                ):
        self.row_key_numbers = row_key_numbers
        self.name = name
        self.columnSpacing = columnSpacing
        self.rowSpacing = rowSpacing
        self.plateThickness = plateThickness
        self.screwHoleDiamater = screwHoleDiamater
        self.switchHoleSize = switchHoleSize
        self.notched_keyhole = notched_keyhole
        self.plateEdgeOffset = plateEdgeOffset
        
        self.caseHeight = caseHeight
        self.caseGap = caseGap
        self.wallThickness = wallThickness
        self.floorThickness = floorThickness
        self.edgeFillet = edgeFillet
        self.bottomFillet = bottomFillet
        
        self.controller = controller  
        self.controllerYOffset = controllerYOffset
        self.controllerBoxThickness = controllerBoxThickness

        

    def to_json(self, file):
        dict_to_write = self.__dict__.copy()
        if self.controller is not None:
            dict_to_write['controller'] = self.controller.as_dict()
        else:
             dict_to_write['controller'] = 'None'
        with open(file, 'w') as f:
            json.dump(dict_to_write, f, indent=4 )
    

def read_config_from_json( **kwargs):
        if 'string' in kwargs.keys():
            dict = json.loads(kwargs['string'])
        else:
            with open(kwargs['file'], 'r') as f:
                dict= json.load(f)

        if dict['controller'] == 'None':
            dict['controller'] = None
        else:
            dict['controller']  = ControllerFromDict(dict['controller'] )
        return Config(**dict)
