import sys
import os
#sys.path.append('../')
sys.path.append(os.path.relpath('../'))
from make_keyboard import make_kb

config_dict = """{
    "name": "square",
    "row_key_numbers": [
        4,
        4,
        4,
        4
    ],
    "columnSpacing": 19,
    "rowSpacing": 19,
    "plateThickness": 2,
    "screwHoleDiamater": 2.4,
    "switchHoleSize": 13.97,
    "shape": 0,
    "notched_keyhole": true,
    "caseHeight": 18,
    "caseGap": 0.6,
    "wallThickness": 2.0,
    "floorThickness": 3.0,
    "edgeFillet": 6,
    "bottomFillet": 2,
    "plateEdgeOffset":-1,
    "controller": {
        "name": "Pi Pico",
        "board_dimension_x": 51.0,
        "board_dimension_y": 21.0,
        "screw_hole_x": 47.0,
        "screw_hole_y": 11.4
    },
    "controllerYOffset": 5,
    "controllerBoxThickness": 2
}"""


def cut_holes_in_top_plate(top):
    led_num=4
    led_spacing = 3.8

    led_posns = [(led_spacing,led_spacing),(-led_spacing,led_spacing), 
                 (led_spacing,-led_spacing), (-led_spacing,-led_spacing)]
    led_hole_dia = 5.15

    #cut holes for LEDs
    for i in range(0,led_num):
        pos = led_posns[i]
        top= (top.faces('>Z').workplane(centerOption="CenterOfBoundBox")
            .moveTo(pos[0], pos[1])
            .circle(0.5*led_hole_dia)
            .cutThruAll()
        )


    return top

def cut_aviator_connector_hole(case):

    aviator_hole_dia = 6.25
    aviator_flat_width = 5.3
    aviator_hole_height =  -1

    case = (case.faces(">Y").workplane(centerOption='CenterOfBoundBox')
                    .center(0,aviator_hole_height)
                    .moveTo(-0.5*aviator_flat_width, -((0.5*aviator_hole_dia)**2 - (0.5*aviator_flat_width)**2)**0.5)
                    .threePointArc((0, -0.5*aviator_hole_dia), (0.5*aviator_flat_width, -((0.5*aviator_hole_dia)**2 - (0.5*aviator_flat_width)**2)**0.5))
                    .lineTo(0.5*aviator_flat_width,((0.5*aviator_hole_dia)**2 - (0.5*aviator_flat_width)**2)**0.5)
                    .threePointArc((0, 0.5*aviator_hole_dia), (-0.5*aviator_flat_width, ((0.5*aviator_hole_dia)**2 - (0.5*aviator_flat_width)**2)**0.5))
                    .close()
                    .cutBlind(until='next')
                    )
    return case 


make_kb(config_dict, cut_holes_in_top_plate, cut_aviator_connector_hole)