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

thetas = [0.0, 0.2264460739936025, 0.42100368157402374, 0.6151816645542881,
          0.9241960890820207, 1.234349387410224, 1.430045868791116,
          1.6246034763715373, 1.6513670106826002, 1.6779407326935845,
          1.8886323857806748, 2.099324038867765, 2.1253283239785143,
          2.1522816705896557, 2.1786655803005615, 2.203720803910918,
          2.5089389824370816, 2.8152960347637155, 2.8418697567746998,
          2.984608606433702, 3.1277270806928605, 3.180305087814594,
          3.348858410284266, 3.6269334298992097, 3.788653509566057,
          3.8672358017985395, 3.9452486571307865, 4.013960709759189,
          4.331896312390609, 4.60655471060414, 4.630850685014183,
          4.655526284024383, 5.012942845072122, 5.456534190355484,
          5.569282696602088, 5.798955579697025, 6.028059025891725,
          6.053683686402318]

widths = [0.4259388013760637, 0.026953346611141286, 0.3621618685497012,
          0.026194097410827448, 0.5918347516446376, 0.028471845011768967,
          0.36292111775001507, 0.026194097410827448, 0.027332971211298206,
          0.025814472810670532, 0.3955688333635102, 0.025814472810670532,
          0.026194097410827448, 0.02771259581145513, 0.02505522361035669,
          0.02505522361035669, 0.58538113344197, 0.027332971211298206,
          0.025814472810670532, 0.259663226507333, 0.02657372201098437,
          0.07858229223248235, 0.2585243527068622, 0.2976256865230249,
          0.025814472810670532, 0.13135011165429417, 0.02467559901019977,
          0.11274850624660511, 0.5231226990162352, 0.026194097410827448,
          0.022397851409258256, 0.026953346611141286, 0.6878797754843382,
          0.19930291508238276, 0.026194097410827448, 0.4331516687790452,
          0.02505522361035669, 0.026194097410827448]
