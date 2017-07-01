from graph import Graph
import xlrd
import pandas as pd


#Get the places name
b = xlrd.open_workbook("data.xlsx")
sh = b.sheet_by_index(0)
places = sh.row_values(0)
marked = []

del places[0]

distances = pd.read_excel('data.xlsx').as_matrix()
print distances[places.index("Gabtoli")][places.index("Kalshi")]

print distances

g = Graph()
for p in places:

    dist_from_p = {}
    idx_p = places.index(p)
    for q in places:
        idx_q = places.index(q)
        dist_from_p[q] = float(distances[idx_p][idx_q])
    g.add_vertex(p, dist_from_p)

print(g.shortest_path('Kalshi', "Gabtoli"))