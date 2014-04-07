__author__ = 'deezzy'

"""
Stakeout

Congratulations! You are the new elite hacker in a group of villainous ne'er-do-wells.

Luckily this group is more savvy than your last band of ruffians, and they are looking to software (and you) to improve their take.
The con man for the team, has gone door-to-door down each street posing as a termite inspector so he could covertly total the valuable goods in each house.
Normally the gang would just rob all the valuable homes, but there's a catch!
Whenever a house is robbed in this wealthy neighborhood, the police watch it and the neighboring houses for months.
So the gang can't simply rob all the homes, and if they choose to rob one, they can no longer rob the house on either side of it.
The ringleader wants to know what houses he should rob to maximize the team's profit, and he wants to know now.
Write a function that takes in an array of positive integers (home values) and returns the maximum expected value of robbing that street.

For example:

[ 20, 10, 50, 5, 1 ] should return $71, as robbing the first, third, and fifth houses is optimal [ 20, x, 50, x, 1 ]

[ 20, 50, 10, 1, 5 ] should return $55, as robbing the second and fifth houses is optimal [ x, 50, x, x, 5 ]


Problem definition:

    The basic idea is to calculate max sum subsequence in an array of +ve integers (since valuables can't have -ve value)
    where no two integers in the max sum subsequence are adjacent.

    In graph theory an independent set of a graph G is the set of vertices of G, no two of which are adjacent.
    Maximum independent set is the largest set of the graph. In a weight graph, a graph with each vertex having weights,
    we defined weighted independent set or WIS as the subset of vertices of G with maximum sum of weights.

    Suppose, v_n is the last vertex in the path graph, to draw analogy of our neighbourhood we assume each house in the
    neighborhood represents vertices in the path graph with value of valuables in each household representing
    weight of the vertex.

    We need to find out the optimal IS of G which is the maximum IS of G. There are two possibilities about how the
    optimal solution would look like. S be the WIS of G and G' is the reduced path graph of G with v_n removed.

    Case 1:
        S doesn't include v_n.
        Then by definition of WIS S will be WIS of G' as well.
    Case 2:
        S includes v_n => S can't contain v_(n-1).
        Let G'' be the sub graph of G with v_n and v_(n-1) removed.
        S - {v_n} has to be optimal IS of G''.


    Thus optimal IS of G:
            i.  optimal IS of G' or
            ii. optimal IS of G'' + v_n

    max_independent_set() finds optimal IS of a path graph G, in our case the richy rich neighborhood.
    neighborhood_path_graph: is an array of costs (of household valuables)
    the output of the program is max sum

"""


def max_independent_set(neighborhood_path_graph):
    exclude_max_sum = 0
    include_max_sum = neighborhood_path_graph[0]
    exclude_max_sum_new = None
    for item in neighborhood_path_graph[1:]:
        exclude_max_sum_new = max(include_max_sum, exclude_max_sum)
        include_max_sum = exclude_max_sum + item
        exclude_max_sum = exclude_max_sum_new

    return max(include_max_sum, exclude_max_sum)

if __name__ == "__main__":
    print max_independent_set([20, 10, 50, 5, 1])
    print max_independent_set([20, 50, 10, 1, 5])
    print max_independent_set([5, 5, 10, 100, 10, 5])
    print max_independent_set([48727, 8442, 747377373, 2, 873627663, 3983782])
