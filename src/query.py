"""

* Lexical features that can be tested in a pattern:
    - token "name" (e.g. "AK-47")
    - lexical category (e.g. "adj")
    - root (e.g. "shoot")
    - conceptual category (e.g. "human")
* Logical combination of lexical feature tests
    - OR, AND ,and NOT
* Wild cards
    $ - 0 or 1 tokens
    * - 0 or more tokens
    + - 1 or more tokens
* Variable assignment from pattern components
    =
* Grouping operators:
    <>  for grouping
    []  for disjunctive grouping
* Repetition
    * - 0 or more
    + - 1 or more
* Range
    - 0 to N
    - 1 to N

"""

question = "Which countries are the neighbours to India and Nepal?"
