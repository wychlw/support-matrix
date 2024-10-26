from src.ruyi_index_parser.index_maintainer import PackageIndex

with PackageIndex() as p:
    b=p.parse_board()
    print(b)
