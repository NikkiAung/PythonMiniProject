# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
resultsTable = [["Mattson", 686, 22.87], ["Blair", 380, 12.67],
                ["Leonhardt", 1051, 35.05], ["Miller", 406, 13.53],
                ["Rowan", 477, 15.90]]

layout = ""                     # For formatting
totalVote = 0                   # Running total
totalPercent = 0.0
layout = '{:<10}   {:>7}   {:>7}'
print(layout.format('Candidate', 'Vote', 'Percent'))
layout = '{:<10}   {:>7}   {:>6.1f}'
for res in resultsTable:
    totalVote += res[1]
    totalPercent += res[2]
    print(layout.format(res[0],res[1],res[2]))
print('=' * 30)
layout = '{:<10}   {:>7}   {:>6.1f}'
print(layout.format('Total', totalVote, totalPercent))