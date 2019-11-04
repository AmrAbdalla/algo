from LayerClass import *

network = [
    # layer 0 list of cells --> cell is defined by (ativation_func,num_of_inputs,option[bias])
    [(Neuron.logsig,10) , (Neuron.logsig,10) , (Neuron.logsig,10)],
    # layer 1 cells
    [(Neuron.logsig,3) , (Neuron.logsig,3)],
    # layer 2 cells
    [(Neuron.logsig,10)]
]

input_map_list = [
    # layer 0 mapping
    [
        # cell 0 list of mapping --> cell map [(selectinput_func,[all:dummy_val , range:range_tuple, ranges:list_of_ranges, element:index ]), ....]
        [(Layer.selectinputall, 0)],
        # cell 1 list of mapping
        [(Layer.selectinputall, 0)],
        # cell 2 list of mapping
        [(Layer.selectinputall, 0)],
    ],

    # layer 1 mapping
    [
        # cell 0 list of mapping
        [(Layer.selectinputall, 0)],
        # cell 1 list of mapping
        [(Layer.selectinputall, 0)],
    ],
    # layer 2 mapping
    [
        # cell 0 list of mapping
        [(Layer.selectinputall, 0)],
    ]
]