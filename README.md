# CVD-Python-Scripts
The python scripts to generate the searching trees of CVD problem is provided in this repository.

In the output, the search tree is described by a list of branching vectors and this list is defined recursively.
Let $L$ be the list of the search tree(subtree) $T$ whose root is $r$.
Suppose that the branching vector of $r$ is $(d_1,d_2)$. Let $L_1$ and $L_2$ be the lists of the left son and rigth son of node $r$.
Then the list of $T$ is described as ${(d_1,d_2),L_1,L_2}$ in our output.

Python Scripts/code1.py This python script to generate the searching trees when $vc(H^v) \ge 4$. The ouput contains the structure of search trees, the branching vector and the corresponding branching factor,

Python Scripts/code2.py This python script to generate the searching trees when $vc(H^v) = 4$. The ouput contains the structure of search trees, the branching vector and the corresponding branching factor,

Python Scripts/branching.py This python sctript is to calculate the branching factor of a branching vector.
