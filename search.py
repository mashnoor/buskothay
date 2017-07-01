from graph import Graph
import xlrd
import pandas as pd


#Get the places name
b = xlrd.open_workbook("distances.xlsx")
sh = b.sheet_by_index(0)
places = sh.row_values(0)
marked = []

del places[0]

distances = pd.read_excel('distances.xlsx').as_matrix()


g = Graph()
for p in places:

    dist_from_p = {}
    idx_p = places.index(p)
    for q in places:
        idx_q = places.index(q)
        dist_from_p[q] = float(distances[idx_p][idx_q])
    g.add_vertex(p, dist_from_p)

def get_path(from_place, to_place):
    return g.shortest_path(from_place, to_place)