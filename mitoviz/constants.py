#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste

NAMES = ["DLOOP", "TF", "RNR1", "TV", "RNR2", "TL1", "NC1",
         "ND1", "TI", "TQ", "NC2", "TM", "ND2",
         "TW", "NC3", "TA", "NC4", "TN", "TC",
         "TY", "NC5", "CO1", "TS1", "NC6", "TD",
         "CO2", "NC7", "TK", "NC8", "ATP8", "ATP6",
         "CO3", "TG", "ND3", "TR", "ND4L", "ND4",
         "TH", "TS2", "TL2", "ND5", "ND6", "TE",
         "NC9", "CYTB", "TT", "NC10", "TP"]

TYPES = ["reg", "trna", "rrna", "trna", "rrna", "trna", "nc",
         "cds", "trna", "trna", "nc", "trna", "cds",
         "trna", "nc", "trna", "nc", "trna", "trna",
         "trna", "nc", "cds", "trna", "nc", "trna",
         "cds", "nc", "trna", "nc", "cds", "cds",
         "cds", "trna", "cds", "trna", "cds", "cds",
         "trna", "trna", "trna", "cds", "cds", "trna",
         "nc", "cds", "trna", "nc", "trna"]

NT_LENGTHS = [1122, 71, 954, 69, 1559, 75, 2,
              956, 69, 72, 1, 68, 1042,
              68, 7, 69, 1, 73, 66,
              66, 12, 1542, 72, 3, 68,
              684, 25, 70, 1, 207, 681,
              784, 68, 346, 65, 297, 1378,
              69, 59, 71, 1812, 525, 69,
              4, 1141, 66, 2, 69]

STARTS = [0, 576, 647, 1601, 1670, 3229, 3304,
          3306, 4262, 4331, 4400, 4401, 4469,
          5511, 5579, 5586, 5655, 5656, 5729,
          5826, 5891, 5903, 7445, 7514, 7517,
          7585, 8269, 8294, 8364, 8365, 8572,
          9207, 9990, 10058, 10404, 10469, 10766,
          12137, 12206, 12265, 12336, 14148, 14673,
          # 14742, 14746, 15887, 15953, 15955]
          14742, 14746, 15887, 15953, 15955, 16023]

STRANDS = ["L", "H", "H", "H", "H", "H", "",
           "H", "H", "L", "", "H", "H",
           "H", "", "L", "", "L", "L",
           "L", "", "H", "L", "", "H",
           "H", "", "H", "", "H", "H",
           "H", "H", "H", "H", "H", "H",
           "H", "H", "H", "H", "L", "L",
           "", "H", "H", "", "L", "L"]

COLORS = {
    "trna": "#4169e1",  # royalblue
    "rrna": "#cd5c5c",  # indianred
    "reg": "#ffa500",  # orange
    "cds": "#2e8b57",  # seagreen
    "nc": "grey",
}

TEXT_HA = ["center", "center", "right", "right", "right", "right", "center",
           "right", "right", "center", "center", "right", "right",
           "right", "center", "center", "center", "left", "center",
           "left", "center", "right", "center", "center", "center",
           "center", "center", "right", "center", "center", "left",
           "left", "left", "left", "left", "left", "left",
           "left", "left", "left", "left", "right", "right",
           "center", "left", "center", "center", "center"]

TEXT_VA = ["top", "bottom", "bottom", "bottom", "bottom", "center",
           "center",
           "bottom", "center", "center", "center", "center", "center",
           "top", "center", "center", "center", "center", "center",
           "center", "center", "top", "top", "center", "top",
           "top", "center", "top", "center", "top", "top",
           "top", "top", "top", "top", "top", "top",
           "center", "center", "center", "center", "center", "center",
           "center", "bottom", "bottom", "center", "center"]

TEXT_Y = [19.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2,
          25.2, 25.2, 19.2, 25.2, 25.2, 25.2,
          25.2, 25.2, 19.2, 19.2, 19.2, 19.2,
          19.2, 25.2, 25.2, 19.2, 25.2, 25.2,
          25.2, 25.2, 25.2, 25.2, 25.2, 25.2,
          25.2, 25.2, 25.2, 25.2, 25.2, 25.2,
          25.2, 25.2, 25.2, 25.2, 19.2, 19.2,
          25.2, 25.2, 25.2, 25.2, 19.2]
