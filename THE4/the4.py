def OX_to_tree(L):
    if len(L) == 1:
        return L[0]

    datum = L[datum_finder(L)]
    subtrees = ayiklayici(L)
    result = [datum]

    if len(subtrees) == 1:
        kucuk_list = L[:]
        kucuk_list.remove(datum)
        result.append(OX_to_tree(kucuk_list))
        return result

    for subtree in subtrees:
        if len(subtree) == 1:
            result.append(subtree[0])
        else:
            result.append(OX_to_tree(subtree))

    return result

def datum_finder(L):
    max_o_index = -1
    max_o = -1
    for i in range(len(L)):
        amount_of_o = L[i].count("o")
        if amount_of_o > max_o:
            max_o_index = i
            max_o = amount_of_o
    return max_o_index

def first_children_finder(L):
    datum_tree = L[datum_finder(L)]
    amount_of_x = datum_tree.count("x")
    children = []
    for i in range(len(L)):
        if L[i].count("x") == amount_of_x + 1:
            children.append(L[i])
    return children

def ayiklayici(L):
    children = first_children_finder(L)
    subtrees = []
    control_list = L[:]
    usage_table = {string: [] for string in L} #Her stringin hangi parentlara ait olduğu

    def expand_subtree(subtree, available_strings):
        added = True #genişleme olduğu sürece devam et
        while added:
            added = False
            for string in available_strings:
                for node in subtree: #subtreedeki her bir node'la ve yeni eklenen ve artık node olan stringler üzerinde dolaş
                    #Daha önce aynı parentla eşleşmemişse ve uyumluysa ekle
                    if is_valid_child(node, string) and node not in usage_table[string]:
                        subtree.append(string)
                        usage_table[string].append(node)#string'e parent ekle
                        available_strings.remove(string)#string'i kullanılabilirler listesinden çıkar
                        added = True
                        break #string subtree'ye eklendikten sonra diğer nodelara bakmaya gerek yok
        return subtree

    def place_orphans(available_strings):
        #açıkta kalan stringleri uygun yerlere yerleştir
        remaining_strings = available_strings[:]
        for string in remaining_strings:
            for subtree in subtrees: #mevcut subtreelerde dolaş
                parent_count = 0
                self_count = 0
                for node in subtree:
                    if is_valid_child(node, string):
                        parent_count+=1
                    if node == string:
                        self_count+=1
                if parent_count>self_count:
                    subtree.append(string)
                    available_strings.remove(string) #string'i kullanılabilirler listesinden çıkar
                    break

    for child in children:
        subtree = [child] #subtree'nin başlangıcı first_children_finder'ın buldukları
        control_list.remove(child)#çıkartsaydık da bir şey değişmezdi sadece verimliliği ve gereksiz kontrolleri azaltıyor
        subtree = expand_subtree(subtree, control_list)
        subtrees.append(subtree)

    place_orphans(control_list)
    place_orphans(control_list)
    place_orphans(control_list)

    return subtrees

def is_valid_child(parent, child):
    for i in range(len(parent)):
        if parent[i] == "x" and child[i] != "x":
            return False
    return parent.count("o") == child.count("o") + 1
