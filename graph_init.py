from graph import  *

# All provinces including Alberta
provinces = [
    "British Columbia", "Alberta", "Saskatchewan", "Ontario",
    "Quebec", "Newfoundland and Labrador", "Nova Scotia", "Ottawa"
]

# Initialize graph
g = Graph(provinces)

# Add all edges
edges = [
    # Format: (Start, End, Hops, Distance, Time, Dementors)
    ("British Columbia", "Saskatchewan", 13, 1800, 19, 6),
    ("Alberta", "Quebec", 3, 2000, 21, 7),
    ("Ontario", "Nova Scotia", 2, 1300, 13, 4),
    ("Quebec", "Newfoundland and Labrador", 13, 1900, 20, 26),
    ("Nova Scotia", "Saskatchewan", 2, 1800, 18, 5),
    ("Alberta", "Saskatchewan", 6, 1600, 8, 3),
    ("Newfoundland and Labrador", "Alberta", 4, 2400, 24, 9),
    ("Ontario", "Quebec", 10, 500, 5, 1),
    ("Nova Scotia", "Ontario", 3, 2000, 21, 7),
    ("Saskatchewan", "Nova Scotia", 3, 2000, 20, 37),
    ("Quebec", "Saskatchewan", 4, 200, 2, 0),
    ("Alberta", "Ottawa", 3, 2400, 24, 9),
    ("Saskatchewan", "Quebec", 2, 2000, 20, 6),
    ("Ontario", "Alberta", 2, 1500, 16, 4),
    ("British Columbia", "Saskatchewan", 2, 1200, 14, 3),
    ("Newfoundland and Labrador", "Quebec", 3, 2200, 22, 7),
    ("Nova Scotia", "Newfoundland and Labrador", 10, 1200, 12, 6),
    ("Quebec", "Ottawa", 29, 1800, 19, 17),
    ("Alberta", "British Columbia", 2, 1800, 18, 27),
    ("British Columbia", "Quebec", 2, 1900, 19, 7),
    ("Ontario", "Newfoundland and Labrador", 3, 2300, 23, 8),
    ("Nova Scotia", "Alberta", 3, 2200, 22, 8),
    ("Newfoundland and Labrador", "Alberta", 3, 2300, 23, 8),
    ("Alberta", "Newfoundland and Labrador", 3, 2400, 24, 9),
    ("Saskatchewan", "British Columbia", 3, 2000, 21, 8),
    ("Ontario", "Saskatchewan", 2, 1600, 16, 5),
    ("Quebec", "Nova Scotia", 2, 1000, 10, 2),
    ("Newfoundland and Labrador", "Saskatchewan", 4, 2200, 23, 19),
    ("Nova Scotia", "Quebec", 2, 1100, 11, 2),
    ("British Columbia", "Newfoundland and Labrador", 4, 2500, 26, 10),
    ("Ontario", "Ottawa", 7, 1450, 4, 12),
    ("Alberta", "Saskatchewan", 5, 600, 8, 3),
    ("Quebec", "Alberta", 2, 1700, 17, 6),
    ("Saskatchewan", "Nova Scotia", 9, 1800, 18, 5),
    ("Alberta", "Quebec", 6, 2000, 21, 6),
    ("Nova Scotia", "British Columbia", 4, 2500, 26, 10),
    ("Ontario", "Nova Scotia", 12, 1300, 13, 4),
    ("British Columbia", "Saskatchewan", 13, 1800, 19, 6),
]

for edge in edges:
    g.add_edge(*edge)