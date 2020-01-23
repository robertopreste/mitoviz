#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste

NAMES = ["DLOOP", "TF", "RNR1", "TV", "RNR2", "TL1",
         "ND1", "TI", "TQ", "TM", "ND2", "TW", "TA", "TN",
         "TC", "TY", "CO1", "TS1", "TD", "CO2", "TK", "ATP8",
         "ATP6", "CO3", "TG", "ND3", "TR", "ND4L", "ND4", "TH",
         "TS2", "TL2", "ND5", "ND6", "TE", "CYTB", "TT", "TP"]

NT_LENGTHS = [1122, 71, 954, 69, 1559, 75,
              956, 69, 72, 68, 1042, 68, 69, 73,
              66, 66, 1542, 72, 68, 684, 70, 207,
              681, 784, 68, 346, 65, 297, 1378, 69,
              59, 71, 1812, 525, 69, 1141, 66, 69]

TYPES = ["reg", "trna", "rrna", "trna", "rrna", "trna",
         "cds", "trna", "trna", "trna", "cds", "trna", "trna", "trna",
         "trna", "trna", "cds", "trna", "trna", "cds", "trna", "cds",
         "cds", "cds", "trna", "cds", "trna", "cds", "cds", "trna",
         "trna", "trna", "cds", "cds", "trna", "cds", "trna", "trna"]

COLORS = {
    "trna": "#4169e1",  # royalblue
    "rrna": "#cd5c5c",  # indianred
    "reg": "#ffa500",  # orange
    "cds": "#2e8b57",  # seagreen
}

TEXT_HA = ["center", "center", "right", "right", "right", "right", "right",
           "center", "right", "center", "right", "right", "center", "right",
           "center", "right", "right", "center", "center", "center", "center",
           "center", "left", "left", "left", "left", "left", "left", "left",
           "left", "center", "left", "left", "left", "center", "left",
           "center", "center"]

TEXT_VA = ["bottom", "bottom", "bottom", "bottom", "bottom", "center",
           "bottom", "center", "center", "center", "center", "top", "top",
           "top", "top", "top", "top", "top", "top", "top", "top", "top",
           "top", "top", "top", "top", "top", "top", "top", "center", "center",
           "center", "center", "center", "bottom", "bottom", "bottom",
           "center"]

TEXT_Y = [25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 19.2, 25.2, 19.2, 25.2,
          25.2, 19.2, 25.2, 19.2, 25.2, 25.2, 25.2, 19.2, 25.2, 19.2, 25.2,
          25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 19.2, 25.2, 25.2,
          25.2, 25.2, 25.2, 25.2, 19.2]
